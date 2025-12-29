# AI-Driven Social Media Content Scheduler
## Final Year Computer Science Project

an Intelligent Social Media Scheduler that uses AI Agents (Google Gemini 2.0) to optimize content, research posting times, and analyze trends.

### 🚀 Project Objective
To build a system that helps users create high-engagement content by leveraging AI for:
- **Optimization**: Rewriting text for different platforms (LinkedIn, Twitter, Instagram).
- **Timing Research**: Finding the best times to post based on timezone/platform.
- **Trend Analysis**: Suggesting viral topics.

### 🛠️ Tech Stack
- **Backend**: FastAPI (Python), SQLAlchemy, Pydantic
- **Database**: MySQL
- **AI Engine**: Google Gemini 2.0 Flash (`google-generativeai`)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

### 📂 Folder Structure
```
/social_media_app
    /backend         # FastAPI Application
        /app
            /agents  # AI Agent Logic (Gemini)
            /routers # API Endpoints
            models.py
            main.py
    /frontend        # User Interface
    database_setup.sql
```

### ⚙️ Setup Instructions

1. **Database Setup**:
   - Install MySQL Server.
   - Run the script `database_setup.sql` in your MySQL Workbench or Command Line.
   - Update `backend/.env` with your DB credentials if they differ from default.

2. **Backend Setup**:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
   *Server runs at: http://localhost:8000*

3. **Frontend Usage**:
   - Open `frontend/index.html` in any browser.
   - **Login**: (Demo Mode) Use any username/password combination (Registration simulated).

### 🤖 AI Agent Workflow
1. **Content Optimization Agent**: Analyzes your draft -> Rewrites it -> Assigns a Score (1-10).
2. **Timing Research Agent**: Queries knowledge base for optimal times -> Returns list + Reasoning.
3. **Trend Agent**: Suggests 3 trending topics for the selected platform.

### 🧪 Demo Flow for Viva/Presentation
1. **Login Page**: Show the clean UI. Login as "Admin".
2. **Dashboard**: 
   - Type "I launched a new product today" in the Composer.
   - Select "LinkedIn" -> Click **Optimize**.
   - Show how AI rewrites it professionally with hashtags.
3. **Research**:
   - Go to Sidebar -> Select "Twitter".
   - Click **Research Best Times**.
   - Show the dynamic result (e.g., "Tuesday 9 AM").
4. **Scheduling**:
   - Click **Schedule This Post**.
   - Show it appear in the "Upcoming Schedule" list.

---
**Note**: This is a simulated environment for Final Year Project demonstration purposes.
