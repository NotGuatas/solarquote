"""
Registro central de modelos.

IMPORTANTE: todo modelo nuevo debe importarse aquí.
Alembic solo detecta las tablas de los modelos que estén en este archivo.
"""

from app.models.cotizacion import Cotizacion, EstadoCotizacion, ItemCotizacion
from app.models.material import Material, PrecioMaterial
from app.models.usuario import RolUsuario, Usuario

__all__ = [
    "Usuario",
    "RolUsuario",
    "Cotizacion",
    "ItemCotizacion",
    "EstadoCotizacion",
    "Material",
    "PrecioMaterial",
]
