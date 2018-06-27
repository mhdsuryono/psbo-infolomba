-- MySQL dump 10.16  Distrib 10.2.14-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: lombakampus
-- ------------------------------------------------------
-- Server version	10.2.14-MariaDB

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
-- Table structure for table `adm_lomba`
--

DROP TABLE IF EXISTS `adm_lomba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adm_lomba` (
  `id_adm` int(11) NOT NULL AUTO_INCREMENT,
  `id_ketua` int(11) DEFAULT NULL,
  `id_lomba` int(11) DEFAULT NULL,
  `nama_tim` varchar(255) DEFAULT NULL,
  `status_penyisihan` int(4) DEFAULT NULL,
  PRIMARY KEY (`id_adm`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_lomba`
--

LOCK TABLES `adm_lomba` WRITE;
/*!40000 ALTER TABLE `adm_lomba` DISABLE KEYS */;
INSERT INTO `adm_lomba` VALUES (1,1,1,'sapi team',0),(2,4,4,'the A team',0),(3,8,5,'faz',0),(4,9,5,'faz',0),(5,11,9,'the great gastby',0),(6,12,9,'the fast gastby',0),(7,3,44,'pppp',0),(8,12,44,'pppp',0),(9,13,44,'aaa',0),(10,17,44,'bbb',0),(11,33,10,'kebau',0),(12,33,9,'semut',0);
/*!40000 ALTER TABLE `adm_lomba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anggota_lomba`
--

DROP TABLE IF EXISTS `anggota_lomba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anggota_lomba` (
  `id_adm` int(11) DEFAULT NULL,
  `id_anggota` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anggota_lomba`
--

LOCK TABLES `anggota_lomba` WRITE;
/*!40000 ALTER TABLE `anggota_lomba` DISABLE KEYS */;
INSERT INTO `anggota_lomba` VALUES (4,4),(4,6),(4,7),(10,17),(10,34),(11,33),(12,33),(12,5);
/*!40000 ALTER TABLE `anggota_lomba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat` (
  `id_chat` int(11) NOT NULL AUTO_INCREMENT,
  `id_pengirim` int(11) DEFAULT NULL,
  `id_penerima` int(11) DEFAULT NULL,
  `pesan` varchar(4096) DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `status_baca` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_chat`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (2,1,4,'wah, ada ayam goreng','2018-05-24 19:15:08',0),(3,1,4,'jamur berjamiran','2018-05-24 19:22:34',0),(4,1,3,'jamur berjamiran','2018-05-24 19:36:09',0),(5,1,1,'jamur berjamiran','2018-05-24 19:36:13',0),(6,5,1,'jamur berjamiran','2018-05-24 19:36:20',0),(7,99,1,'jamur berjamiran','2018-05-24 19:46:24',0),(8,1,87,'jamur berjamiran','2018-05-24 19:46:36',0),(9,3,6,'makan yuk','2018-06-27 12:55:35',0),(10,6,3,'yuk makan sekarang','2018-06-27 12:55:35',0),(11,3,6,'makan yuk','2018-06-27 12:56:07',0),(12,6,3,'yuk makan sekarang','2018-06-27 12:56:07',0),(13,3,6,'makan yuk','2018-06-27 12:56:13',0),(14,6,3,'yuk makan sekarang','2018-06-27 12:56:13',0);
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lomba`
--

DROP TABLE IF EXISTS `lomba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lomba` (
  `id_lomba` int(11) NOT NULL AUTO_INCREMENT,
  `nama_lomba` varchar(255) DEFAULT NULL,
  `deskripsi` varchar(4096) DEFAULT NULL,
  `tanggal_dibuat` datetime DEFAULT NULL,
  `tanggal_mulai` datetime DEFAULT NULL,
  `tanggal_ditutup` datetime DEFAULT NULL,
  `tempat` varchar(255) DEFAULT NULL,
  `biaya` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `max_anggota` int(10) DEFAULT NULL,
  `kategori` varchar(255) DEFAULT NULL,
  `aturan` text DEFAULT NULL,
  `hadiah` text DEFAULT NULL,
  PRIMARY KEY (`id_lomba`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lomba`
--

LOCK TABLES `lomba` WRITE;
/*!40000 ALTER TABLE `lomba` DISABLE KEYS */;
INSERT INTO `lomba` VALUES (9,'karambol','2018-12-12 00:00:00','2018-05-13 09:54:52','2018-08-15 00:00:00','2018-12-19 12:12:12','deket GWW',50000,0,2,'makan goerngan',NULL,NULL),(10,'balap karung','lomba dimana kita menggunakan karung','2018-05-13 09:58:42','2018-08-15 00:00:00','2018-09-25 00:00:00','lapangan sempur',50000,4,5,'lari',NULL,NULL);
/*!40000 ALTER TABLE `lomba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pembayaran`
--

DROP TABLE IF EXISTS `pembayaran`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pembayaran` (
  `id_ketua` int(11) DEFAULT NULL,
  `id_lomba` int(11) DEFAULT NULL,
  `status_pembayaran` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pembayaran`
--

LOCK TABLES `pembayaran` WRITE;
/*!40000 ALTER TABLE `pembayaran` DISABLE KEYS */;
INSERT INTO `pembayaran` VALUES (9,5,2),(11,9,0),(12,9,0),(17,44,0),(33,10,0),(33,9,0);
/*!40000 ALTER TABLE `pembayaran` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) DEFAULT NULL,
  `jenis_kelamin` tinyint(1) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `universitas` varchar(255) DEFAULT NULL,
  `nomor_ktm` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `status_aktif` tinyint(1) DEFAULT NULL,
  `status_akses` int(11) DEFAULT NULL,
  `no_hp` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'sapi',1,'nino@gmail.com','UI','G645','1234',0,0,NULL),(2,'kevin',1,'kebin@gmail.com','IPB','G645','1234',0,0,NULL),(3,'jodhji',1,'jod@gmail.com','Sriwijaya','g6415008','1234',0,0,NULL),(4,'jod',1,'jodaq@gmail.com','ipb','g641500','gorengan',0,0,NULL),(5,'jod',1,'jodq@gmail.com','ipb','g641500','1234',1,0,NULL);
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

-- Dump completed on 2018-06-27 18:27:46
