from sqlalchemy.orm import DeclarativeBase
import pkgutil
import importlib
import app.db.models

class Base(DeclarativeBase):
    pass

def import_all_models():
    package = app.db.models
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package.__name__}.{module_name}")
