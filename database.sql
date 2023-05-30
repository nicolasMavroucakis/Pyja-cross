CREATE DATABASE IF NOT EXISTS `db_pii`;
USE `db_pii`;

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_ra` varchar(10) DEFAULT NULL,
  `user_password` varchar(30) DEFAULT NULL,
  `user_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_ra` (`user_ra`)
);

CREATE TABLE IF NOT EXISTS `times` (
  `user_id` int NOT NULL,
  `time` int NOT NULL,
  `game` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `FK__users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
);