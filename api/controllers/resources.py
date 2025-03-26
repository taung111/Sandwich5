from sqlalchemy.orm import Session
from ..models import models, schemas
from fastapi import HTTPException, status, Response, Depends

def create(db: Session, resource):
    db_resource = models.Resource(
        item=resource.item,
        amount=resource.amount)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    if resource.item:
        db_resource.item = resource.item
    if resource.amount:
        db_resource.amount = resource.amount
    db.commit()
    return db_resource

def delete(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return {"message": "Resource deleted successfully"}
