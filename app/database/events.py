import os

import asyncpg
from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger

load_dotenv()


async def open_database_connection(app: FastAPI) -> None:
    logger.info("Connecting to database...")
    app.state.pool = await asyncpg.create_pool(str(os.getenv("DATABASE_URL")))
    logger.info("Connected to database.")


async def close_database_connection(app: FastAPI) -> None:
    logger.info("Closing database connection...")
    await app.state.pool.close()
    logger.info("Closed database connection.")
