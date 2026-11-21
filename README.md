# Stomiq.AI

**Stomiq.AI** is a mobile health application developed as a Computer Engineering (CTI) graduation project. It is designed to assist doctors and patients in managing stomach CT scan analysis, tumor detection/classification, and treatment progression tracking through a native Android client connected to a Python/FastAPI backend.

---

## Project Roadmap & Status

| Milestone | Scope | Status | Git Tag |
| :--- | :--- | :--- | :--- |
| **Milestone 1** | Client-Server REST architecture, Android Auth UI (Login/Sign Up), role-based navigation (Doctor / Patient), FastAPI backend with Pydantic validation and database persistence | Done | `milestone-1` |
| **Milestone 2** | Password hashing (`bcrypt`) & JWT authentication, configurable server IP & connection test in Settings, CT image upload pipeline, automated backend & unit tests | In Progress | — |
| **Milestone 3** | PyTorch CNN integration for stomach CT DICOM analysis (tumor detection, benign/malignant classification), results visualization & treatment history | Planned | — |

---

## Architecture & Tech Stack

**Architecture in one line:** Android App (Jetpack Compose + Retrofit) $\rightarrow$ REST API (FastAPI + Pydantic) $\rightarrow$ Local Database & AI Inference Pipeline (Python).

* **Mobile Client (`android/`):**
  * **Language & UI:** Kotlin, Jetpack Compose (Material 3), Navigation Compose
  * **Networking:** Retrofit 2, Gson, Kotlin Coroutines
* **Backend (`backend/`):**
  * **Framework:** Python, FastAPI, Uvicorn
  * **Validation & Docs:** Pydantic, automatic OpenAPI / Swagger UI (`/docs`)
  * **Database:** SQLite (local persistence for Milestone 1)
* **Networking:** Direct local network REST communication (designed for large medical image transfers without relying on third-party tunneling services).

---

## Project Layout

```text
Stomiq.AI/
├── android/          # Native Android application (Kotlin, Jetpack Compose, Retrofit)
├── backend/          # FastAPI server, Pydantic schemas, database models
├── .gitignore        # Excludes build artifacts, venv, and local DB files
└── README.md         # Project documentation
