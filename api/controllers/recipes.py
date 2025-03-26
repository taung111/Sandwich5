from sqlalchemy.orm import Session
from ..models import models, schemas

def create(db: Session, recipe):
    db_recipe = (models.Recipe
                 (amount=recipe.amount,
                  sandwich_id=recipe.sandwich_id,
                  resource_id=recipe.resource_id,))
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe: schemas.RecipeUpdate, recipe_id):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe is None:
        return None

    if recipe.amount is not None:
        db_recipe.amount = recipe.amount
    if recipe.sandwich_id is not None:
        db_recipe.sandwich_id = recipe.sandwich_id
    if recipe.resource_id is not None:
        db_recipe.resource_id = recipe.resource_id

    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete(db: Session, recipe_id):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe is None:
        return None
    db.delete(db_recipe)
    db.commit()
    return db_recipe