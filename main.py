from fastapi import FastAPI
from schemas import Item

from crud import (
    listar_itens,
    criar_item,
    atualizar_item,
    deletar_item,
    buscar_item_por_id
)

app = FastAPI()


#itens = []
contador_id = 1


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}


@app.get("/itens")
def get_itens(nome: str = None):
    return listar_itens(nome)


@app.post("/itens")
def post_item(item: Item):
    return criar_item(item)


@app.put("/itens/{item_id}")
def put_item(item_id: int, item: Item):
    return atualizar_item(item_id, item)


@app.delete("/itens/{item_id}")
def delete_item(item_id: int):
    return deletar_item(item_id)


@app.get("/itens/{item_id}")
def get_item(item_id: int):
    return buscar_item_por_id(item_id)

