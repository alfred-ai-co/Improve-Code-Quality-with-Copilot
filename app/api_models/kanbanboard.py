from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class KanbanBoardBase(BaseModel):
    name: str
    description: Optional[str] = None


class KanbanBoardCreate(KanbanBoardBase):
    pass


class KanbanBoardUpdate(KanbanBoardBase):
    pass


class KanbanBoardInDB(KanbanBoardBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True


class KanbanStatusBase(BaseModel):
    name: str
    description: Optional[str] = None
    board_id: int


class KanbanStatusCreate(KanbanStatusBase):
    pass


class KanbanStatusUpdate(KanbanStatusBase):
    pass


class KanbanStatusInDB(KanbanStatusBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True