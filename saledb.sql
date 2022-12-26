-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: saledb
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `hoadon`
--

DROP TABLE IF EXISTS `hoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoadon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tongTien` double DEFAULT NULL,
  `phieuThuePhong_id` int NOT NULL,
  `ngayTao` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  `phuThu` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_phieuThuePhong_idx` (`phieuThuePhong_id`),
  KEY `fk_user_id_idx` (`user_id`),
  CONSTRAINT `fk_phieuThuePhong` FOREIGN KEY (`phieuThuePhong_id`) REFERENCES `phieuthuephong` (`id`),
  CONSTRAINT `fk_user_hoadon` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoadon`
--

LOCK TABLES `hoadon` WRITE;
/*!40000 ALTER TABLE `hoadon` DISABLE KEYS */;
INSERT INTO `hoadon` VALUES (4,1350000,5,'2022-12-14 21:11:18',2,350000);
/*!40000 ALTER TABLE `hoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieuthuephong`
--

DROP TABLE IF EXISTS `phieuthuephong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieuthuephong` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tenKhach` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `loaiKhach` enum('NOI_DIA','NUOC_NGOAI') COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `CMND` varchar(20) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `diaChi` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `ngayNhanPhong` datetime DEFAULT NULL,
  `ngayTraPhong` datetime DEFAULT NULL,
  `phong_id` int NOT NULL,
  `soLuongKhach` int NOT NULL,
  `tinhTrang` enum('CHUA_THANH_TOAN','DA_THANH_TOAN') COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `active` tinyint DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_phong_id_idx` (`phong_id`),
  KEY `fk_user_id_idx` (`user_id`),
  CONSTRAINT `fk_phong_id` FOREIGN KEY (`phong_id`) REFERENCES `phong` (`id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuthuephong`
--

LOCK TABLES `phieuthuephong` WRITE;
/*!40000 ALTER TABLE `phieuthuephong` DISABLE KEYS */;
INSERT INTO `phieuthuephong` VALUES (5,'Qui','NOI_DIA','231','Nha Trang','2022-12-12 19:35:42',NULL,5,3,'DA_THANH_TOAN',1,2);
/*!40000 ALTER TABLE `phieuthuephong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phong`
--

DROP TABLE IF EXISTS `phong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phong` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tenPhong` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `loaiPhong` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `donGia` double NOT NULL,
  `tinhTrang` enum('TRONG','DA_DAT') COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phong`
--

LOCK TABLES `phong` WRITE;
/*!40000 ALTER TABLE `phong` DISABLE KEYS */;
INSERT INTO `phong` VALUES (5,'A01','Vip',500000,'TRONG'),(6,'A02','Normal',300000,'TRONG');
/*!40000 ALTER TABLE `phong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quidinh`
--

DROP TABLE IF EXISTS `quidinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quidinh` (
  `soLuong` int NOT NULL,
  `tiLePhuThu` double NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quidinh`
--

LOCK TABLES `quidinh` WRITE;
/*!40000 ALTER TABLE `quidinh` DISABLE KEYS */;
INSERT INTO `quidinh` VALUES (2,35,1);
/*!40000 ALTER TABLE `quidinh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `joined_date` datetime DEFAULT NULL,
  `avatar` varchar(150) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `user_role` enum('ADMIN','USER','NHANVIEN') COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `gmail` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `address` varchar(150) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Tu','admin','202cb962ac59075b964b07152d234b70',1,'2022-11-30 14:39:14',NULL,'ADMIN',NULL,NULL,NULL),(2,'Tuấn','user1','202cb962ac59075b964b07152d234b70',1,'2022-12-12 14:23:36',NULL,'NHANVIEN',NULL,NULL,NULL),(3,'Tuấn','user2','202cb962ac59075b964b07152d234b70',1,'2022-12-14 21:19:34',NULL,'USER','abc@gmail.com','354325','sad');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-14 21:24:28
