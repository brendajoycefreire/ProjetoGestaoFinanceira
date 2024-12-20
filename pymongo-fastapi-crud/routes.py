from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Usuario, MovimentacaoFinanceira, CentroDeCustos

router = APIRouter()

@router.post("/", response_description="Create a new usuario", status_code=status.HTTP_201_CREATED, response_model=Usuario)
def create_usuario(request: Request, usuario: Usuario = Body(...)):
    usuario = jsonable_encoder(usuario)
    new_usuario = request.app.database["usuarios"].insert_one(usuario)
    created_usuario = request.app.database["usuarios"].find_one(
        {"_id": new_usuario.inserted_id}
    )

    return created_usuario

@router.get("/", response_description="List all usuarios", response_model=List[Usuario])
def list_usuarios(request: Request):
    usuarios = list(request.app.database["usuarios"].find(limit=100))
    return usuarios

@router.get("/{id}", response_description="Get a single usuario by id", response_model=Usuario)
def find_usuario(id: str, request: Request):
    if (usuario := request.app.database["usuarios"].find_one({"_id": id})) is not None:
        return usuario
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario with ID {id} not found")

@router.put("/{id}", response_description="Update a usuario", response_model=Usuario)
def update_usuario(id: str, request: Request, usuario: UsuarioUpdate = Body(...)):
    usuario = {k: v for k, v in usuario.dict().items() if v is not None}
    if len(usuario) >= 1:
        update_result = request.app.database["usuarios"].update_one(
            {"_id": id}, {"$set": usuario}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario with ID {id} not found")

    if (
        existing_usuario := request.app.database["usuarios"].find_one({"_id": id})
    ) is not None:
        return existing_usuario

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario with ID {id} not found")

@router.delete("/{id}", response_description="Delete a usuario")
def delete_usuario(id: str, request: Request, response: Response):
    delete_result = request.app.database["usuarios"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario with ID {id} not found")

