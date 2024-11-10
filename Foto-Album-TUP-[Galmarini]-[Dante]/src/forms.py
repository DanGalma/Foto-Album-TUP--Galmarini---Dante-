from typing import Optional
from pydantic import BaseModel


class PhotoCreateForm(BaseModel):
    title: str
    description: Optional[str] = None
    image: str
    
#VALIDA QUE SUS DATOS SEAN CORRECTOS
