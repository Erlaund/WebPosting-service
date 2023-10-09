from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

publications = Table(
    "publications",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String),
    Column("user_id", Integer, ForeignKey("users.id")),
    # добавить поля публикации и прикладываемых документов, фото и видео
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
)
