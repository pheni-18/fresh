from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from src.presentation.controllers import router
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()

origins = [
    'http://localhost:3000',
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(router)


def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema

    openapi_schema = get_openapi(
        title='Fresh API',
        version='1.0.0',
        description='This is a practice of ddd and onion arch.',
        routes=api.routes,
    )
    openapi_schema['info']['x-logo'] = {
        'url': 'https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png',
    }
    api.openapi_schema = openapi_schema
    return api.openapi_schema


api.openapi = custom_openapi
