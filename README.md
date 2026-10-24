<div align="center">

# kannadiga.lens (ಕನ್ನಡಿಗ.lens)

![Python](https://img.shields.io/badge/PYTHON-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Domain](https://img.shields.io/badge/DOMAIN-DOCUMENT%20AI%20%26%20OCR-red?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/TECH%20STACK-HTML5%20%7C%20CSS3%20%7C%20JS%20%7C%20PYTHON-orange?style=for-the-badge)
![OCR Engine](https://img.shields.io/badge/ENGINE-TESSERACT%20(KAN%2BENG)-purple?style=for-the-badge)
![Challenge](https://img.shields.io/badge/CHALLENGE-PS--05%20KANNADA%20DIGITIZATION-blue?style=for-the-badge)
![License](https://img.shields.io/badge/LICENSE-MIT-007EC6?style=for-the-badge)

<br/>

### **A lightweight, mobile-first document digitization platform converting printed/scanned Kannada media into searchable digital text with contextual English gloss.**

<br/>
---

### 🌐 ಲೈವ್ ಅಪ್ಲಿಕೇಶನ್ | Live Production Deployment

👉 **[https://kannadiga-lens-4.onrender.com/](https://kannadiga-lens-4.onrender.com/)** 👈

*No local installation or environment configuration required. Access directly in any browser on mobile or desktop.*

---

[Overview](#overview) • [Problem Alignment](#problem-statement-alignment) • [Key Features](#key-features) • [System Architecture](#system-architecture) • [Tech Stack](#tech-stack) • [Quick Start](#quick-start) • [Offline Demo Mode](#offline-demo-mode)

</div>

---

## Overview

**kannadiga.lens** addresses the challenge of accessibility and searchability in physical Kannada media. By leveraging a lightweight Python backend paired with a local Tesseract OCR engine, the application extracts Kannada text from uploaded photos, scans, or live camera streams, rendering it into an accessible interface complete with an integrated English gloss.

---

## Problem Statement Alignment

| Challenge Parameter | Project Specification |
| :--- | :--- |
| **Track** | Problem Statement 05 — Kannada Text Digitization |
| **Input Channels** | Drag-and-drop upload, local file picker, live mobile/desktop camera capture |
| **Core Processing** | Local Tesseract OCR pipeline using `kan` + `eng` language packs |
| **Output Deliverables**| High-contrast searchable text, one-click copy, structured text export, and compact English gloss |
| **Execution Model** | Zero external API dependencies, fully operational offline |

---

## Key Features

* **Mobile-First Responsive Dashboard:** Optimized for both handheld devices and desktop views with accessible typography and high-contrast styling.
* **Rubik's Loader:** Custom visual intro loader integrated during document processing phases (adapted from MIT-licensed Uiverse component).
* **Flexible Document Ingestion:** Supports physical document scans, uploaded image files, and direct camera captures.
* **Local Tesseract OCR Processing:** Operates `kan+eng` trained data locally without third-party network API calls or data privacy concerns.
* **Search & Export Utilities:** Integrated real-time query search, clipboard copying, and file downloading for extracted Kannada text.
* **Offline Demo Mode:** Built-in evaluation pipeline allows complete end-to-end UX testing using pre-loaded sample documents when Tesseract binaries are not installed.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Browser Client (Camera / Upload)           │
└────────────────────────────┬────────────────────────────┘
                             │ HTTP Upload (Multipart Form)
                             ▼
┌─────────────────────────────────────────────────────────┐
│               Python API (http.server)                  │
└────────────────────────────┬────────────────────────────┘
                             │ Exec Subprocess (kan+eng)
                             ▼
┌─────────────────────────────────────────────────────────┐
│             Local Tesseract OCR Engine                  │
└────────────────────────────┬────────────────────────────┘
                             │ Normalized Kannada Text Output
                             ▼
┌─────────────────────────────────────────────────────────┐
│     Accessible Reader Dashboard (Text + English Gloss)  │
└────────────────────────────┬────────────────────────────┘
```

---

## Tech Stack

| Layer | Technology | Details |
| :--- | :--- | :--- |
| **Frontend** | HTML5 / CSS3 / JavaScript (ES6+) | Vanilla mobile-first UI with accessible typography & custom Uiverse loader |
| **Backend** | Python Standard Library | Lightweight HTTP server (`http.server`) managing request routes & OCR execution |
| **OCR Engine** | Tesseract OCR | Local execution configured with combined `kan` + `eng` trained datasets |
| **Dependencies**| Zero External API Keys | Runs completely locally on machine hardware |

---


