# kannadiga.lens

**Problem statement 5 - Kannada Text Digitization.** kannadiga.lens turns Kannada in a photo or scan into large, searchable digital text and adds a compact English gloss for quick understanding.

## What it does

- A colourful, accessible mobile-first dashboard
- A Rubik's-cube inspired intro loader (adapted from the requested MIT-licensed Uiverse component)
- Drag/drop, file picker, or camera capture
- Kannada OCR through a local Tesseract backend (`kan+eng`)
- Search, copy, and download extracted text
- Offline demo mode so the complete product flow can be evaluated without an OCR installation

## Run locally

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and its Kannada language data (`kan.traineddata`) for live OCR.
2. Run `python server.py`.
3. Open `http://localhost:4173`.

The application has no secrets or external API dependencies. When Tesseract is unavailable, the interface remains usable in Demo mode; use **Try a sample** to evaluate the end-to-end reading, searching, copying, and downloading experience.

## Architecture

`Browser (camera/upload) -> Python API -> Tesseract kan+eng -> normalized Kannada text -> accessible reader dashboard`

## Tech stack

Vanilla HTML/CSS/JavaScript, Python standard-library HTTP server, and optional Tesseract OCR.
