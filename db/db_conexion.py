from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

#Creando Motor y Conexion con la Base de Datos
# TODO: Con la ayuda de pgAdmin debes crear una base de datos
# y la BD debes crearle un esquema
# TODO: Debes cambiar con tu usuario y contraseña de PostgreSQL
# además del host, puerto y nombre de la base de datos que hayas definido
import os


DATABASE_URL = os.environ['DATABASE_URL']


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/MISION_TIC"
engine = create_engine(DATABASE_URL)

#Creacion de un creador la Sesion
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# En obtener_sesion inyectamos la dependencia SessionLocal
def obtener_sesion():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creando Base para la creacion de los modelos
Base = declarative_base()

# TODO: Reemplazar el nombre del esquema creado 
# en la base de datos
Base.metadata.schema = "gestionatec"