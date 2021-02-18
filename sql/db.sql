-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Availability`
--

DROP TABLE IF EXISTS `Availability`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Availability` (
  `LiveUUID` varchar(256) NOT NULL,
  `MaxSlots` bigint NOT NULL,
  `BookedSlots` bigint NOT NULL,
  `LastUpdateDatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`LiveUUID`),
  CONSTRAINT `FK_AVL_LiveUUID` FOREIGN KEY (`LiveUUID`) REFERENCES `Live` (`UUID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Availability`
--

LOCK TABLES `Availability` WRITE;
/*!40000 ALTER TABLE `Availability` DISABLE KEYS */;
INSERT INTO `Availability` VALUES ('2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9',94,6,'2021-01-21 14:33:51');
/*!40000 ALTER TABLE `Availability` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Categories`
--

DROP TABLE IF EXISTS `Categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Categories` (
  `UUID` varchar(256) NOT NULL,
  `LanguageISO` varchar(36) NOT NULL,
  `Value` text,
  PRIMARY KEY (`UUID`,`LanguageISO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categories`
--

LOCK TABLES `Categories` WRITE;
/*!40000 ALTER TABLE `Categories` DISABLE KEYS */;
INSERT INTO `Categories` VALUES ('abc9011b-ff53-4cad-a747-2233fb343661','en','hello\r\n'),('def9011b-ff53-4cad-a747-2233fb343661','en','morning'),('f0c9011b-ff53-4cad-a747-2233fb343661','en','fitness'),('ghi9011b-ff53-4cad-a747-2233fb343661','fr','bonjour'),('ijk9011b-ff53-4cad-a747-2233fb343661','fr','matin');
/*!40000 ALTER TABLE `Categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Image`
--

DROP TABLE IF EXISTS `Image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Image` (
  `RefUUID` varchar(256) NOT NULL,
  `Uri` varchar(36) NOT NULL,
  `Title` varchar(256) DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`RefUUID`,`Uri`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Image`
--

LOCK TABLES `Image` WRITE;
/*!40000 ALTER TABLE `Image` DISABLE KEYS */;
/*!40000 ALTER TABLE `Image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Live`
--

DROP TABLE IF EXISTS `Live`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Live` (
  `UUID` varchar(256) NOT NULL,
  `SessionUUID` varchar(256) DEFAULT NULL,
  `PresenterUUID` varchar(36) DEFAULT NULL,
  `StartAtGMT` datetime NOT NULL,
  `EndsAtGMT` datetime NOT NULL,
  `LanguageISO` varchar(36) NOT NULL,
  `Description` text NOT NULL,
  `LastUpdateDatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `CreationDateTime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`UUID`),
  KEY `FK_L_SessionUUID` (`SessionUUID`),
  CONSTRAINT `FK_L_SessionUUID` FOREIGN KEY (`SessionUUID`) REFERENCES `Session` (`UUID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Live`
--

LOCK TABLES `Live` WRITE;
/*!40000 ALTER TABLE `Live` DISABLE KEYS */;
INSERT INTO `Live` VALUES ('2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9','784a2b7e-317b-4b88-aad5-0e0b62ad93f0','3fa85f64-5717-4562-b3fc-2c963f66afa6','2021-02-17 18:25:14','2021-02-17 20:25:14','en','Live Update','2021-01-21 09:47:46','2021-01-21 09:42:19'),('43906fc2-279f-4be1-a866-c7393b689b99','917de83e-1825-4bbb-bd58-3fb1a8959bfd','3fa85f64-5717-4562-b3fc-2c963f66afa6','2021-01-17 18:25:15','2021-01-17 21:25:15','en','Live Unit Test',NULL,'2021-01-22 02:22:42'),('d1916ed9-ec3b-4aca-8dbf-43f8cda96aca','8bff1e86-890d-49f7-9b72-b41c75ef440a','3fa85f64-5717-4562-b3fc-2c963f66afa6','2021-02-17 18:25:14','2021-02-17 20:25:14','en','Live Update','2021-01-21 14:27:33','2021-01-21 14:24:36');
/*!40000 ALTER TABLE `Live` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LiveTag`
--

DROP TABLE IF EXISTS `LiveTag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LiveTag` (
  `LiveUUID` varchar(256) NOT NULL,
  `Hashtag` text,
  `LanguageISO` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`LiveUUID`),
  CONSTRAINT `FK_LT_LiveUUID` FOREIGN KEY (`LiveUUID`) REFERENCES `Live` (`UUID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LiveTag`
--

LOCK TABLES `LiveTag` WRITE;
/*!40000 ALTER TABLE `LiveTag` DISABLE KEYS */;
INSERT INTO `LiveTag` VALUES ('2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9','harshil','en'),('43906fc2-279f-4be1-a866-c7393b689b99','unit,test','en'),('d1916ed9-ec3b-4aca-8dbf-43f8cda96aca','city,state','en');
/*!40000 ALTER TABLE `LiveTag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Session`
--

DROP TABLE IF EXISTS `Session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Session` (
  `UUID` varchar(256) NOT NULL,
  `Name` varchar(256) DEFAULT NULL,
  `Category` varchar(256) NOT NULL,
  `CreatorUUID` varchar(256) NOT NULL,
  `CreationDateTime` datetime DEFAULT CURRENT_TIMESTAMP,
  `LastUpdateDatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `LanguageISO` varchar(2) DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`UUID`),
  KEY `FK_Session` (`Category`),
  CONSTRAINT `FK_Session` FOREIGN KEY (`Category`) REFERENCES `Categories` (`UUID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Session`
--

LOCK TABLES `Session` WRITE;
/*!40000 ALTER TABLE `Session` DISABLE KEYS */;
INSERT INTO `Session` VALUES ('784a2b7e-317b-4b88-aad5-0e0b62ad93f0','Second Session','f0c9011b-ff53-4cad-a747-2233fb343661','3fa85f64-5717-4562-b3fc-2c963f66afa6','2021-01-21 09:31:04','2021-01-21 09:34:35','en','Get Fit in 2022'),('8bff1e86-890d-49f7-9b72-b41c75ef440a','First Session','f0c9011b-ff53-4cad-a747-2233fb343661','3fa85f64-5717-4562-b3fc-2c963f66afa6','2021-01-21 14:07:32','2021-01-22 02:22:42','en','Unit test module for put'),('917de83e-1825-4bbb-bd58-3fb1a8959bfd','my very First Session','f0c9011b-ff53-4cad-a747-2233fb343661','3fa85f64-5717-4562-b3fc-2c963f66afa6','2021-01-22 00:48:17',NULL,'en','Unit test in 2021'),('b7c1a1d1-29ae-4447-a3d7-6ad934ec5091','my very First Session','f0c9011b-ff53-4cad-a747-2233fb343661','3fa85f64-5717-4562-b3fc-2c963f66afa6','2021-01-22 02:22:42',NULL,'en','Unit test in 2021');
/*!40000 ALTER TABLE `Session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SessionTag`
--

DROP TABLE IF EXISTS `SessionTag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SessionTag` (
  `SessionUUID` varchar(256) NOT NULL,
  `Hashtag` text,
  `LanguageISO` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`SessionUUID`),
  CONSTRAINT `FK_STSessionUUID` FOREIGN KEY (`SessionUUID`) REFERENCES `Session` (`UUID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SessionTag`
--

LOCK TABLES `SessionTag` WRITE;
/*!40000 ALTER TABLE `SessionTag` DISABLE KEYS */;
INSERT INTO `SessionTag` VALUES ('784a2b7e-317b-4b88-aad5-0e0b62ad93f0','#bestof2021,#fitIndia, #truemotivation','en'),('8bff1e86-890d-49f7-9b72-b41c75ef440a','#bestof2021,#fitIndia,#unittest','en'),('917de83e-1825-4bbb-bd58-3fb1a8959bfd','#bestof2021,#fitIndia,#unittest','en'),('b7c1a1d1-29ae-4447-a3d7-6ad934ec5091','#bestof2021,#fitIndia,#unittest','en');
/*!40000 ALTER TABLE `SessionTag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-22  2:24:51
