# 🤖 Gemini Agent

A lightweight agentic AI assistant powered by **Google Gemini** that can read files, write files, and execute Python code autonomously — all from a simple conversational interface.

---

## ✨ Features

- 📖 **File Reading** — Load and parse text-based files to use as context
- ✍️ **File Writing** — Generate and save files based on instructions
- 🐍 **Python Code Execution** — Write and run Python code dynamically, with results fed back into the agent loop
- 🔄 **Agentic Loop** — The agent reasons step-by-step, deciding which tool to use at each turn until the task is complete

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- A Google Gemini API key ([get one here](https://aistudio.google.com/app/apikey))

### Installation

```bash
git clone  https://github.com/StefanoFaiola/gemini_agent.git
cd gemini_agent
uv run main.py
```

### Configuration

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the Agent

```bash
uv run main.py
```

---

## 🛠️ Tools Available

| Tool | Description |
|------|-------------|
| `get_file_content` | Reads the contents of a file from the local filesystem |
| `write_file` | Creates or overwrites a file with the given content |
| `run_python_file` | Executes a Python code snippet and returns stdout/stderr |
| `get_file_info` | Get files info from a specified directory |

---

## 💡 Example Usage

```
You: Read the file data.csv and plot a bar chart of the top 5 values, then save it as chart.png

Agent: [read_file] Reading data.csv...
Agent: [run_python] Generating chart with matplotlib...
Agent: [write_file] Saving chart.png...
Agent: Done! The bar chart has been saved to chart.png.
```

---

## 🗂️ Project Structure
```
GEMINI_AGENT/
├── agent/                     # Core agent logic
├── calculator/                # Example use case
├── functions/                 # Tool implementations
│   ├── get_file_content.py    # Read a file's content
│   ├── get_files_info.py      # List and inspect files
│   ├── run_python_file.py     # Execute Python files
│   └── write_file.py          # Write content to a file
├── main.py                    # Entry point and agent loop
├── config.py                  # Configuration and settings
├── sandbox.py                 # Sandboxed execution environment
├── test_get_file_content.py   # Tests for file reading
├── test_get_files_info.py     # Tests for file info
├── test_run_python_file.py    # Tests for Python execution
├── test_write_file.py         # Tests for file writing
├── pyproject.toml             # Project metadata & dependencies
├── .env                       # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

```

---

## 📦 Dependencies

- [`google-generativeai`](https://pypi.org/project/google-generativeai/) — Gemini API client
- `python-dotenv` — Environment variable management

---

## ⚠️ Disclaimer

This agent can execute arbitrary Python code on your machine. Run it in a sandboxed or controlled environment if you plan to use it with untrusted inputs.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
