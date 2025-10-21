from fastapi import APIRouter
from app.db.session import SessionLocal
from app.db.models.words import Words
from loguru import logger

api_router = APIRouter(prefix="/words")

@api_router.get("/hello")
async def hello_world():
    return {"message": "Hello, world!"}


from .schema import WordCreate
@api_router.post("/create")
def create_word(word: WordCreate):
    logger.info(f"create new word: {word}")
    with SessionLocal() as db:
        words_entity = Words(word=word.word)
        db.add(words_entity)
        db.commit()
        return {"id": words_entity.id}
