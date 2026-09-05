# 🎓 Assignment Sorter & AI Study Assistant

A full-stack, AI-powered academic platform for college assignments, syllabus analysis, previous-year question (PYQ) discovery, notebook OCR, assignment generation, grading, note making, quizzes, and RAG contextual chat.

---

## 🚀 Opening in VS Code

1. Launch **Visual Studio Code**.
2. Go to **File → Open Folder...** (or press `Ctrl + K, Ctrl + O`).
3. Select the folder: `C:\Users\dell\Assignment Sorter`

---

## 🐞 Debugging in VS Code

Pre-configured launch configurations are included in `.vscode/launch.json`:

1. Open the **Run & Debug** panel on the left sidebar (`Ctrl + Shift + D`).
2. Select a configuration from the dropdown at the top:
   - **🚀 Debug FastAPI Server (Assignment Sorter)**: Launches the full server with breakpoints and hot-reload enabled.
   - **🧪 Run & Debug E2E Test Suite**: Steps through the unit and integration tests.
   - **⚙️ Debug C Core Compilation & Bridge**: Runs and inspects the C shared library compiler.
3. Press **`F5`** to start debugging.

---

## 🛠️ VS Code Tasks

Press `Ctrl + Shift + P` → `Tasks: Run Task` to run:
- **Build C Core Library (GCC)** (`Ctrl + Shift + B`)
- **Run E2E Test Suite**
- **Start Server (Uvicorn)**

---

## 🌐 Running from Terminal

```bash
# Start the web server
python run.py

# Or double-click
start_app.bat
```

Open **`http://127.0.0.1:8000`** in your browser.
