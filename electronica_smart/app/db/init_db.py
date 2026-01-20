from app.db.session import engine
from app.db.base import Base

# Mostrar la URL de conexión para depuración
print(f"🚨 DATABASE_URL Cargada: {engine.url}")

def init_db():
    print("🛠️ Creando las tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente.")

if __name__ == "__main__":
    init_db()
