CREATE DATABASE  IF NOT EXISTS `mldb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mldb`;
-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mldb
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Time` double DEFAULT NULL,
  `V1` double DEFAULT NULL,
  `V2` double DEFAULT NULL,
  `V3` double DEFAULT NULL,
  `V4` double DEFAULT NULL,
  `V5` double DEFAULT NULL,
  `V6` double DEFAULT NULL,
  `V7` double DEFAULT NULL,
  `V8` double DEFAULT NULL,
  `V9` double DEFAULT NULL,
  `V10` double DEFAULT NULL,
  `V11` double DEFAULT NULL,
  `V12` double DEFAULT NULL,
  `V13` double DEFAULT NULL,
  `V14` double DEFAULT NULL,
  `V15` double DEFAULT NULL,
  `V16` double DEFAULT NULL,
  `V17` double DEFAULT NULL,
  `V18` double DEFAULT NULL,
  `V19` double DEFAULT NULL,
  `V20` double DEFAULT NULL,
  `V21` double DEFAULT NULL,
  `V22` double DEFAULT NULL,
  `V23` double DEFAULT NULL,
  `V24` double DEFAULT NULL,
  `V25` double DEFAULT NULL,
  `V26` double DEFAULT NULL,
  `V27` double DEFAULT NULL,
  `V28` double DEFAULT NULL,
  `Amount` double DEFAULT NULL,
  `class` int DEFAULT NULL,
  `proba` double DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-16  8:35:03
