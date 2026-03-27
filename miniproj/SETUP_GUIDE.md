# MediTrack Setup & Running Procedure

This document outlines the steps taken to get the MediTrack application up and running on your machine. 

## 1. Project Dependencies
The application is built using Python and the Flask framework. The following libraries were required to run it, which were installed via `pip`:
- `flask`: The core web framework.
- `flask-session`: For maintaining user login sessions.
- `werkzeug`: A utility library for Flask (security and routing).
- `pillow`: For processing images when examining uploaded reports.
- `google-generativeai`: For the Gemini AI medical report analysis feature.

**Installation Command used:**
```bash
pip install flask flask-session werkzeug google-generativeai pillow
```

## 2. Database Initialization
Before the application can be used, the SQLite database (`meditrack_final.db`) needs to be created and populated with the necessary tables (`users`, `doctors`, `patients`, `reports`, `disease_map`).

We ran the included initialization script:
```bash
python database.py
```
This script automatically:
1. Created the database file if it didn't exist.
2. Built the schemas for all the tables.
3. **Inserted the default admin credentials** (`admin` / `admin`) into the `users` table so you can successfully log in.
4. Inserted some sample data into the `disease_map` table for the AI symptom checker.

## 3. Running the Server
Finally, we start the Flask web server to host the application locally:
```bash
python app.py
```
This runs the application on localhost over port 5000. 

## 4. How to Access
With the server running in the background, you can open your web browser and navigate to:
**http://127.0.0.1:5000**

You can then log in using the credentials we initialized in step 2:
- **Username:** `admin`
- **Password:** `admin`

## 5. (Optional) Gemini AI configuration
To use the fully functioning AI analysis section for uploaded reports, you'll need a Google Gemini API key. 
If you have one, you export it to your environment like this before starting the server:
- Windows (Command Prompt): `set GEMINI_API_KEY=your_key_here`
- Windows (PowerShell): `$env:GEMINI_API_KEY="your_key_here"`
*(If you do not set it, the application will simply use a mocked fallback text so it won't crash).*
