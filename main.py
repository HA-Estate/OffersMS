from pathlib import Path

import uvicorn
from fastapi import FastAPI
from ms_core import setup_app

application = FastAPI()

setup_app(
    application,
    "asyncpg://postgres:postgres@localhost:5432/ha_offers",
    Path("app") / "routers",
    ["app.models"],  # module path to a file containing models
)

if __name__ == "__main__":
    uvicorn.run("main:application", port=8000, reload=True)
