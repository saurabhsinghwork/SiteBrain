FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir .

COPY . .

EXPOSE 8501

# The Streamlit startup command will be added when implementation begins.
CMD ["sh", "-c", "echo 'Repository skeleton only: application code has not been implemented yet.'"]
