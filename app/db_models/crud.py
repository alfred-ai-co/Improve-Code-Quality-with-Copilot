from sqlalchemy.orm import Session
from app.db_models.base import *


# CRUD operations for Project
def create_project(db: Session, name: str, description: str):
    new_project = Project(name=name, description=description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id: int, name: str, description: str):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        project.name = name
        project.description = description
        db.commit()
        db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()


# CRUD operations for Ticket
def create_ticket(db: Session, project_id: int, title: str, description: str, status: str, priority: str):
    new_ticket = Ticket(project_id=project_id, title=title, description=description, status=status, priority=priority)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, title: str, description: str, status: str, priority: str):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        ticket.title = title
        ticket.description = description
        ticket.status = status
        ticket.priority = priority
        db.commit()
        db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        db.delete(ticket)
        db.commit()


# CRUD Operations for Kanban Boards
def create_board(db: Session, name: str, description: str):
    new_board = KanbanBoard(name=name, description=description)
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board

def get_board(db: Session, board_id: int):
    return db.query(KanbanBoard).filter(KanbanBoard.id == board_id).first()

def update_board(db: Session, board_id: int, name: str, description: str):
    board = db.query(KanbanBoard).filter(KanbanBoard.id == board_id).first()
    if board:
        board.name = name
        board.description = description
        db.commit()
        db.refresh(board)
    return board

def delete_board(db: Session, board_id: int):
    board = db.query(KanbanBoard).filter(KanbanBoard.id == board_id).first()
    if board:
        db.delete(board)
        db.commit()


# CRUD Operations for Kanban Statuses
def create_status(db: Session, name: str, description: str, board_id: int):
    new_status = KanbanStatus(name=name, description=description, board_id=board_id)
    db.add(new_status)
    db.commit()
    db.refresh(new_status)
    return new_status

def get_status(db: Session, status_id: int):
    return db.query(KanbanStatus).filter(KanbanStatus.id == status_id).first()

def update_status(db: Session, status_id: int, name: str, description: str, board_id: int):
    status = db.query(KanbanStatus).filter(KanbanStatus.id == status_id).first()
    if status:
        status.name = name
        status.description = description
        status.board_id = board_id
        db.commit()
        db.refresh(status)
    return status

def delete_status(db: Session, status_id: int):
    status = db.query(KanbanStatus).filter(KanbanStatus.id == status_id).first()
    if status:
        db.delete(status)
        db.commit()


# CRUD Operations for Kanban Tickets
def create_ticket(db: Session, name: str, description: str, status: str, priority: str, board_id: int):
    new_ticket = Ticket(name=name, description=description, status=status, priority=priority, board_id=board_id)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, name: str, description: str, status: str, priority: str, board_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        ticket.name = name
        ticket.description = description
        ticket.status = status
        ticket.priority = priority
        ticket.board_id = board_id
        db.commit()
        db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        db.delete(ticket)
        db.commit()

