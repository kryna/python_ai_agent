# Python AI Agent

A Python-based AI agent built with modern LLM tooling to explore autonomous workflows, structured outputs, function calling, and external integrations.

The project serves as a playground for experimenting with AI agents while following clean software engineering practices and Python development standards.

---

## Features

* 🤖 AI agent powered by modern Large Language Models
* 💬 Interactive command-line interface
* 🔧 Extensible tool architecture
* 📄 Structured output support
* 🌐 External API integrations
* 🐍 Modern Python project structure
* 🧪 Easy to extend for new capabilities

---

## Tech Stack

* Python 3.12+
* OpenAI API
* Virtual environments (`venv`)
* Modern Python packaging
* Type hints

---

## Project Structure

```text
python_ai_agent/
├── app/
│   ├── agent.py
│   ├── tools/
│   ├── prompts/
│   └── ...
├── tests/
├── .env.example
├── requirements.txt
├── pyproject.toml
└── README.md
```

> The exact structure may evolve as new features are added.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kryna/python_ai_agent.git
cd python_ai_agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Additional environment variables may be required depending on the integrations enabled.

---

## Running the Project

Run the application:

```bash
python main.py
```

or

```bash
python -m app
```

(depending on the current project structure)

---

## Development

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

Format the code:

```bash
black .
```

Lint:

```bash
ruff check .
```

---

## Roadmap

* [ ] Conversation memory
* [ ] Function/tool calling
* [ ] Multi-agent support
* [ ] RAG integration
* [ ] Web search
* [ ] Streaming responses
* [ ] Docker support
* [ ] REST API
* [ ] FastAPI interface
* [ ] Unit and integration tests

---

## Learning Goals

This repository is intended as a learning project focused on:

* AI agent architecture
* Python best practices
* Prompt engineering
* Tool integration
* API communication
* Clean project organization
* Experimenting with modern LLM capabilities

---

## Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Krzysztof Krynicki**

GitHub: https://github.com/kryna
