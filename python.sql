/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : python

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-05-16 17:24:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('888519375955');

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  `content` text,
  `descript` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES ('1', '文章标题1', '1', '2018-05-14 11:18:57', '哈哈，blog正在进行中1...', '1');
INSERT INTO `article` VALUES ('2', '文章标题2', '2', '2018-05-14 11:28:22', '哈哈，blog正在进行中2...', '2');
INSERT INTO `article` VALUES ('3', '文章标题3', '3', '2018-05-14 11:31:44', '哈哈，blog正在进行中3...', '3');
INSERT INTO `article` VALUES ('4', '文章标题4', '4', '2018-05-14 11:34:06', '哈哈，blog正在进行中4...', '4');
INSERT INTO `article` VALUES ('5', '文章标题5', '5', '2018-05-15 11:24:15', '哈哈，blog正在进行中5...', '5');
INSERT INTO `article` VALUES ('6', '阿道夫', '1', '2018-05-15 11:24:15', '<p>阿道夫</p>\r\n', '阿道夫');
INSERT INTO `article` VALUES ('7', '阿道夫', '1', '2018-05-15 11:24:15', '<p>阿道夫</p>\r\n', '阿道夫');
INSERT INTO `article` VALUES ('8', '阿道夫11', '5', '2018-05-15 11:24:15', '<p>123</p>\r\n', '123');
INSERT INTO `article` VALUES ('9', '阿道夫', '3', '2018-05-16 14:10:03', '<p>阿道夫</p>\r\n', '阿道夫');

-- ----------------------------
-- Table structure for article_tags
-- ----------------------------
DROP TABLE IF EXISTS `article_tags`;
CREATE TABLE `article_tags` (
  `article_id` int(11) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  KEY `article_id` (`article_id`),
  KEY `tag_id` (`tag_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_tags
-- ----------------------------
INSERT INTO `article_tags` VALUES ('1', '1');
INSERT INTO `article_tags` VALUES ('2', '1');
INSERT INTO `article_tags` VALUES ('3', '1');
INSERT INTO `article_tags` VALUES ('4', '2');
INSERT INTO `article_tags` VALUES ('4', '3');
INSERT INTO `article_tags` VALUES ('4', '4');
INSERT INTO `article_tags` VALUES ('5', '4');
INSERT INTO `article_tags` VALUES ('5', '3');
INSERT INTO `article_tags` VALUES ('5', '2');
INSERT INTO `article_tags` VALUES ('8', '1');
INSERT INTO `article_tags` VALUES ('8', '2');
INSERT INTO `article_tags` VALUES ('9', '1');
INSERT INTO `article_tags` VALUES ('9', '2');
INSERT INTO `article_tags` VALUES ('8', '3');
INSERT INTO `article_tags` VALUES ('8', '4');

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', 'Python');
INSERT INTO `category` VALUES ('2', 'Flask');
INSERT INTO `category` VALUES ('3', 'PHP');
INSERT INTO `category` VALUES ('4', 'Symfony');
INSERT INTO `category` VALUES ('5', '1111');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `article_id` (`article_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comment
-- ----------------------------

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('1', 'Python');
INSERT INTO `tag` VALUES ('2', 'Flask');
INSERT INTO `tag` VALUES ('3', 'Php');
INSERT INTO `tag` VALUES ('4', 'Symfony');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
