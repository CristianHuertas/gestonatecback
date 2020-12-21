from pydantic import BaseModel

class Cliente(BaseModel):
    documento: int
    tipo_documento: str
    razon_social: str
    contacto: str
    telefono: int
    direccion: str
    ciudad: str
    correo: str
    detalle: str

    class Config:
        orm_mode = True
