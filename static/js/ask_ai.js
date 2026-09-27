const form = document.getElementById("ai-question-form");
const textarea = document.getElementById("ai-question");
const submitButton = document.getElementById("ai-submit-button");
const conversationList = document.getElementById("conversation-list");
const conversation = document.getElementById("conversation");

if (form && textarea && submitButton && conversationList) {
    const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;

    function addMessage(className, label, text) {
        const message = document.createElement("div");
        message.className = `chat-message ${className}`;
        const messageLabel = document.createElement("span");
        messageLabel.className = "message-label";
        messageLabel.textContent = label;
        const messageText = document.createElement("p");
        messageText.textContent = text;
        message.append(messageLabel, messageText);
        conversationList.querySelector(".conversation-empty")?.remove();
        conversationList.appendChild(message);
        return message;
    }

    function addTypingMessage() {
        const message = document.createElement("div");
        message.className = "chat-message ai-message typing-message";
        message.setAttribute("aria-label", "AssistHub AI is thinking");
        const label = document.createElement("span");
        label.className = "message-label";
        label.textContent = "AssistHub AI is thinking";
        const dots = document.createElement("span");
        dots.className = "typing-dots";
        dots.innerHTML = "<span></span><span></span><span></span>";
        message.append(label, dots);
        conversationList.appendChild(message);
        return message;
    }

    function updateRecommendations(devices) {
        let products = document.getElementById("recommended-products");
        if (!devices.length) {
            products?.remove();
            return;
        }
        if (!products) {
            products = document.createElement("div");
            products.id = "recommended-products";
            products.className = "recommended-products";
            conversation.after(products);
        }
        products.replaceChildren();
        const heading = document.createElement("h2");
        heading.textContent = "Recommended Products";
        const grid = document.createElement("div");
        grid.className = "ai-recommended-grid";
        devices.forEach((device) => {
            const card = document.createElement("div");
            card.className = "ai-recommended-card";
            if (device.image) {
                const image = document.createElement("img");
                image.src = device.image;
                image.alt = device.name;
                card.appendChild(image);
            }
            const title = document.createElement("h3");
            title.textContent = device.name;
            const brand = document.createElement("p");
            brand.textContent = device.brand || "";
            const price = document.createElement("p");
            price.textContent = `Rs. ${device.price}`;
            const link = document.createElement("a");
            link.href = device.detail_url;
            link.textContent = "View Product";
            card.append(title, brand, price, link);
            grid.appendChild(card);
        });
        products.append(heading, grid);
    }

    async function submitQuestion(question) {
        const trimmedQuestion = question.trim();
        if (!trimmedQuestion || submitButton.disabled) return;
        addMessage("user-message", "You", trimmedQuestion);
        textarea.value = "";
        submitButton.disabled = true;
        submitButton.innerHTML = "<i class=\"fa-solid fa-circle-notch\"></i> Thinking...";
        const typingMessage = addTypingMessage();
        typingMessage.scrollIntoView({ behavior: "smooth", block: "nearest" });
        const controller = new AbortController();
        const timeout = window.setTimeout(() => controller.abort(), 30000);
        try {
            const body = new URLSearchParams({ question: trimmedQuestion, csrfmiddlewaretoken: csrfToken });
            const response = await fetch(form.dataset.endpoint, {
                method: "POST",
                body,
                headers: { "X-Requested-With": "XMLHttpRequest" },
                signal: controller.signal,
            });
            const data = await response.json();
            typingMessage.remove();
            if (!response.ok) throw new Error(data.error || "Request failed");
            addMessage("ai-message", "AssistHub AI", data.response);
            updateRecommendations(data.devices || []);
        } catch (error) {
            typingMessage.remove();
            addMessage("ai-message ai-error", "AssistHub AI", error.name === "AbortError"
                ? "Sorry, I'm having trouble connecting right now. Please try again."
                : (error.message || "Sorry, I'm having trouble connecting right now. Please try again."));
        } finally {
            window.clearTimeout(timeout);
            submitButton.disabled = false;
            submitButton.innerHTML = "<i class=\"fa-solid fa-paper-plane\"></i> Ask AssistHub AI";
            textarea.focus();
        }
    }

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        submitQuestion(textarea.value);
    });

    textarea.addEventListener("keydown", (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            form.requestSubmit();
        }
    });

    document.querySelectorAll(".chip").forEach((chip) => {
        chip.addEventListener("click", () => submitQuestion(chip.textContent));
    });
}