from services.database import Base, engine
import models  # IMPORTANT: this loads all tables

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("✅ Database tables created successfully")
