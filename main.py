# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:14:31 2022

Framework FastAPI.

@author: cflorelu
"""

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#Ejecución :
    
    # uvicorn main:app --reload

#Documentación Interactiva :

    # FastAPI <- SwaggerUI (Muestra en HTML API documentada) <- OpenAPI
    # http://127.0.0.1:8000/docs
