#!/usr/bin/python3

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from models import models
from db import configuration
from typing import List
from core.repositories import user
from core.crawlers.RankedPages import RankedPages

router = APIRouter(
    tags=["Crawler"],
    prefix="/crawler"
)

@router.get("/get_most_visted_pages", status_code=status.HTTP_200_OK)
def get_most_visited_pages(website: str):
    rankedPages = RankedPages(website)
    ranked_pages_links = rankedPages.get_suggested_pages(limit=10)
    return {'status': status.HTTP_200_OK, 'data': ranked_pages_links}