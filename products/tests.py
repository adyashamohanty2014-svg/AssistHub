from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Category, Device, Review
from django.contrib.auth.models import User

class DeviceSearchTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		mobility = Category.objects.create(name="Mobility Aids")
		cls.wheelchair = Device.objects.create(
			name="Everactiv Everyday Premium Foldable Wheelchair",
			category=mobility,
			description="Foldable wheelchair designed for everyday mobility.",
			price=100,
			tags="mobility, wheelchair, elderly",
		)
		hearing = Category.objects.create(name="Hearing Aids")
		cls.hearing_aid = Device.objects.create(
			name="Clear Sound Hearing Aid",
			category=hearing,
			description="A hearing device for people with hearing loss.",
			price=100,
			tags="hearing, hearing loss",
		)
		vision = Category.objects.create(name="Vision and Communication Aids")
		cls.braille_device = Device.objects.create(
			name="Braille Display",
			category=vision,
			description="A braille device for blind users.",
			price=100,
			tags="braille, vision",
		)
		cls.communication_device = Device.objects.create(
			name="Communication Aid",
			category=vision,
			description="A communication device for users who need support.",
			price=100,
			tags="communication, communication aid",
		)

	def search_results(self, query):
		response = self.client.get(reverse("device_list"), {"q": query})
		return response.context["devices"]

	def test_searches_compound_word_and_case(self):
		self.assertIn(self.wheelchair, self.search_results("wheel chair"))
		self.assertIn(self.wheelchair, self.search_results("WHEELCHAIR"))

	def test_searches_category_tags_and_intent_terms(self):
		self.assertIn(self.wheelchair, self.search_results("mobility"))
		self.assertIn(self.hearing_aid, self.search_results("device for hearing loss"))

	def test_searches_braille_vision_and_communication(self):
		self.assertIn(self.braille_device, self.search_results("braille"))
		self.assertIn(self.braille_device, self.search_results("vision aid"))
		self.assertIn(
			self.communication_device,
			self.search_results("communication aid"),
		)

	def test_multiword_searches_match_all_terms(self):
		hearing_results = self.search_results("hearing aid")
		self.assertIn(self.hearing_aid, hearing_results)
		self.assertNotIn(self.wheelchair, hearing_results)
		self.assertNotIn(self.braille_device, hearing_results)
		self.assertIn(self.hearing_aid, self.search_results("hearing"))
		self.assertIn(self.wheelchair, self.search_results("wheelchair"))
		mobility_results = self.search_results("mobility aid")
		self.assertIn(self.wheelchair, mobility_results)
		self.assertNotIn(self.hearing_aid, mobility_results)
		self.assertNotIn(self.braille_device, mobility_results)
		self.assertIn(self.braille_device, self.search_results("braille"))
		vision_results = self.search_results("vision aid")
		self.assertIn(self.braille_device, vision_results)
		self.assertNotIn(self.wheelchair, vision_results)
		self.assertIn(
			self.communication_device,
			self.search_results("communication aid"),
		)

	def test_compare_rejects_same_device(self):
		response = self.client.get(
			reverse("compare"),
			{"device1": self.wheelchair.id, "device2": self.wheelchair.id},
		)
		self.assertEqual(response.context["device1"], self.wheelchair)
		self.assertIsNone(response.context["device2"])
		self.assertContains(
			response,
			"Please select two different devices to compare.",
		)

	def test_compare_allows_different_devices_in_same_category(self):
		response = self.client.get(
			reverse("compare"),
			{
				"device1": self.braille_device.id,
				"device2": self.communication_device.id,
			},
		)
		self.assertEqual(response.context["device1"], self.braille_device)
		self.assertEqual(response.context["device2"], self.communication_device)

	def test_compare_keeps_same_category_warning(self):
		response = self.client.get(
			reverse("compare"),
			{"device1": self.wheelchair.id, "device2": self.hearing_aid.id},
		)
		self.assertIsNone(response.context["device2"])
		self.assertContains(
			response,
			"Please compare devices from the same category.",
		)

	def test_about_statistics_use_database_counts(self):
		response = self.client.get(reverse("about"))
		self.assertEqual(response.context["total_devices"], Device.objects.count())
		self.assertEqual(
			response.context["total_categories"],
			Category.objects.count(),
		)
		self.assertContains(response, "Registered Users")
		self.assertNotContains(response, "1000+")

	def test_home_statistics_use_database_counts(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.context["total_devices"], Device.objects.count())
		self.assertEqual(
			response.context["total_categories"],
			Category.objects.count(),
		)
		self.assertEqual(response.context["total_reviews"], Review.objects.count())
		self.assertEqual(response.context["total_users"], User.objects.count())

	def test_unrelated_query_returns_no_devices(self):
		self.assertFalse(self.search_results("car engine").exists())

	def test_blank_search_returns_all_devices(self):
		response = self.client.get(reverse("device_list"))
		self.assertQuerySetEqual(
			response.context["devices"],
			Device.objects.all(),
			ordered=False,
		)

	def test_price_sorting_uses_template_values(self):
		cheap = Device.objects.create(
			name="Affordable Mobility Device",
			category=self.wheelchair.category,
			description="Mobility support.",
			price=50,
		)
		response = self.client.get(
			reverse("device_list"),
			{"sort": "price_low"},
		)
		self.assertEqual(response.context["devices"][0], cheap)
