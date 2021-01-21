-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 21, 2021 at 10:06 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db`
--

-- --------------------------------------------------------

--
-- Table structure for table `availability`
--

CREATE TABLE `availability` (
  `LiveUUID` varchar(256) NOT NULL,
  `MaxSlots` bigint(20) NOT NULL,
  `BookedSlots` bigint(20) NOT NULL,
  `LastUpdateDatetime` datetime DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `availability`
--

INSERT INTO `availability` (`LiveUUID`, `MaxSlots`, `BookedSlots`, `LastUpdateDatetime`) VALUES
('2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9', 94, 6, '2021-01-21 14:33:51');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `UUID` varchar(256) NOT NULL,
  `LanguageISO` varchar(36) NOT NULL,
  `Value` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`UUID`, `LanguageISO`, `Value`) VALUES
('abc9011b-ff53-4cad-a747-2233fb343661', 'en', 'hello\r\n'),
('def9011b-ff53-4cad-a747-2233fb343661', 'en', 'morning'),
('f0c9011b-ff53-4cad-a747-2233fb343661', 'en', 'fitness'),
('ghi9011b-ff53-4cad-a747-2233fb343661', 'fr', 'bonjour'),
('ijk9011b-ff53-4cad-a747-2233fb343661', 'fr', 'matin');

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `RefUUID` varchar(256) NOT NULL,
  `Uri` varchar(36) NOT NULL,
  `Title` varchar(256) DEFAULT NULL,
  `Description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `live`
--

CREATE TABLE `live` (
  `UUID` varchar(256) NOT NULL,
  `SessionUUID` varchar(256) DEFAULT NULL,
  `PresenterUUID` varchar(36) DEFAULT NULL,
  `StartAtGMT` datetime NOT NULL,
  `EndsAtGMT` datetime NOT NULL,
  `LanguageISO` varchar(36) NOT NULL,
  `Description` text NOT NULL,
  `LastUpdateDatetime` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  `CreationDateTime` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `live`
--

INSERT INTO `live` (`UUID`, `SessionUUID`, `PresenterUUID`, `StartAtGMT`, `EndsAtGMT`, `LanguageISO`, `Description`, `LastUpdateDatetime`, `CreationDateTime`) VALUES
('2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9', '784a2b7e-317b-4b88-aad5-0e0b62ad93f0', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2021-02-17 18:25:14', '2021-02-17 20:25:14', 'en', 'Live Update', '2021-01-21 09:47:46', '2021-01-21 09:42:19'),
('d1916ed9-ec3b-4aca-8dbf-43f8cda96aca', '8bff1e86-890d-49f7-9b72-b41c75ef440a', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2021-02-17 18:25:14', '2021-02-17 20:25:14', 'en', 'Live Update', '2021-01-21 14:27:33', '2021-01-21 14:24:36');

-- --------------------------------------------------------

--
-- Table structure for table `livetag`
--

CREATE TABLE `livetag` (
  `LiveUUID` varchar(256) NOT NULL,
  `Hashtag` text DEFAULT NULL,
  `LanguageISO` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `livetag`
--

INSERT INTO `livetag` (`LiveUUID`, `Hashtag`, `LanguageISO`) VALUES
('2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9', 'harshil', 'en'),
('d1916ed9-ec3b-4aca-8dbf-43f8cda96aca', 'city,state', 'en');

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE `session` (
  `UUID` varchar(256) NOT NULL,
  `Name` varchar(256) DEFAULT NULL,
  `Category` varchar(256) NOT NULL,
  `CreatorUUID` varchar(256) NOT NULL,
  `CreationDateTime` datetime DEFAULT current_timestamp(),
  `LastUpdateDatetime` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  `LanguageISO` varchar(2) DEFAULT NULL,
  `Description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`UUID`, `Name`, `Category`, `CreatorUUID`, `CreationDateTime`, `LastUpdateDatetime`, `LanguageISO`, `Description`) VALUES
('784a2b7e-317b-4b88-aad5-0e0b62ad93f0', 'Second Session', 'f0c9011b-ff53-4cad-a747-2233fb343661', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2021-01-21 09:31:04', '2021-01-21 09:34:35', 'en', 'Get Fit in 2022'),
('8bff1e86-890d-49f7-9b72-b41c75ef440a', 'Test by Harshil', 'f0c9011b-ff53-4cad-a747-2233fb343661', '98765f64-5717-4562-b3fc-2c963f66afa6', '2021-01-21 14:07:32', NULL, 'en', 'IT companies');

-- --------------------------------------------------------

--
-- Table structure for table `sessiontag`
--

CREATE TABLE `sessiontag` (
  `SessionUUID` varchar(256) NOT NULL,
  `Hashtag` text DEFAULT NULL,
  `LanguageISO` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sessiontag`
--

INSERT INTO `sessiontag` (`SessionUUID`, `Hashtag`, `LanguageISO`) VALUES
('784a2b7e-317b-4b88-aad5-0e0b62ad93f0', '#bestof2021,#fitIndia, #truemotivation', 'en'),
('8bff1e86-890d-49f7-9b72-b41c75ef440a', '#abc', 'en');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `availability`
--
ALTER TABLE `availability`
  ADD PRIMARY KEY (`LiveUUID`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`UUID`,`LanguageISO`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`RefUUID`,`Uri`);

--
-- Indexes for table `live`
--
ALTER TABLE `live`
  ADD PRIMARY KEY (`UUID`),
  ADD KEY `FK_L_SessionUUID` (`SessionUUID`);

--
-- Indexes for table `livetag`
--
ALTER TABLE `livetag`
  ADD PRIMARY KEY (`LiveUUID`);

--
-- Indexes for table `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`UUID`),
  ADD KEY `FK_Session` (`Category`);

--
-- Indexes for table `sessiontag`
--
ALTER TABLE `sessiontag`
  ADD PRIMARY KEY (`SessionUUID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `availability`
--
ALTER TABLE `availability`
  ADD CONSTRAINT `FK_AVL_LiveUUID` FOREIGN KEY (`LiveUUID`) REFERENCES `live` (`UUID`) ON DELETE CASCADE;

--
-- Constraints for table `live`
--
ALTER TABLE `live`
  ADD CONSTRAINT `FK_L_SessionUUID` FOREIGN KEY (`SessionUUID`) REFERENCES `session` (`UUID`);

--
-- Constraints for table `livetag`
--
ALTER TABLE `livetag`
  ADD CONSTRAINT `FK_LT_LiveUUID` FOREIGN KEY (`LiveUUID`) REFERENCES `live` (`UUID`) ON DELETE CASCADE;

--
-- Constraints for table `session`
--
ALTER TABLE `session`
  ADD CONSTRAINT `FK_Session` FOREIGN KEY (`Category`) REFERENCES `categories` (`UUID`) ON DELETE CASCADE;

--
-- Constraints for table `sessiontag`
--
ALTER TABLE `sessiontag`
  ADD CONSTRAINT `FK_STSessionUUID` FOREIGN KEY (`SessionUUID`) REFERENCES `session` (`UUID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
