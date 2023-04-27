-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: bd_reino_del_trevol
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `solicitudes`
--

DROP TABLE IF EXISTS `solicitudes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitudes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `identificacion` varchar(10) NOT NULL,
  `edad` int NOT NULL,
  `afinidad_magia` varchar(200) NOT NULL,
  `grimorio` varchar(50) NOT NULL,
  `estatus` int NOT NULL,
  `datetime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitudes`
--

LOCK TABLES `solicitudes` WRITE;
/*!40000 ALTER TABLE `solicitudes` DISABLE KEYS */;
INSERT INTO `solicitudes` VALUES (1,'mdr','aptest','10004',43,'Oscuridad','Buena fortuna',2,'2023-04-26 18:22:32'),(2,'Miguel','Hidalgo','10005',55,'Fuego','Sinceridad',2,'2023-04-26 18:33:45'),(3,'mdr','aptest','10006',43,'Oscuridad','Amor',2,'2023-04-26 18:34:33'),(5,'JoseMaria','Martinez','Identi002',15,'Luz','Desesperacion',1,'2023-04-26 20:32:19');
/*!40000 ALTER TABLE `solicitudes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_de_magia`
--

DROP TABLE IF EXISTS `tipos_de_magia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_de_magia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_de_magia`
--

LOCK TABLES `tipos_de_magia` WRITE;
/*!40000 ALTER TABLE `tipos_de_magia` DISABLE KEYS */;
INSERT INTO `tipos_de_magia` VALUES (1,'Magia de Acero'),(2,'Magia de Agua'),(3,'Magia de Aire'),(4,'Magia de Alas'),(5,'Magia de Algodón'),(6,'Magia de Almagre'),(7,'Anti-Magia'),(8,'Magia de Arena'),(9,'Magia de Arenisca'),(10,'Magia de Barro'),(11,'Magia de Bestia'),(12,'Magia de Bestia Demoníaca'),(13,'Magia de Bronce'),(14,'Magia de Brújula'),(15,'Magia de Burbujas'),(16,'Magia de Cadenas'),(17,'Magia de Cabello'),(18,'Magia de Canto'),(19,'Magia de Cenizas'),(20,'Magia de Cerezos'),(21,'Magia de Cobre'),(22,'Magia de Comida'),(23,'Magia Compuesta'),(24,'Magia de Comunicación'),(25,'Magia de Corindón'),(26,'Magia de Corte'),(27,'Magia de Creación'),(28,'Magia de Cristal'),(29,'Magia de Cuerpo'),(30,'Magia Curativa'),(31,'Magia de Dados'),(32,'Magia de Danza'),(33,'Magia Debilitante'),(34,'Magia de Espacio'),(35,'Magia de Espadas'),(36,'Magia de Espectros'),(37,'Magia de Espejo'),(38,'Magia de Espinas'),(39,'Magia Espiritual'),(40,'Magia de Fuego'),(41,'Magia de Gel'),(42,'Magia de Gravedad'),(43,'Magia de Hielo'),(44,'Magia de Hilos'),(45,'Magia de Hongos'),(46,'Magia de Huesos'),(47,'Magia de Humo'),(48,'Magia de Ilusión'),(49,'Magia de Imitación'),(50,'Magia de Juego'),(51,'Magia Kotodama'),(52,'Magia del Árbol del Mundo'),(53,'Magia de Luz'),(54,'Magia de Maleficio'),(55,'Magia de Plantas Venenosas'),(56,'Magia de Maldición'),(57,'Método de Maná'),(58,'Magia de Memoria'),(59,'Magia de Mercurio'),(60,'Magia de Mosquito'),(61,'Magia de Mucosidad'),(62,'Magia de Niebla'),(63,'Magia de Nieve'),(64,'Magia de Ojos'),(65,'Magia de Oscuridad'),(66,'Magia de Piedra'),(67,'Magia de Pintura'),(68,'Magia de Plantas'),(69,'Magia de Plumas'),(70,'Magia prohibida'),(71,'Magia de Rayo'),(72,'Magia de Recombinación'),(73,'Magia de Reencarnación'),(74,'Magia Reforzante'),(75,'Magia de Restricción'),(76,'Magia de Roca'),(77,'Magia de Sangre'),(78,'Magia de Sellado'),(79,'Magia de Shakudo'),(80,'Magia de Sombra'),(81,'Magia de Sueños'),(82,'Magia de Tiempo'),(83,'Magia de Tierra'),(84,'Trampa Mágica'),(85,'Magia de Transformación'),(86,'Magia de Transparencia'),(87,'Magia de Veneno'),(88,'Magia de Vidrio'),(89,'Magia de Viento'),(90,'Magia de Vídes'),(91,'Magia de Vórtice'),(92,'Magia de Árboles');
/*!40000 ALTER TABLE `tipos_de_magia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'mdr','king');
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

-- Dump completed on 2023-04-26 23:14:07
