USE db;

-- Catalogue

CREATE TABLE IF NOT EXISTS Session
(
  UUID VARCHAR(256) NOT NULL,
  Name VARCHAR(256),
  Category VARCHAR(256) NOT NULL,
  CreatorUUID VARCHAR(256) NOT NULL,
  CreationDateTime datetime DEFAULT CURRENT_TIMESTAMP,
  LastUpdateDatetime datetime ON UPDATE CURRENT_TIMESTAMP,
  LanguageISO VARCHAR(2),
  Description TEXT,
  CONSTRAINT PK_Session PRIMARY KEY (UUID),
  CONSTRAINT FK_Session FOREIGN KEY (Category) REFERENCES Categories (UUID) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Live
(
  UUID VARCHAR(256) NOT NULL,
  SessionUUID VARCHAR(256),
  PresenterUUID VARCHAR(36),
  StartAtGMT datetime NOT NULL,
  EndsAtGMT datetime NOT NULL,
  LanguageISO VARCHAR(36) NOT NULL,
  Description TEXT NOT NULL,
  LastUpdateDatetime datetime ON UPDATE CURRENT_TIMESTAMP,
  CreationDateTime datetime DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT PK_Live PRIMARY KEY (UUID),
  CONSTRAINT FK_L_SessionUUID FOREIGN KEY (SessionUUID) REFERENCES Session (UUID)
);

CREATE TABLE IF NOT EXISTS Image
(
  RefUUID VARCHAR(256) NOT NULL,
  Uri VARCHAR(36),
  Title VARCHAR(256),
  Description TEXT,
  CONSTRAINT PK_Image PRIMARY KEY (RefUUID, Uri)
);

CREATE TABLE IF NOT EXISTS LiveTag
(
  LiveUUID VARCHAR(256) NOT NULL PRIMARY KEY,
  Hashtag TEXT,
  LanguageISO VARCHAR(2),
  CONSTRAINT FK_LT_LiveUUID FOREIGN KEY (LiveUUID) REFERENCES Live (UUID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS SessionTag
(
  SessionUUID VARCHAR(256) NOT NULL PRIMARY KEY,
  Hashtag TEXT,
  LanguageISO VARCHAR(2),
  CONSTRAINT FK_STSessionUUID FOREIGN KEY (SessionUUID) REFERENCES Session (UUID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Availability
(
  LiveUUID VARCHAR(256) NOT NULL,
  MaxSlots bigint NOT NULL,
  BookedSlots bigint NOT NULL,
  LastUpdateDatetime datetime ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT PK_Availability PRIMARY KEY (LiveUUID),
  CONSTRAINT FK_AVL_LiveUUID FOREIGN KEY (LiveUUID) REFERENCES Live (UUID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Categories
(
  UUID VARCHAR(256) NOT NULL,
  LanguageISO VARCHAR(36) NOT NULL,
  Value TEXT,
  CONSTRAINT PK_Categories PRIMARY KEY (UUID, LanguageISO)
);
