from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
import os

app = FastAPI(title="Test Deploy API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    """Health check — returns server info."""
    return {
        "status": "ok",
        "service": "test-deploy-api",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "env": os.getenv("RAILWAY_ENVIRONMENT", "unknown"),
    }


@app.get("/")
async def root():
    """Root — redirect to docs or return simple message."""
    return {
        "message": "Test Deploy API is running!",
        "docs": "/docs",
    }
