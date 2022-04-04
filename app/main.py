import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.core.events import start_app_handler
from app.core.events import stop_app_handler

load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if os.getenv("ENVIRONMENT", "local") == "local":
        @app.get("/", include_in_schema=False)
        def redirect_to_swagger() -> RedirectResponse:
            return RedirectResponse("/docs")

    app.add_event_handler("startup", start_app_handler(app))
    app.add_event_handler("shutdown", stop_app_handler(app))

    return app


app = create_app()
