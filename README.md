# Website AI Assistant

Professional repository skeleton for a website-aware AI assistant.

This repository will eventually contain two core systems:

1. `rag/` — accepts the latest website repository as a ZIP file, safely extracts it, scans useful files, creates chunks, generates embeddings, stores them in a vector database, and retrieves relevant knowledge.
2. `ai_assistant/` — contains the LangGraph-based chat agent that uses RAG knowledge to answer visitors and decide when a website navigation action should be returned.

`ui/` will contain the temporary Streamlit chat interface used during local development and testing. Streamlit is not the website itself.

No project implementation is included in this skeleton.
