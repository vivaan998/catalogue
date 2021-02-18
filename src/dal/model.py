# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Text, text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Categories(Base):
    __tablename__ = 'Categories'

    UUID = Column(String(256), primary_key=True, nullable=False)
    LanguageISO = Column(String(36), primary_key=True, nullable=False)
    Value = Column(Text)


class Image(Base):
    __tablename__ = 'Image'
    RefUUID = Column(String(256), primary_key=True, nullable=False)
    SessionUUID = Column(ForeignKey('Session.UUID', ondelete='CASCADE'), nullable=False)
    Uri = Column(String(256), primary_key=True, nullable=False)


class Session(Base):
    __tablename__ = 'Session'

    UUID = Column(String(256), primary_key=True)
    Name = Column(String(256))
    Tokens = Column(BIGINT(20), nullable=False)
    Category = Column(ForeignKey('Categories.UUID', ondelete='CASCADE'), index=True, nullable=False)
    CreatorUUID = Column(String(256), nullable=False)
    CreationDateTime = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    LastUpdateDatetime = Column(DateTime)
    Description = Column(Text)
    LanguageISO = Column(String(36), server_default='en')

    Categories = relationship('Categories', backref='Categories')
    SessionTag = relationship('SessionTag', backref='SessionTag')


class Live(Base):
    __tablename__ = 'Live'

    UUID = Column(String(256), primary_key=True)
    SessionUUID = Column(ForeignKey('Session.UUID'), index=True)
    PresenterUUID = Column(String(36))
    StartAtGMT = Column(DateTime, nullable=False)
    EndsAtGMT = Column(DateTime, nullable=False)
    LastUpdateDatetime = Column(DateTime)
    CreationDateTime = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    Description = Column(Text)
    LanguageISO = Column(String(36), server_default='en')

    Session = relationship('Session', backref='Session')
    LiveTag = relationship('LiveTag', backref='LiveTag')


class Availability(Base):
    __tablename__ = 'Availability'

    LiveUUID = Column(ForeignKey('Live.UUID', ondelete='CASCADE'), primary_key=True)
    MaxSlots = Column(BIGINT(20), nullable=False)
    BookedSlots = Column(BIGINT(20), nullable=False)
    LastUpdateDatetime = Column(DateTime)


class SessionTag(Base):
    __tablename__ = 'SessionTag'

    SessionUUID = Column(ForeignKey('Session.UUID', ondelete='CASCADE'), primary_key=True, nullable=False)
    Hashtag = Column(Text, primary_key=True, nullable=False)
    LanguageISO = Column(String(36), server_default='en')

    Session = relationship('Session')


class LiveTag(Base):
    __tablename__ = 'LiveTag'

    LiveUUID = Column(ForeignKey('Live.UUID', ondelete='CASCADE'), primary_key=True, nullable=False)
    Hashtag = Column(Text, primary_key=True, nullable=False)
    LanguageISO = Column(String(36), server_default='en')

    Live = relationship('Live')
