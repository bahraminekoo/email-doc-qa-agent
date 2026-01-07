# 📧 Document Q&A Agent

Upload PDFs or text files and query them conversationally using RAG.

## Project Structure
- `src/` → core implementation
- `tests/` → unit tests
- Root → configs, requirements, README

## Tech Stack
- LangChain
- Hugging Face models
- ChromaDB
- Streamlit (optional UI)

## Quickstart
```bash
pip install -r requirements.txt
cp .env.example .env
python -m src.agent
pytest tests/
