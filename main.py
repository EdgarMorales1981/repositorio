import psycopg2
import uuid
import cloudinary
import cloudinary.uploader
import uvicorn
from fastapi import FastAPI, status, UploadFile, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

class Servicio(BaseModel):
    id: str = None
    nombre: str
    descripcion: str
    foto: str
    precio: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudinary.config(
     cloud_name="ejmorales",
     api_key="485664484772281",
     api_secret="zTuUNkCS6RX3kmizDQCIpo3Qf3c"
 )


@app.get("/verfoto")
def read_root():
    conn = psycopg2.connect(
        database="vfvxprgv",
        user='vfvxprgv',
        password='u1Ququtd0f-27eKTgXwzlrHTpwaYqVUE',
        host="mahmud.db.elephantsql.com"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM contenedor ORDER BY id DESC")
    rows = cur.fetchall()

    formatted_datos = []
    for row in rows:
        formatted_datos.append(
            Servicio(id=row[0], nombre=row[1], descripcion=row[2],foto=row[3],precio=row[4])
        )

    cur.close()
    conn.close()
    return formatted_datos