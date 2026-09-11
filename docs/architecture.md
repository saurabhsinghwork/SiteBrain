# Planned Architecture

## RAG side

Latest website repo ZIP -> safe extraction -> file scan -> chunking -> embeddings -> local vector store -> retrieval

## AI assistant side

Visitor query -> LangGraph -> retrieve relevant RAG knowledge -> prepare answer -> optional navigation action -> fallback if uncertain

## UI during development

Streamlit is only the chat interface. The actual website repository will be run locally for integration and navigation testing.

## Future commercial integration

The website frontend will eventually consume the assistant's response and navigation action directly. The RAG and AI assistant layers should remain reusable when Streamlit is removed.
