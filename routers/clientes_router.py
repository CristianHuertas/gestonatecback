from typing import List
from typing import  Dict
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_conexion import obtener_sesion
from db import cliente_db
from db.cliente_db import ClienteInDB
from models.cliente_model import Cliente

router = APIRouter()

@router.get("/pruebas")#agregar nuevo cliente
async def get_clientes(sesion: Session = Depends(obtener_sesion)):
    nuevo_cliente= ClienteInDB( documento= 804002437, tipo_documento= "cc", razon_social= "descont", contacto= "yo", telefono= 2312344, direccion= "cll bga", ciudad= "bga", correo= "as@asd", detalle= " ")
    sesion.add(nuevo_cliente)
    sesion.commit()
    nuevo_cliente= sesion.query(ClienteInDB).get(nuevo_cliente.documento)
    return nuevo_cliente

@router.get("/cliente/registroGetAll") #mostrar todos los clientes
async def get_clientes(sesion: Session = Depends(obtener_sesion)):
    todos_clientes= sesion.query(ClienteInDB).all()
    return todos_clientes    

    

@router.get("/cliente/registroGet") #consultar un solo cliente por documento
async def get_cliente (documento: int, sesion: Session = Depends(obtener_sesion)):
    este_cliente= sesion.query(ClienteInDB).get(documento)

    if este_cliente==None:
        raise HTTPException(status_code=404, detail=" El cliente no existe ")
    
    return este_cliente 

#revisar por que no lo veo claro
@router.get("/cliente/registroGet/{documento}") #consultar un solo cliente por documento cuando viene de la url
async def get_cliente(documento:int, sesion: Session = Depends(obtener_sesion)):
    este_cliente= sesion.query(ClienteInDB).get(documento)
    if este_cliente==None:
        raise HTTPException(status_code=404, detail=" El cliente no existe ")
    return este_cliente    


@router.get("/")
async def root():
    return {"message":"Gestionatec"} 

""" ///////////////////////////// """
@router.put("/cliente/registroPut") #cambiar datos de un cliente
async def update_cliente(cliente: Cliente, sesion: Session = Depends(obtener_sesion)):
    cliente_in_db=sesion.query(ClienteInDB).get(cliente.documento)

    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail=" El cliente no existe ")
    
    cliente_in_db.tipo_documento= cliente.tipo_documento
    cliente_in_db.razon_social= cliente.razon_social
    cliente_in_db.contacto= cliente.contacto
    cliente_in_db.telefono= cliente.telefono
    cliente_in_db.direccion= cliente.direccion
    cliente_in_db.ciudad= cliente.ciudad
    cliente_in_db.correo= cliente.correo
    cliente_in_db.detalle= cliente.detalle

    # Vamos a actualizar en la db
    sesion.commit()

    # Actualiza la sesión que tenemos creada
    sesion.refresh(cliente_in_db)
    
    return  cliente_in_db

@router.post("/cliente/registroSave")#crear un nuevo cliente
async def save_cliente(cliente: Cliente, sesion: Session = Depends(obtener_sesion)):
    busca_cliente= sesion.query(ClienteInDB).get(cliente.documento)
    if busca_cliente != None:
        raise HTTPException(status_code=404,
                            detail=" El cliente ya existe ")
    cliente_nuevo = ClienteInDB(**cliente.dict())   
    sesion.add(cliente_nuevo)
    sesion.commit()
    sesion.refresh(cliente_nuevo)

    return cliente_nuevo 


@router.delete("/cliente/registroDel/{documento}") # Elimina un cliente por documento
def delete_cliente(documento:int, sesion: Session = Depends(obtener_sesion)):
    cliente_eliminado= sesion.query(ClienteInDB).get(documento)

    if cliente_eliminado==None:
        raise HTTPException(status_code=404, detail=" El cliente no existe ")

    sesion.delete(cliente_eliminado)
    sesion.commit()
    

    return documento

