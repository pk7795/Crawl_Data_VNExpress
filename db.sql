CREATE DATABASE	Crawl_Data;
use Crawl_Data;
CREATE TABLE `categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50),
  `url` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);

CREATE TABLE `news` (
  `new_id` bigint NOT NULL AUTO_INCREMENT,
  `title` text,
  `description` longtext,
  `original_url` text,
  `author` varchar(255) DEFAULT NULL,
  `date_created` varchar(255) DEFAULT NULL,
  `category_id` bigint DEFAULT NULL,
  PRIMARY KEY (`new_id`),
  UNIQUE KEY `new_id_UNIQUE` (`new_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `contents_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
);