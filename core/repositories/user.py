#!/usr/bin/python3

from sqlalchemy.orm import Session
from models import models
from fastapi import HTTPException, status

def get_all(db: Session):
    users = db.query(models.User).all()
    return users