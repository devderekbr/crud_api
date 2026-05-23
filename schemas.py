from pydantic import BaseModel, Field


class Item(BaseModel):
    nome: str = Field(
        min_length=2,
        max_length=100
    )

    categoria: str = Field(
        min_length=2,
        max_length=50
    )

    quantidade: int = Field(
        ge=0
    )