import sqlalchemy.ext.asyncio as sa_async

from app.config import (
    DB_NAME,
    DB_DRIVER,
    DB_LOGIN,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
)


engine = sa_async.create_async_engine(
    f"{DB_NAME}{DB_DRIVER}://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
    echo=False,
)

# with engine.begin() as conn:
#     conn.run_sync(Base.metadata.drop_all)
#     conn.run_sync(Base.metadata.create_all)
# ?????????
