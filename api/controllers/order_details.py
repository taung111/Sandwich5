from sqlalchemy.orm import Session
from ..models import models

def create(db: Session, order_detail):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail_id, order_detail):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

    if db_order_detail:
        if order_detail.amount is not None:
            db_order_detail.amount = order_detail.amount
        if order_detail.sandwich_id is not None:
            db_order_detail.sandwich_id = order_detail.sandwich_id
        if order_detail.order_id is not None:
            db_order_detail.order_id = order_detail.order_id

        db.commit()
        db.refresh(db_order_detail)
        return db_order_detail
    return None

def delete(db: Session, order_detail_id):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

    if db_order_detail:
        db.delete(db_order_detail)
        db.commit()
        return db_order_detail
    return None
