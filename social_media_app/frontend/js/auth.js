const API_URL = "http://localhost:8000/auth";

document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem("token", data.access_token);
            window.location.href = "dashboard.html";
        } else {
            alert("Login failed! Check credentials.");
        }
    } catch (err) {
        alert("Error connecting to server");
    }
});

function toggleMode() {
    alert("Demo Mode: Registration is auto-handled in real app (or just implement similar logic). For now, try logging in with any details, if fails, use 'register' endpoint manually via swagger or add register UI logic here.");
}
