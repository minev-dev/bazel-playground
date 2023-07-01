from typing import Union
import sys

import uvicorn
from fastapi import FastAPI

from src.calculator.calculator import Calculator

app = FastAPI()


@app.get("/")
def read_root():
    print(Calculator().add(1, 2))

    return {"Hello": "World"}


if __name__ == "__main__":
    sys.exit(uvicorn.run(app, port=8000, host="0.0.0.0"))
