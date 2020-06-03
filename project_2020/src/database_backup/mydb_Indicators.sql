-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Indicators`
--

DROP TABLE IF EXISTS `Indicators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Indicators` (
  `indicatorCode` varchar(20) NOT NULL,
  `IndicatorName` varchar(100) DEFAULT NULL,
  `measurementUnit` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`indicatorCode`),
  UNIQUE KEY `IndicatorName_UNIQUE` (`IndicatorName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Indicators`
--

LOCK TABLES `Indicators` WRITE;
/*!40000 ALTER TABLE `Indicators` DISABLE KEYS */;
INSERT INTO `Indicators` VALUES ('EG.IMP.CONS.ZS','Energy imports net ','% of energy use\r'),('NE.EXP.GNFS.ZS','Exports of goods and services ','% of GDP\r'),('NE.GDI.TOTL.ZS','Gross capital formation ','% of GDP\r'),('NE.TRD.GNFS.ZS','Trade ','% of GDP\r'),('NY.EXP.CAPM.KN','Exports as a capacity to import ','constant LCU\r'),('NY.GDP.DEFL.ZS','GDP deflator ','base year varies by country\r'),('NY.GDP.PCAP.KD.ZG','GDP per capita growth ','annual %\r'),('NY.GDP.TOTL.RT.ZS','Total natural resources rents ','% of GDP\r'),('NY.GDS.TOTL.ZS','Gross domestic savings ','% of GDP\r'),('TG.VAL.TOTL.GD.ZS','Merchandise trade ','% of GDP\r'),('TM.VAL.MRCH.WL.CD','Merchandise imports by the reporting economy ','current US$\r'),('TX.VAL.MRCH.WL.CD','Merchandise exports by the reporting economy ','current US$\r');
/*!40000 ALTER TABLE `Indicators` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-22 16:19:51
