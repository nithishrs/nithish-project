const API_BASE = "http://localhost:8000/content";

// Check Auth
if (!localStorage.getItem("token")) {
    window.location.href = "index.html";
}

let lastOptimizedData = null;

async function optimizeContent() {
    const text = document.getElementById("contentInput").value;
    const platform = document.getElementById("platformSelect").value;

    if (!text) return alert("Please enter some text!");

    const res = await fetch(`${API_BASE}/optimize`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, platform })
    });

    const data = await res.json();
    lastOptimizedData = data;

    document.getElementById("optimizationResult").classList.remove("hidden");
    document.getElementById("optimizedText").innerText = data.optimized_text;
    document.getElementById("hashtags").innerText = data.hashtags.join(" ");
    document.getElementById("scoreVal").innerText = data.score;
    document.getElementById("explanation").innerText = data.recommendations;
}

async function researchTiming() {
    const platform = document.getElementById("timePlatform").value;

    // Default timezone
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    const res = await fetch(`${API_BASE}/research-timing`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ platform, timezone })
    });

    const data = await res.json();
    const list = document.getElementById("bestTimesList");
    list.innerHTML = "";
    data.best_times.forEach(t => {
        const li = document.createElement("li");
        li.innerText = t;
        list.appendChild(li);
    });
    document.getElementById("timingReasoning").innerText = data.reasoning;
    document.getElementById("timingResult").classList.remove("hidden");
}

async function analyzeTrends() {
    const platform = document.getElementById("platformSelect").value;
    const res = await fetch(`${API_BASE}/analyze-trends`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ platform })
    });

    const data = await res.json();
    const list = document.getElementById("trendList");
    list.innerHTML = "";
    data.trends.forEach(t => {
        const li = document.createElement("li");
        li.innerText = t;
        list.appendChild(li);
    });
    document.getElementById("trendResult").classList.remove("hidden");
}

async function schedulePost() {
    if (!lastOptimizedData) return;

    // Schedule for 24 hours from now (Simulation)
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);

    const res = await fetch(`${API_BASE}/schedule`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            draft_id: 1, // Demo ID
            platform: document.getElementById("platformSelect").value,
            scheduled_time: tomorrow.toISOString()
        })
    });

    if (res.ok) {
        alert("Post Scheduled!");
        loadSchedule();
    }
}

async function loadSchedule() {
    const res = await fetch(`${API_BASE}/schedule`);
    const data = await res.json();
    const div = document.getElementById("scheduleList");
    div.innerHTML = "";

    if (data.length === 0) div.innerHTML = "<p>No posts scheduled.</p>";

    data.forEach(item => {
        const p = document.createElement("div");
        p.style.padding = "10px";
        p.style.borderBottom = "1px solid #eee";
        p.innerHTML = `<strong>${item.platform_name}</strong> - ${new Date(item.scheduled_datetime).toLocaleString()}`;
        div.appendChild(p);
    });
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

// Init
researchTiming(); // Load initial stats
loadSchedule();
