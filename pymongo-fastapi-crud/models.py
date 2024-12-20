import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    profilepiclink: str = Field(...)
    nome: str = Field(...)
    apelido: str = Field(...)
    pronomes: str = Field(...)
    telefone: str = Field(...)
    email: str = Field(...)
    senha: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "nome": "Don Quixote",
                "apelido": "Miguel de Cervantes",
                "pronomes": "..."
            }
        }

class MovimentacaoFinanceira(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    valor: str = Field(...)
    descricao: str = Field(...)
    centrodecusto: str = Field(...)
    entrada: str = Field(...)
    saida: str = Field(...)
    mes: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "valor": "Don Quixote",
                "descrição": "Miguel de Cervantes",
                "centro de custo": "..."
            }
        }


class CentroDeCustos(BaseModel):
    nome: Optional[str]
    tipo: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "nome": "Don Quixote",
                "tipo": "Miguel de Cervantes",
                "detalhes": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }