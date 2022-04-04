from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.database.events import close_database_connection
from app.database.events import open_database_connection


def start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        logger.info("Starting application...")
        await open_database_connection(app)
        logger.info("Started application.")
    return start_app


def stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        logger.info("Stopping application...")
        await close_database_connection(app)
        logger.info("Stopped application.")
    return stop_app
