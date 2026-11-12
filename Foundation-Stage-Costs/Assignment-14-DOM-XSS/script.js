// تجميد إعدادات العناصر لمنع التعديل عليها من المتصفح 
const DOM_CONFIG = Object.freeze({
    inputId: "userInput",
    unsafeBox: document.getElementById("unsafeBox"),
    safeBox: document.getElementById("safeBox"),
    statusNote: document.getElementById("statusNote")
});

// العرض غير الآمن:  (يسمح بتنفيذ أكواد XSS)
document.getElementById("btnUnsafe").addEventListener("click", function () {
    const value = document.getElementById(DOM_CONFIG.inputId).value;
    DOM_CONFIG.unsafeBox.innerHTML = value;
    DOM_CONFIG.statusNote.textContent = "[WARNING] Rendered via innerHTML: Input parsed as executable HTML/JS!";
});

// العرض الآمن: بناء العنصر عبر createElement وإسناد النص لـ textContent
document.getElementById("btnSafe").addEventListener("click", function () {
    const value = document.getElementById(DOM_CONFIG.inputId).value;
    DOM_CONFIG.safeBox.textContent = "";

    const item = document.createElement("div");
    item.textContent = value;
    DOM_CONFIG.safeBox.appendChild(item);

    DOM_CONFIG.statusNote.textContent = "[SECURE] Rendered via textContent & createElement: Payload neutralized as plain text.";
});
