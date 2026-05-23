from sqlalchemy import text
from database import engine
from schemas import Item


def listar_itens(nome=None):
    with engine.connect() as conn:

        query = "SELECT * FROM itens"
        parametros = {}

        if nome:
            query += " WHERE nome LIKE :nome"
            parametros["nome"] = f"%{nome}%"

        resultado = conn.execute(text(query), parametros)

        return [
            {
                "id": item.id,
                "nome": item.nome,
                "categoria": item.categoria,
                "quantidade": item.quantidade
            }
            for item in resultado
        ]


def criar_item(item: Item):
    with engine.connect() as conn:

        conn.execute(
            text("""
                INSERT INTO itens (nome, categoria, quantidade)
                VALUES (:nome, :categoria, :quantidade)
            """),
            {
                "nome": item.nome,
                "categoria": item.categoria,
                "quantidade": item.quantidade
            }
        )

        conn.commit()

    return {"mensagem": "Item criado"}


def atualizar_item(item_id: int, item_atualizado: Item):
    with engine.connect() as conn:

        resultado = conn.execute(
            text("""
                UPDATE itens
                SET nome = :nome,
                    categoria = :categoria,
                    quantidade = :quantidade
                WHERE id = :id
            """),
            {
                "id": item_id,
                "nome": item_atualizado.nome,
                "categoria": item_atualizado.categoria,
                "quantidade": item_atualizado.quantidade
            }
        )

        conn.commit()

        if resultado.rowcount == 0:
            return {"erro": "Item não encontrado"}

        return {"mensagem": "Item atualizado"}


def deletar_item(item_id: int):
    with engine.connect() as conn:

        resultado = conn.execute(
            text("""
                DELETE FROM itens
                WHERE id = :id
            """),
            {"id": item_id}
        )

        conn.commit()

        if resultado.rowcount == 0:
            return {"erro": "Item não encontrado"}

        return {"mensagem": "Item removido"}


def buscar_item_por_id(item_id):
    with engine.connect() as conn:

        resultado = conn.execute(
            text("""
                SELECT * FROM itens
                WHERE id = :id
            """),
            {"id": item_id}
        )

        item = resultado.fetchone()

        if item is None:
            return {"erro": "Item não encontrado"}

        return {
            "id": item.id,
            "nome": item.nome,
            "categoria": item.categoria,
            "quantidade": item.quantidade
        }