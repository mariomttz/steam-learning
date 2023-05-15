-- MariaDB dump 10.19-11.1.0-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: Steam_Learning
-- ------------------------------------------------------
-- Server version	11.1.0-MariaDB

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
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data` (
  `review_range` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `appid` int(11) NOT NULL,
  `precio` float NOT NULL,
  `Action` bit(1) DEFAULT b'0',
  `Adventure` bit(1) DEFAULT b'0',
  `Singleplayer` bit(1) DEFAULT b'0',
  `Casual` bit(1) DEFAULT b'0',
  `Strategy` bit(1) DEFAULT b'0',
  `Simulation` bit(1) DEFAULT b'0',
  `RPG` bit(1) DEFAULT b'0',
  `Multiplayer` bit(1) DEFAULT b'0',
  `Great_Soundtrack` bit(1) DEFAULT b'0',
  `Atmospheric` bit(1) DEFAULT b'0',
  `2D` bit(1) DEFAULT b'0',
  `Puzzle` bit(1) DEFAULT b'0',
  `Early_Access` bit(1) DEFAULT b'0',
  `Open_World` bit(1) DEFAULT b'0',
  `Story_Rich` bit(1) DEFAULT b'0',
  `Co_op` bit(1) DEFAULT b'0',
  `Difficult` bit(1) DEFAULT b'0',
  `Shooter` bit(1) DEFAULT b'0',
  `Sci_fi` bit(1) DEFAULT b'0',
  `First_Person` bit(1) DEFAULT b'0',
  `Horror` bit(1) DEFAULT b'0',
  `VR` bit(1) DEFAULT b'0',
  `Anime` bit(1) DEFAULT b'0',
  `Pixel_Graphics` bit(1) DEFAULT b'0',
  `Funny` bit(1) DEFAULT b'0',
  `Fantasy` bit(1) DEFAULT b'0',
  `Platformer` bit(1) DEFAULT b'0',
  `Female_Protagonist` bit(1) DEFAULT b'0',
  `Free_to_Play` bit(1) DEFAULT b'0',
  `FPS` bit(1) DEFAULT b'0',
  `Survival` bit(1) DEFAULT b'0',
  `Gore` bit(1) DEFAULT b'0',
  `Violent` bit(1) DEFAULT b'0',
  `Sandbox` bit(1) DEFAULT b'0',
  `Retro` bit(1) DEFAULT b'0',
  `Arcade` bit(1) DEFAULT b'0',
  `Comedy` bit(1) DEFAULT b'0',
  `Classic` bit(1) DEFAULT b'0',
  `Nudity` bit(1) DEFAULT b'0',
  `Third_Person` bit(1) DEFAULT b'0',
  `Massively_Multiplayer` bit(1) DEFAULT b'0',
  `Exploration` bit(1) DEFAULT b'0',
  `Point_and_Click` bit(1) DEFAULT b'0',
  `Visual_Novel` bit(1) DEFAULT b'0',
  `Turn_Based` bit(1) DEFAULT b'0',
  `Space` bit(1) DEFAULT b'0',
  `Sports` bit(1) DEFAULT b'0',
  `Rogue_like` bit(1) DEFAULT b'0',
  `Tactical` bit(1) DEFAULT b'0',
  `Cute` bit(1) DEFAULT b'0',
  `Racing` bit(1) DEFAULT b'0',
  `Psychological_Horror` bit(1) DEFAULT b'0',
  `Online_Co_Op` bit(1) DEFAULT b'0',
  `Zombies` bit(1) DEFAULT b'0',
  `Family_Friendly` bit(1) DEFAULT b'0',
  `Sexual_Content` bit(1) DEFAULT b'0',
  `Local_Co_Op` bit(1) DEFAULT b'0',
  `Local_Multiplayer` bit(1) DEFAULT b'0',
  `Controller` bit(1) DEFAULT b'0',
  `Replay_Value` bit(1) DEFAULT b'0',
  `Memes` bit(1) DEFAULT b'0',
  `Building` bit(1) DEFAULT b'0',
  `RTS` bit(1) DEFAULT b'0',
  `Turn_Based_Strategy` bit(1) DEFAULT b'0',
  `Side_Scroller` bit(1) DEFAULT b'0',
  `Fast_Paced` bit(1) DEFAULT b'0',
  `Crafting` bit(1) DEFAULT b'0',
  `Action_RPG` bit(1) DEFAULT b'0',
  `Mystery` bit(1) DEFAULT b'0',
  `Shoot_Em_Up` bit(1) DEFAULT b'0',
  `Dark` bit(1) DEFAULT b'0',
  `Management` bit(1) DEFAULT b'0',
  `Survival_Horror` bit(1) DEFAULT b'0',
  `Hack_and_Slash` bit(1) DEFAULT b'0',
  `War` bit(1) DEFAULT b'0',
  `Historical` bit(1) DEFAULT b'0',
  `Physics` bit(1) DEFAULT b'0',
  `Stealth` bit(1) DEFAULT b'0',
  `Rogue_lite` bit(1) DEFAULT b'0',
  `PvP` bit(1) DEFAULT b'0',
  `Realistic` bit(1) DEFAULT b'0',
  `Short` bit(1) DEFAULT b'0',
  `Isometric` bit(1) DEFAULT b'0',
  `RPGMaker` bit(1) DEFAULT b'0',
  `Moddable` bit(1) DEFAULT b'0',
  `Relaxing` bit(1) DEFAULT b'0',
  `Third_Person_Shooter` bit(1) DEFAULT b'0',
  `Bullet_Hell` bit(1) DEFAULT b'0',
  `Top_Down` bit(1) DEFAULT b'0',
  `Walking_Simulator` bit(1) DEFAULT b'0',
  `Dungeon_Crawler` bit(1) DEFAULT b'0',
  `JRPG` bit(1) DEFAULT b'0',
  `Fighting` bit(1) DEFAULT b'0',
  `Colorful` bit(1) DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 14:26:42
