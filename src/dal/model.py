# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Text, text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Image(Base):
    __tablename__ = 'Image'

    RefUUID = Column(String(36), primary_key=True, nullable=False)
    Uri = Column(String(36), primary_key=True, nullable=False)
    Title = Column(String(256))
    Description = Column(Text)


class Session(Base):
    __tablename__ = 'Session'

    UUID = Column(String(36), primary_key=True)
    Name = Column(String(256))
    Category = Column(Text)
    CreatorUUID = Column(String(36))
    CreationDateTime = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    LastUpdateDatetime = Column(DateTime)
    Description = Column(Text)
    LanguageISO = Column(String(36))


class Live(Base):
    __tablename__ = 'Live'

    UUID = Column(String(36), primary_key=True)
    SessionUUID = Column(ForeignKey('Session.UUID'), index=True)
    PresenterUUID = Column(String(36))
    StartAtGMT = Column(DateTime, nullable=False)
    EndsAtGMT = Column(DateTime, nullable=False)
    LastUpdateDatetime = Column(DateTime)
    CreationDateTime = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    Session = relationship('Session')


class Availability(Live):
    __tablename__ = 'Availability'

    LiveUUID = Column(ForeignKey('Live.UUID', ondelete='CASCADE'), primary_key=True)
    MaxSlots = Column(BIGINT(20), nullable=False)
    BookedSlots = Column(BIGINT(20), nullable=False)
    LastUpdateDatetime = Column(DateTime)


class SessionTag(Base):
    __tablename__ = 'SessionTag'

    SessionUUID = Column(ForeignKey('Session.UUID', ondelete='CASCADE'), primary_key=True, nullable=False)
    Hashtag = Column(Text, primary_key=True, nullable=False)
    LanguageISO = Column(String(2))

    Session = relationship('Session')


class LiveTag(Base):
    __tablename__ = 'LiveTag'

    LiveUUID = Column(ForeignKey('Live.UUID', ondelete='CASCADE'), primary_key=True, nullable=False)
    Hashtag = Column(String(256), primary_key=True, nullable=False)
    LanguageISO = Column(String(2), primary_key=True, nullable=False)

    Live = relationship('Live')


class LiveTranslation(Base):
    __tablename__ = 'LiveTranslation'

    LiveUUID = Column(ForeignKey('Live.UUID', ondelete='CASCADE'), primary_key=True, nullable=False)
    LanguageISO = Column(String(2), primary_key=True, nullable=False)
    Field = Column(String(128), primary_key=True, nullable=False)
    Value = Column(Text)

    Live = relationship('Live')


class Categories(Base):
    __tablename__ = 'Categories'

    UUID = Column(String(256), primary_key=True, nullable=False)
    LanguageISO = Column(String(36), primary_key=True, nullable=False)
    Value = Column(Text)
