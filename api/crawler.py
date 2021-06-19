#!/usr/bin/python3

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from models import models
from db import configuration
from typing import List
from core.repositories import user

router = APIRouter(
    tags=["Users"],
    prefix="/users"
)
get_db = configuration.get_db

@router.get("/", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return user.get_all(db)