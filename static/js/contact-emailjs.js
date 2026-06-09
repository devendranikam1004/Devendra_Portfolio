// ─────────────────────────────────────────────────
//  EMAILJS CONFIGURATION — fill these in
// ─────────────────────────────────────────────────
const EMAILJS_PUBLIC_KEY  = "gzx3wnAB1xn6c1X7P";
const EMAILJS_SERVICE_ID  = "service_5yfvl8l";
const EMAILJS_TEMPLATE_ID = "template_l0u6d6p";

emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

// ── Toast helper ──────────────────────────────────
function showToast(msg, type = "success") {
    const toast = document.getElementById("toast");
    const icon  = type === "success"
        ? '<i class="fa-solid fa-circle-check"></i>'
        : '<i class="fa-solid fa-circle-xmark"></i>';
    toast.className = `toast toast-${type}`;
    toast.innerHTML = icon + " " + msg;
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 4000);
}

// ── Show confirmation card ────────────────────────
function showConfirmCard(name, email, message) {
    document.getElementById("confirmName").textContent    = name;
    document.getElementById("confirmEmail").textContent   = email;
    document.getElementById("confirmMessage").textContent = message;

    document.getElementById("contactForm").style.display  = "none";
    document.getElementById("confirmCard").classList.add("visible");
}

// ── Send another message button ───────────────────
document.getElementById("sendAgainBtn").addEventListener("click", function () {
    document.getElementById("contactForm").style.display = "";
    document.getElementById("confirmCard").classList.remove("visible");
    document.getElementById("contactForm").reset();
});

// ── Form submit ───────────────────────────────────
document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const form    = this;
    const btn     = document.getElementById("submitBtn");
    const btnText = document.getElementById("submitText");

    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    const name    = document.getElementById("name").value.trim();
    const email   = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    // Loading state
    btn.disabled = true;
    btnText.textContent = "Sending…";
    btn.querySelector("i").className = "fa-solid fa-spinner fa-spin";

    const now = new Date().toLocaleString("en-IN", {
        day: "2-digit", month: "short", year: "numeric",
        hour: "2-digit", minute: "2-digit", hour12: true,
    });

    const templateParams = {
        name:       name,
        from_email: email,
        message:    message,
        time:       now,
    };

    emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, templateParams)
        .then(() => {
            showConfirmCard(name, email, message);
            showToast("Message sent! I'll get back to you soon.", "success");
        })
        .catch((err) => {
            console.error("EmailJS error:", err);
            showToast("Oops! Something went wrong. Please try again.", "error");
            btn.disabled = false;
            btnText.textContent = "Send Message";
            btn.querySelector("i").className = "fa-solid fa-paper-plane";
        });
});