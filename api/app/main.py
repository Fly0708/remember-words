from app.core import config
from app.db.session import engine, SessionLocal
from app.db.base import import_all_models, Base
from app.core import log
from fastapi import FastAPI
from app.routers.words import endpoints as words_endpoints
import_all_models()

Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)

app.include_router(words_endpoints.api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",  # 或者直接传 app 对象
        # host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs= ['app/'],
    )