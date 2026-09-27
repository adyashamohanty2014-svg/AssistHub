# AssistHub

## Assistive Technology for All

AssistHub is a web-based assistive technology platform developed to make assistive devices easier to **discover, understand, compare, and explore**.

The platform brings information about different assistive devices into one place and provides features such as intelligent search, sorting, device comparison, reviews, personalized recommendations, and an AI-powered assistant.

---

## Project Overview

Finding suitable assistive technology can be challenging because information about different devices is often distributed across multiple platforms.

**AssistHub** aims to provide a centralized platform where users can explore assistive devices based on their needs and preferences.

Users can browse devices, search for specific products, view detailed information, compare devices, read reviews, save devices to their wishlist, and receive personalized recommendations.

The platform also includes an **AI Assistant** that helps users interact with the system and explore assistive technology more easily.

---

## Objectives

The main objectives of AssistHub are to:

* Provide a centralized platform for discovering assistive devices.
* Make assistive technology information easier to understand.
* Allow users to search and sort devices efficiently.
* Help users compare different assistive devices.
* Provide community-based reviews and ratings.
* Offer personalized device recommendations.
* Provide an AI-powered assistant for easier interaction.
* Create a responsive and user-friendly interface.

---

## Key Features

### Smart Device Search

Users can search for assistive devices using keywords.

The search system can consider information such as:

* Device name
* Brand
* Category
* Description
* Tags
* Related search terms

It also supports variations of common assistive technology terms.

For example:

```text
Wheelchair
Wheel Chair
Hearing Aid
Mobility Aid
Braille
Vision Aid
Communication Aid
```

---

### Device Sorting

Users can sort available devices according to the sorting options provided by the platform.

This makes it easier to organize and browse a large number of assistive devices.

---

### Device Categories

Assistive devices are organized into categories so users can quickly browse devices belonging to a particular area of assistive technology.

The category-based browsing system helps users narrow down their search and discover relevant devices.

---

### Detailed Device Information

Each device has a dedicated detail page containing relevant information such as:

* Device name
* Brand
* Category
* Description
* Specifications
* Price information
* Tags
* Ratings
* Reviews
* Related devices

This allows users to understand a device before comparing or saving it.

---

### Reviews and Ratings

Users can share their experiences by submitting reviews and ratings for devices.

The review system provides:

* User reviews
* Star ratings
* Average ratings
* Review history

This allows users to consider feedback from other users when exploring devices.

---

### Wishlist

Users can save devices to their wishlist.

This allows users to keep track of devices they are interested in and revisit them later.

---

### Device Comparison

AssistHub provides a dedicated comparison feature that allows users to compare multiple devices side by side.

Users can compare available information such as:

* Device name
* Brand
* Category
* Price
* Rating
* Description
* Specifications

The comparison feature makes it easier to examine different options together.

---

### AI Assistant

AssistHub includes an AI-powered assistant designed to make interacting with assistive technology information easier.

Users can ask questions and receive AI-generated assistance related to assistive technology and the devices available through the platform.

The AI assistant provides an additional conversational way to explore the platform.

> AI-generated responses are intended for general informational purposes and should not replace professional medical or accessibility advice.

---

### Personalized Recommendations

AssistHub provides a **Recommended For You** section to help users discover relevant devices.

Recommendations can consider available user activity such as:

* Recent searches
* Previously reviewed device categories
* Wishlist activity
* Highly rated devices

The system can also provide general recommendations when sufficient user activity is not available.

---

### Best Purchases

The platform includes a **Best Purchases** section that highlights highly rated devices.

This provides users with another way to discover devices that have received positive ratings.

---

### User Profiles

Registered users have access to their own profiles.

The user system supports features such as:

* User registration
* Login
* Profile management
* Review history
* Wishlist
* Personalized recommendations

---

### Light and Dark Theme

AssistHub supports both **light and dark themes**.

Users can switch between themes according to their preference.

---

### Responsive Design

The interface is designed to provide a consistent experience across different screen sizes.

The website supports:

* Desktop
* Laptop
* Tablet
* Mobile devices

Responsive layouts are applied across the major sections of the platform.

---

## Technology Stack

### Backend

* Python
* Django 6.0.6
* Django ORM
* Django Authentication System

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Database

* SQLite
* Django ORM

### AI Integration

* AI-powered assistant integrated into the Django application

### Version Control

* Git
* GitHub

### Development Environment

* Visual Studio Code

---

## System Modules

The AssistHub application is divided into several major functional modules.

### 1. User Authentication Module

Handles:

* Registration
* Login
* User authentication
* User profiles

### 2. Device Management Module

Handles:

* Device information
* Device categories
* Device details
* Device listings

### 3. Search and Sorting Module

Handles:

* Keyword search
* Search suggestions
* Search aliases
* Relevance-based results
* Device sorting

### 4. Recommendation Module

Provides personalized device recommendations based on available user activity.

### 5. Review and Rating Module

Handles:

* User reviews
* Device ratings
* Average ratings
* Review history

### 6. Wishlist Module

Allows authenticated users to save and manage devices they are interested in.

### 7. Device Comparison Module

Allows users to compare multiple assistive devices side by side.

### 8. AI Assistant Module

Provides a conversational interface for interacting with assistive technology information.

### 9. Theme and Responsive UI Module

Provides:

* Light and dark theme
* Responsive layouts
* Mobile-friendly interface
* Consistent visual design

---

## Application Pages

The platform contains several major pages and interfaces:

| Page               | Purpose                                                         |
| ------------------ | --------------------------------------------------------------- |
| **Home**           | Introduction, categories, recommendations, and featured devices |
| **Devices**        | Browse, search, and sort assistive devices                      |
| **Device Details** | View detailed information about a specific device               |
| **Compare**        | Compare multiple devices                                        |
| **About Us**       | Information about the platform                                  |
| **Contact**        | Contact interface                                               |
| **Profile**        | Manage user profile and user-specific information               |
| **My Wishlist**    | View saved devices                                              |
| **My Reviews**     | View submitted reviews                                          |
| **AI Assistant**   | Interact with the AI-powered assistant                          |

---

## How AssistHub Works

The basic user flow is:

```text
              ┌─────────────────┐
              │     AssistHub   │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Browse / Search │
              │    Devices      │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Device Details  │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
      Compare      Wishlist      Reviews
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
              Personalized
              Recommendations
                       │
                       ▼
                 AI Assistant
```

---

## Project Highlights

AssistHub combines multiple functionalities into a single assistive technology platform:

* Intelligent device search
* Device sorting
* Category-based browsing
* Detailed device information
* Reviews and ratings
* Wishlist management
* Device comparison
* Personalized recommendations
* AI-powered assistance
* User authentication and profiles
* Light and dark theme
* Responsive interface

---

## Security Considerations

The project uses Django's built-in security and authentication mechanisms.

Security-related features include:

* User authentication
* Password hashing through Django
* CSRF protection
* Authenticated access to user-specific functionality
* Secure handling of application credentials

Sensitive API credentials should be kept outside the source code and should not be committed to the repository.

---

## Testing and Validation

The project has been checked using Django's built-in validation and testing framework.

The application has been tested across major functionality including:

* User authentication
* Device browsing
* Device search
* Device sorting
* Device details
* Reviews
* Wishlist
* Device comparison
* AI assistant
* User profile
* Responsive interface

Django system checks were also performed to identify configuration issues.

---

## Future Scope

AssistHub can be further enhanced with:

* Advanced device filtering
* More sophisticated recommendation algorithms
* Voice-based search
* Voice interaction with the AI assistant
* Multilingual support
* Additional assistive technology categories
* Real-time product availability
* Price comparison across different platforms
* Improved accessibility based on WCAG guidelines
* More extensive automated testing
* Production deployment
* Additional AI-powered accessibility features

---

## Team

### Project Members

**Srutirani Sahoo**

**Adyasha Mohanty**

---

## Project Purpose

AssistHub was developed as an academic/software development project with the objective of exploring how web technologies and AI can be used to make information about assistive technology more accessible and easier to navigate.

The project combines:

**Web Development + Database Management + Search + Recommendations + AI**

into a single platform focused on assistive technology.

---

## Project Status

**Status: Completed / Functional**

The current implementation includes the major planned features of the AssistHub platform, including device discovery, search, sorting, comparison, reviews, wishlist functionality, recommendations, user accounts, responsive UI, theme switching, and AI assistance.

---

## AssistHub

### Making assistive technology easier to discover, understand, and compare.
