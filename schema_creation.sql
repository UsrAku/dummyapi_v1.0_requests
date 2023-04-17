/*Sql file for creating a table in our MySql docker server
Creates User_Profiles table with required fields and their data types
Can be used to drop the DB from container terminal*/

DROP DATABASE IF EXISTS `USER_DB`;
CREATE DATABASE `USER_DB`;
USE `USER_DB`;

DROP TABLE IF EXISTS `User_Profiles`;
CREATE TABLE `User_Profiles` (
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `name_character_count` INT(100) NOT NULL
);