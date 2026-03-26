# Phase 5 Research: Testing & Dockerization

## Decisions Made

1. **Testing Framework**: `pytest`. It's lightweight, standard, and perfectly suited for fast Flask test clients.
2. **Containerization Strategy**: Two separate containers orchestrated with `docker-compose`.
   - `backend`: Flask running on port 5000.
   - `frontend`: Streamlit running on port 8501.
   The frontend will communicate with the backend over the internal Docker network using the service name (e.g., `http://backend:5000`). To facilitate this, `ui/app.py` must resolve its `API_BASE` dynamically via an environment variable.
