"""FastAPI application for Sequential Multi-Agent Startup Pitch Deck Generator.

This file creates a FastAPI app using get_fast_api_app() from ADK and fixes
the OpenAPI schema generation issue with httpx.Client fields.
"""

import os
from typing import Any

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
from pydantic.errors import PydanticInvalidForJsonSchema


# Load environment variables from .env file
load_dotenv()

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Get session service URI from environment variables
session_uri = os.getenv("SESSION_SERVICE_URI", None)

# Get Enable Web interface serving flag from environment variables
# Set web=True if you intend to serve a web interface, False otherwise
web_interface_enabled = os.getenv("SERVE_WEB_INTERFACE", "False").lower() in ("true", "1")

# Prepare arguments for get_fast_api_app
app_args = {"agents_dir": AGENT_DIR, "web": web_interface_enabled}

# Only include session_service_uri if it's provided
if session_uri:
    app_args["session_service_uri"] = session_uri

# Create FastAPI app with appropriate arguments
app: FastAPI = get_fast_api_app(**app_args)

app.title = "startup_pitch_deck_generator"
app.description = "A sequential multi-agent system that researches markets, analyzes competition, and creates startup pitch decks"

# Store the original openapi method
_original_openapi = app.openapi


def patched_openapi() -> dict[str, Any]:
    """Patched openapi method that handles httpx.Client errors gracefully."""
    # If schema is already cached, return it
    if app.openapi_schema:
        return app.openapi_schema

    try:
        # Try to generate the schema normally
        return _original_openapi()
    except PydanticInvalidForJsonSchema as e:
        # If the error is about httpx.Client, return a minimal working schema
        if "httpx.Client" in str(e):
            # Generate a minimal schema that allows /docs to work
            # The actual API endpoints will still work, just not fully documented in OpenAPI
            openapi_schema = {
                "openapi": "3.1.0",
                "info": {
                    "title": app.title,
                    "version": getattr(app, "version", "1.0.0"),
                    "description": app.description,
                },
                "paths": {
                    "/docs": {
                        "get": {
                            "summary": "OpenAPI documentation",
                            "responses": {"200": {"description": "Success"}},
                        }
                    },
                    "/redoc": {
                        "get": {
                            "summary": "ReDoc documentation",
                            "responses": {"200": {"description": "Success"}},
                        }
                    },
                    "/openapi.json": {
                        "get": {
                            "summary": "OpenAPI schema",
                            "responses": {"200": {"description": "Success"}},
                        }
                    },
                },
            }
            app.openapi_schema = openapi_schema
            return openapi_schema
        # Re-raise if it's a different error
        raise


# Replace the openapi method with our patched version
app.openapi = patched_openapi


if __name__ == "__main__":
    # Use the PORT environment variable provided by Cloud Run, defaulting to 8080
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

