from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, sandwich):
    db_sandwich = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )
    db.add(db_sandwich)
    # Commit the changes to the database
    db.commit()
    db.refresh(db_sandwich)
    # Return the newly created Order object
    return db_sandwich


def read_all(db: Session):
    return db.query(models.Sandwich).all()


def read_one(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()


def update(db: Session, sandwich_id, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    if sandwich.sandwich_name:
        db_sandwich.sandwich_name = sandwich.sandwich_name
    if sandwich.price is not None:
        db_sandwich.price = sandwich.price
    # Commit the changes to the database
    db.commit()
    # Return the updated order record
    return db_sandwich.first()


def delete(db: Session, sandwich_id):
    # Query the database for the specific order to delete
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    # Delete the database record without synchronizing the session
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")

    db.delete(db_sandwich)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
