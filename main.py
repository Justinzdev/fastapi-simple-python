from fastapi import FastAPI

# Routes
from v1.routes import user_routes

app = FastAPI()

app.include_router(user_routes.router, prefix='/api/v1')