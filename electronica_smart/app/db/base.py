from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Importa los modelos aquí para que se registren, pero hazlo al final
from app.models import smart_device, user  # 👈 Añade esto al final del archivo
