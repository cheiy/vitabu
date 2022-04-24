-- MySQL dump 10.19  Distrib 10.3.31-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: vitabu
-- ------------------------------------------------------
-- Server version	10.3.31-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('b471e205ee61');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authors` (
  `author_id` bigint(20) NOT NULL,
  `author_name` varchar(255) NOT NULL,
  `book_id` bigint(20) NOT NULL,
  PRIMARY KEY (`author_id`),
  KEY `FK_AuthorBook` (`book_id`),
  CONSTRAINT `FK_AuthorBook` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `book_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `isbn_code` bigint(20) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `publisher_id` bigint(20) NOT NULL,
  `grade_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`),
  KEY `publisher_id` (`publisher_id`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`publisher_id`) REFERENCES `publishers` (`publisher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,9789966012753,19,'Mentor Social Studies Learner\'s book',8,4),(4,9789966012715,5,'Mentor Science and Technology Learner\'s book',8,4),(5,9789966572141,3,'Spotlight English Learner\'s Book',4,4),(6,9789966479242,9,'Summit Hygiene and Nutrition Activities',12,2),(8,9789966571847,10,'Spotlight Environmental Activities Learner\'s Book',4,9),(9,9789966652089,12,'Skillgrow Christian Religious Activities Learner\'s Workbook',13,10),(10,9780195746648,9,'Everyday Hygiene and Nutrition Activities',3,1),(11,9789966643001,15,'Longhorn Art and Craft',6,4),(12,9789966012739,4,'Kielekezi cha Kiswahili - Kitabu cha Mwanafunzi',8,4),(13,9789966059529,2,'Mentor Mathematical Activities Learner\'s book',8,9),(14,9789966059536,2,'Mentor Mathematical Activities Learner\'s book',8,10),(15,9789966016102,6,'Targeter Series Combined Encyclopaedia',5,1),(16,9789966571380,3,'Spotlight Language Activities - Learner\'s Book',3,9),(17,9789966571526,9,'Spotlight Hygiene and Nutrition - Learner\'s Book',4,1),(18,9789966571687,2,'Spotlight Mathematics Activities - Learner\'s Book',4,1),(19,9789966571427,3,'Spotlight English Activities - Learner\'s Book',4,1),(20,9789966652065,10,'KLB Skillgrow Environmental Activities - Learner\'s Workbook',13,10),(21,9789966651990,22,'KLB Skillgrow Language Activities - Learner\'s Workbook',13,10),(22,9789966571588,10,'Spotlight Environmental Activities Learner\'s Book',4,1),(23,9780195747003,2,'Let\'s Do Mathematics Activities - Learner\'s Book',3,1),(24,9789966640024,4,'Longhorn Kiswahili Mufti - Kitabu Cha Mwanafunzi',6,1),(25,9780195747843,2,'Let\'s Do Mathematics Activities - Learner\'s Book',3,4),(26,9789966562821,4,'Kiswahili Angaza - Shughuli za Kiswahili',7,1),(27,9789966640086,7,'Longhorn English Literacy Activities - Learner\'s Book',6,1),(28,1970197321174,7,'MTP English Literacy Activities - Workbook for Grade 2',18,2),(29,9789966640154,4,'Longhorn Kusoma na Kuandika Katika Kiswahili - Kitabu Cha Mwanafunzi',6,2),(30,9780996671828,17,'Mastering Computers',3,2),(31,9789966511041,3,'New Primary English - Learner\'s Activities Book 2',10,2),(32,9789966640710,2,'Longhorn Mathematics Activities - Learner\'s Book ',6,10),(33,9789966115218,6,'Premier Revision Encylopaedia',14,10),(34,9789966122049,6,'Distinction Competency Based Curriculum',20,2),(35,9789966479181,10,'Summit Environmental Activities - Learner\'s Book Grade 2',12,2),(36,9780195747010,2,'Let\'s Do Mathematics Activities - Learner\'s Book',3,2),(37,9780195746839,4,'Kiswahili Dadisi Mazoezi ya Lugha - Kitabu cha Mwanafunzi',3,2),(38,9789966059536,2,'Mentor Mathematical Activities Learner\'s book',8,10),(39,9789966643230,18,'Longhorn Methode de Francais',6,5),(40,9789966164759,12,'Golden Bells',21,3),(41,9789966479365,12,'Summit Christian Religious Education Activities',12,2);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grades`
--

DROP TABLE IF EXISTS `grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grades` (
  `grade_id` int(11) NOT NULL AUTO_INCREMENT,
  `grade_num` int(11) DEFAULT NULL,
  `grade_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`grade_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grades`
--

LOCK TABLES `grades` WRITE;
/*!40000 ALTER TABLE `grades` DISABLE KEYS */;
INSERT INTO `grades` VALUES (1,1,'one'),(2,2,'two'),(3,3,'three'),(4,4,'four'),(5,5,'five'),(6,6,'six'),(7,7,'seven'),(8,8,'eight'),(9,100,'pp1 - Pre-Primary One'),(10,101,'pp2 - Pre-Primary Two');
/*!40000 ALTER TABLE `grades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listed_books`
--

DROP TABLE IF EXISTS `listed_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `listed_books` (
  `listing_id` int(11) NOT NULL AUTO_INCREMENT,
  `listed_by` bigint(20) DEFAULT NULL,
  `book_title` varchar(255) DEFAULT NULL,
  `options` enum('sell','exchange','both') DEFAULT NULL,
  `price` int(20) DEFAULT NULL,
  `book_condition` varchar(255) DEFAULT NULL,
  `listing_date` timestamp NULL DEFAULT current_timestamp(),
  `publisher_name` varchar(255) DEFAULT NULL,
  `grade_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`listing_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listed_books`
--

LOCK TABLES `listed_books` WRITE;
/*!40000 ALTER TABLE `listed_books` DISABLE KEYS */;
/*!40000 ALTER TABLE `listed_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publishers`
--

DROP TABLE IF EXISTS `publishers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publishers` (
  `publisher_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `shortname` varchar(50) DEFAULT NULL,
  `longname` varchar(100) DEFAULT NULL,
  `ISBN` bigint(13) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `date_added` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`publisher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publishers`
--

LOCK TABLES `publishers` WRITE;
/*!40000 ALTER TABLE `publishers` DISABLE KEYS */;
INSERT INTO `publishers` VALUES (3,'OUP','Oxford University Press',978019,1,'2021-07-31 21:43:06'),(4,'Spotlight','Spotlight Publishers (EA) Limited',9789966,1,'2021-07-31 21:45:57'),(5,'Targeter','Targeter Educational Publishers Ltd.',9789966571,1,'2021-07-31 21:49:33'),(6,'Longhorn','Longhorn Publishers Limited',9789966640,1,'2021-07-31 21:51:04'),(7,'EAEP','East African Educational Publishers',9789966562,1,'2021-07-31 21:51:52'),(8,'Mentor','Mentor Publishing Company Limited',9789966059,1,'2021-07-31 21:52:48'),(9,'Danmar','Danmar Publishers',9799966863,1,'2021-07-31 21:54:42'),(10,'JKF','The Jomo Kenyatta Foundation',9789966222,1,'2021-07-31 21:55:57'),(11,'Moran','Moran Publishers',9789966630,1,'2021-07-31 21:57:45'),(12,'Phoenix','Phoenix Publishers',9789966479,1,'2021-07-31 22:01:14'),(13,'KLB','Kenya Literature Bureau',9789966656,1,'2021-07-31 22:05:33'),(14,'Queenex','Queenex Publishers Limited',9789966075,1,'2021-08-01 13:03:21'),(18,'MTP','Mountain Top Publishers',1970197,NULL,'2022-04-18 18:49:27'),(19,'SmartBrains','SmartBrains Publication',9780996671,NULL,'2022-04-18 18:56:12'),(20,'Distinction','Distinction Educational Publishers Limited',9789966122049,NULL,'2022-04-18 19:05:17'),(21,'Scripture Union','Scripture Union of Kenya',9789966164759,NULL,'2022-04-18 19:16:43');
/*!40000 ALTER TABLE `publishers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_subjects_subject_name` (`subject_name`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` VALUES (15,'Art and Craft'),(17,'Computer'),(12,'CRE activities'),(11,'Creative Activities and Movement'),(6,'Encyclopaedia'),(3,'English'),(10,'Environmental Activities'),(18,'French'),(21,'Home Science'),(9,'Hygiene and Nutrition Activities'),(13,'IRE Activities'),(4,'Kiswahili'),(8,'Kusoma na Kuandika'),(22,'Language Activities'),(7,'Literacy Activities'),(2,'Mathematics'),(14,'Music Activities'),(20,'Physical Education'),(5,'Science'),(19,'Social Studies'),(16,'Story Books');
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `phone_number` bigint(20) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `signup_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username_2` (`username`,`email_address`),
  KEY `first_name` (`first_name`,`last_name`,`username`,`email_address`,`phone_number`,`gender`,`signup_date`),
  KEY `email_address` (`email_address`),
  KEY `first_name_2` (`first_name`,`last_name`,`username`,`email_address`,`phone_number`),
  KEY `last_name` (`last_name`),
  KEY `username` (`username`),
  KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'','','faychege1@gmail.com','Fay2021!','faychege1@gmail.com',254718656401,'Female','2021-07-29 09:23:01',0),(3,'','','test@test.com','testing','test@test.com',9990292,'unknown','2021-07-31 21:17:34',0),(4,'Samuel','Chege','gschege@gmail.com','UMwNq3MFitbL7Ga','gschege@gmail.com',726864395,'unknown','2022-04-02 23:52:08',0),(5,'Samuel','Chege','gschege@yahoo.com','B!0m,tric','gschege@yahoo.com',726864395,'unknown','2022-04-02 23:59:11',0),(7,'Samuel','Chege','samuel.chege@aar-healthcare.com','pbkdf2:sha256:260000$QVqSp4oNxZb07Xjq$ef6493745fe60ad7d37090a33089e80dcbf9206421962354480cca22bfa75e0d','samuel.chege@aar-healthcare.com',726864395,'unknown','2022-04-03 00:18:08',0),(9,'vitabu','admin','admin@vitabu.ke','pbkdf2:sha256:260000$7JJduvtH6k9sNtn7$a836284e59c97774f8a7d9c8d5d6c9a3f0a4f12d25354e38d382cbc0fee8a4e7','admin@vitabu.ke',726864395,'Male','2022-04-07 10:45:49',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-18 22:39:54
