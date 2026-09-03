CREATE DATABASE  IF NOT EXISTS `sgc` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sgc`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: sgc
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `atendimento`
--

DROP TABLE IF EXISTS `atendimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atendimento` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `dt_atendimento` datetime NOT NULL,
  `cliente_id` int unsigned NOT NULL,
  `vendedor_id` int unsigned NOT NULL,
  `usuario_id` int unsigned NOT NULL,
  `produto_servico` varchar(25) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `assunto` varchar(20) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `descricao` varchar(4000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `solucao` varchar(4000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `status_atendimento` varchar(15) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_atendimento_cliente` (`cliente_id`),
  KEY `fk_atendimento_vendedor` (`vendedor_id`),
  KEY `fk_atendimento_usuario` (`usuario_id`),
  CONSTRAINT `fk_atendimento_cliente` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`),
  CONSTRAINT `fk_atendimento_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `fk_atendimento_vendedor` FOREIGN KEY (`vendedor_id`) REFERENCES `vendedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atendimento`
--

LOCK TABLES `atendimento` WRITE;
/*!40000 ALTER TABLE `atendimento` DISABLE KEYS */;
INSERT INTO `atendimento` VALUES (1,'2024-09-07 00:00:00',1,1,1,'Coca-cola','Reclamação','Disse que o produto estava muito caro','Oferecemos a Pepsi','Finalizado'),(2,'2024-09-28 00:00:00',1,1,1,'Parafuso','Reclamação','Reclamou que o tamanho do parafuso estava menor','Produto foi trocado',NULL),(3,'2024-10-23 00:00:00',1,1,1,'Bicicleta','Elogio','Gostou do atendimento','',NULL),(4,'2024-11-14 00:00:00',1,1,1,'Notebook','Reclamação','Cliente afirmou que o produto estava com defeito','Trocamos o produto',NULL);
/*!40000 ALTER TABLE `atendimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `cpf` varchar(11) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `rg` varchar(15) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `sexo` varchar(9) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `dt_nascimento` date NOT NULL,
  `cep` int unsigned NOT NULL,
  `logradouro` varchar(100) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `end_num` int unsigned NOT NULL,
  `complemento` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `bairro` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `cidade` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `uf` varchar(2) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `telefone` varchar(10) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `celular` varchar(11) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Maria','12345678900','123456789','Feminino','2003-07-31',12500000,'Rua Edmundo Morewood',1001,'Apto 13','Estiva','Taubate','SP','1236332595','12991230000','maria.maria@email.com'),(2,'Mateus','00950768830','5633914701','Masculino','1992-08-09',12040809,'Rua Celso Charuri',65,'Apto 15','Portal da Mantiqueira','Taubate','SP','1125267800','11997468800','mateus1@gov.sp'),(3,'Luiz','01001001099','010110008','Masculino','1988-12-06',11040000,'Rua Teste',12,'Apto 1','Chacara das Paineiras','Osasco','SP','1136332200','11995558888','luiz@email.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `cpf` varchar(11) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `sexo` varchar(9) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `cargo` varchar(100) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `setor` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `dt_admissao` date DEFAULT NULL,
  `status` varchar(10) COLLATE utf8mb3_general_mysql500_ci NOT NULL DEFAULT 'Inativo',
  `qtd_cadastro` int DEFAULT NULL,
  `login` varchar(25) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `senha` varchar(8) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Paulo','99988877700','Masculino','Assistente','Atendimento','2023-06-07','Ativo',NULL,'paulo','123'),(2,'Administrador','00000000000','Masculino','Diretoria','TI','2003-02-05','Ativo',NULL,'admin','admin'),(3,'Teste senha','00000000000','Masculino','Teste','Teste','2024-10-18','Ativo',NULL,'teste','teste1'),(4,'Teste Status','00000000000','Masculino','Teste','Teste','2024-10-19','Inativo',NULL,'status','status'),(5,'Teste Data','00000000000','Masculino','Teste','Teste','2024-10-10','Ativo',NULL,'testedata','testew'),(6,'lavinia','90980012333','Feminino','Gestora','Comercial','2022-11-22','Inativo',NULL,'lavinia','lavinia'),(7,'Nickolas','48196853840','Masculino','Programador','TI','2024-12-10','Ativo',NULL,'nickolas','123');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendedor`
--

DROP TABLE IF EXISTS `vendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendedor` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `cpf` varchar(11) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `sexo` varchar(9) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `dt_nascimento` date NOT NULL,
  `telefone` varchar(10) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `celular` varchar(11) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb3_general_mysql500_ci NOT NULL,
  `conselho` varchar(200) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  `nr_conselho` varchar(200) COLLATE utf8mb3_general_mysql500_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendedor`
--

LOCK TABLES `vendedor` WRITE;
/*!40000 ALTER TABLE `vendedor` DISABLE KEYS */;
INSERT INTO `vendedor` VALUES (1,'Ricardo','02000000000','Masculino','1994-06-02','1200000000','12000000000','ricardo.vendas@email.com',NULL,NULL),(2,'Michel','09080043211','Masculino','1957-07-02','1134560000','11997680999','michel.silva@gmail.com','Sindicato','000');
/*!40000 ALTER TABLE `vendedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-11 23:44:26
