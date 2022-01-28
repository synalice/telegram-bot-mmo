# import asyncio
#
# import sqlalchemy as sa
# import sqlalchemy.ext.asyncio as sa_async
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# from app.config import (
#     DB_NAME,
#     DB_DRIVER,
#     DB_LOGIN,
#     DB_PASSWORD,
#     DB_HOST,
#     DB_PORT,
#     DB_DATABASE,
# )
#
#
# Base = declarative_base()
#
#
# async def async_main():
#     engine = sa_async.create_async_engine(
#         f"{DB_NAME}{DB_DRIVER}://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
#         echo=False,
#     )
#
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#
#     class TelegramUserProfile(Base):
#         __tablename__ = "telegram_user_profile"
#         telegram_id = sa.Column(sa.Integer, primary_key=True)
#         telegram_firstname = sa.Column(sa.String, nullable=False)
#         telegram_lastname = sa.Column(sa.String)
#         sa.Index(telegram_id, unique=True)
#
#
#     async def register_new_user(user_id, first_name, last_name):
#         async_session = sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)
#
#         async with async_session() as session:
#             async with session.begin():
#                 querry_user = (
#                     sa.select(TelegramUserProfile)
#                     .where(TelegramUserProfile.telegram_id == user_id)
#                     .one()
#                 )
#                 user = await session.execute(querry_user)
#                 await session.commit()
#         if not user:
#             user = TelegramUserProfile(
#                 telegram_id=user_id,
#                 telegram_firstname=first_name,
#                 telegram_lastname=last_name,
#             )
#         return user
#
# asyncio.run(async_main())
# # TODO: This is bad and I don't know how to fix it. This code shouldn't be all in one file.
