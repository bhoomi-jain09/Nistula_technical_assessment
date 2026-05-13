from fastapi import FastAPI
from sqlalchemy import text

from app.api.webhook import router
from app.database import SessionLocal

app = FastAPI(
    title="Nistula AI Backend"
)
app.include_router(router)
@app.get("/")
def home():

    db = SessionLocal()

    try:
        result = db.execute(
            text("SELECT * FROM guests")
        )

        guests = result.fetchall()

        return {
            "message": "Database connected successfully",
            "guests": [dict(row._mapping) for row in guests]
        }

    except Exception as e:
        return {
            "error": str(e)
        }

    finally:
        db.close()