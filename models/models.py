from db.configuration import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)


class Website(Base):
    __tablename__ = "websites"
    id = Column(Integer, primary_key=True,index=True)
    url = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))


class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True,index=True)
    url = Column(String)
    website_id = Column(Integer, ForeignKey("websites.id"))


class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True,index=True)
    startAt = Column(DateTime)
    endAt = Column(DateTime)
    page_id = Column(Integer, ForeignKey("pages.id"))


class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    type = Column(String)


class ScanDetail(Base):
    __tablename__ = "scan_details"
    id = Column(Integer, primary_key=True,index=True)
    score = Column(Integer)
    scan_id = Column(Integer, ForeignKey("scans.id"))
    rule_id = Column(Integer, ForeignKey("rules.id"))


