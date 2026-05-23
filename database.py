from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///estoque.db")

with engine.connect() as conn:

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            quantidade INTEGER
        )
    """))

    conn.commit()

    try:
        conn.execute(text("""
            ALTER TABLE itens
            ADD COLUMN categoria TEXT
        """))

        conn.commit()

    except:
        pass