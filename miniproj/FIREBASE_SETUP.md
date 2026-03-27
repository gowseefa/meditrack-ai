# Firebase Setup Guide for MediTrack

To use Firebase with MediTrack, please follow these steps:

### 1. Create a Firebase Project
1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click **Add Project** and name it `MediTrack`.

### 2. Set up Firestore (Database)
1. In the left sidebar, go to **Build > Firestore Database**.
2. Click **Create Database**.
3. Choose **Start in test mode** for now, select your location, and click **Enable**.

### 3. Set up Storage (File Uploads)
1. Go to **Build > Storage**.
2. Click **Get Started**.
3. Choose **Start in test mode**, select your location, and click **Done**.

### 4. Obtain Service Account Key (CRITICAL)
1. Click the **Gear icon (Project Settings)** next to Project Overview.
2. Go to the **Service accounts** tab.
3. Click **Generate new private key**.
4. A JSON file will be downloaded.
5. **Rename** it to `serviceAccountKey.json`.
6. **Move** this file to the root directory of your project: `c:\Users\Happy\Desktop\miniproj\`.

### 5. Install Dependencies
I will handle the installation of `firebase-admin` via the terminal.

> [!WARNING]
> Do NOT share your `serviceAccountKey.json` with anyone or commit it to a public repository!
