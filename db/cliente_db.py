from typing import  Dict
from pydantic import BaseModel


from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from db.db_conexion import Base, engine


class ClienteInDB(Base):
    __tablename__ = "clientes"

    documento= Column(Integer, primary_key=True)
    tipo_documento= Column(String)
    razon_social= Column(String)
    contacto= Column(String)
    telefono= Column(Integer)
    direccion= Column(String)
    ciudad= Column(String)
    correo= Column(String)
    detalle= Column(String)


Base.metadata.create_all(bind=engine)


""" class ClienteInDB(BaseModel):
    documento: int
    tipo_documento: str
    razon_social: str
    contacto: str
    telefono: int
    direccion: str
    ciudad: str
    correo: str
    detalle: str

database_clientes: Dict[str, ClienteInDB]

database_clientes={
    "800433422": ClienteInDB(**{"documento": 800433422,
                                "tipo_documento": "NIT",
                                "razon_social": "ÉXITO MEDELLIN",
                                "contacto": "SANTIAGO MARTINEZ",
                                "telefono": 3169161138,
                                "direccion": "Calle 10 No. 9 - 78 ",
                                "ciudad": "BOGOTA",
                                "correo": "SANTIAGOMARTINEZ@GMAIL.COM",
                                "detalle": ""}),
    "199823874": ClienteInDB(**{"documento": 199823874,
                                "tipo_documento": "CC",
                                "razon_social": "CARLOS SANCHEZ",
                                "contacto": "CARLOS SANCHEZ",
                                "telefono": 3054442279,
                                "direccion": "Carrera 56A No. 51 - 81",
                                "ciudad": "BOGOTA",
                                "correo": "CARLOSSANCHEZ@GMAIL.COM",
                                "detalle": ""}),
    "119457089": ClienteInDB(**{"documento": 119457089,
                                "tipo_documento": "CC",
                                "razon_social": "ANDREA VAQUERO",
                                "contacto": "ANDREA VAQUERO",
                                "telefono": 3167565600,
                                "direccion": "Carrera 22 No. 17-31",
                                "ciudad": "BOGOTA",
                                "correo": "ANDREAVAQUERO@GMAIL.COM",
                                "detalle": ""}),                        
    "147256716": ClienteInDB(**{"documento": 147256716,
                                "tipo_documento": "CC",
                                "razon_social": "LUIS PINTO",
                                "contacto": "LUIS PINTO",
                                "telefono": 3095530053,
                                "direccion": "Carrera 54 No. 68 - 80",
                                "ciudad": "BOGOTA",
                                "correo": "LUISPINTO@GMAIL.COM",
                                "detalle": ""}),     
    "166062874": ClienteInDB(**{"documento": 166062874,
                                "tipo_documento": "CC",
                                "razon_social": "ANDRES PEREZ",
                                "contacto": "ANDRES PEREZ",
                                "telefono": 3193939789,
                                "direccion": "Calle 59 No. 27 - 35",
                                "ciudad": "BOGOTA",
                                "correo": "ANDRESPEREZ@GMAIL.COM",
                                "detalle": ""}),            
    "900487546": ClienteInDB(**{"documento": 900487546,
                                "tipo_documento": "NIT",
                                "razon_social": "RAPPI",
                                "contacto": "JOSE HURTADO",
                                "telefono": 3031611503,
                                "direccion": "Carrera 8 No. 20 - 59",
                                "ciudad": "BOGOTA",
                                "correo": "JOSEHURTADO@GMAIL.COM",
                                "detalle": ""}),       
    "151165796": ClienteInDB(**{"documento": 151165796,
                                "tipo_documento": "CC",
                                "razon_social": "PAOLA RAMIREZ",
                                "contacto": "PAOLA RAMIREZ",
                                "telefono": 3124049958,
                                "direccion": "Carrera 85 No. 103 - 59",
                                "ciudad": "BOGOTA",
                                "correo": "PAOLARAMIREZ@GMAIL.COM",
                                "detalle": ""}),

}

def get_cliente(documento: str):
    if documento in database_clientes.keys():
        return database_clientes[documento]
    else:
        return None

def update_cliente(cliente_in_db: ClienteInDB):
    if str(cliente_in_db.documento) in database_clientes.keys():
        database_clientes[str(cliente_in_db.documento)] = cliente_in_db
        return cliente_in_db
    else:
        return None

def delete_cliente(documento: str):
    if str(documento) in database_clientes.keys():
        del database_clientes[documento]
        return documento
    else:
        return None    

def save_cliente(cliente_in_db: ClienteInDB):
    database_clientes[str(cliente_in_db.documento)] = cliente_in_db
    return cliente_in_db  

def get_all_clientes():
    return database_clientes
 """
