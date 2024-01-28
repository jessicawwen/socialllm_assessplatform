/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80200 (8.2.0)
 Source Host           : localhost:3306
 Source Schema         : platform

 Target Server Type    : MySQL
 Target Server Version : 80200 (8.2.0)
 File Encoding         : 65001

 Date: 28/01/2024 13:02:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Pairs
-- ----------------------------
DROP TABLE IF EXISTS `Pairs`;
CREATE TABLE `Pairs` (
  `pairsID` int NOT NULL AUTO_INCREMENT,
  `postID` int DEFAULT NULL,
  `comment` text,
  `source` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pairsID`),
  KEY `post_pairs` (`postID`),
  CONSTRAINT `post_pairs` FOREIGN KEY (`postID`) REFERENCES `Posts` (`postID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Pairs
-- ----------------------------
BEGIN;
INSERT INTO `Pairs` (`pairsID`, `postID`, `comment`, `source`) VALUES (1, 1, '[泪]希望雨下的大一点', 'origin');
INSERT INTO `Pairs` (`pairsID`, `postID`, `comment`, `source`) VALUES (2, 1, '希望我的孩子们都是正直的人', 'weibobot');
INSERT INTO `Pairs` (`pairsID`, `postID`, `comment`, `source`) VALUES (3, 2, '我觉得沟通很重要 ', 'socialglm');
INSERT INTO `Pairs` (`pairsID`, `postID`, `comment`, `source`) VALUES (4, 2, '形式主义', 'origin');
COMMIT;

-- ----------------------------
-- Table structure for Posts
-- ----------------------------
DROP TABLE IF EXISTS `Posts`;
CREATE TABLE `Posts` (
  `postID` int NOT NULL AUTO_INCREMENT,
  `post` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`postID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Posts
-- ----------------------------
BEGIN;
INSERT INTO `Posts` (`postID`, `post`) VALUES (1, '明天要去上班了前天洗的衣服没有干，想着今天拿到楼上去晾一下干了带着去，然后刚刚下雨忘记收了，现在彻底干不了了 ​');
INSERT INTO `Posts` (`postID`, `post`) VALUES (2, '偶像不是让人心生向往的吗，为什么你们总是让人产生一种“这里比现实更险恶”的退缩的心情 ​');
INSERT INTO `Posts` (`postID`, `post`) VALUES (3, '是我太钻牛角尖了吗 可是我真的觉得委屈 要深究也可以说都没有对错 但你不愿意先低头 可能这就是你的态度 你随便撂下一句话之后就走了 这也是你的态度 ​ ');
INSERT INTO `Posts` (`postID`, `post`) VALUES (4, '#00后女老师自杀校方拒绝家属看监控#很多人近些年不断吐槽教师承担太多不属于教学性质的工作，然而造成这种情况的根源是什么？ ​');
COMMIT;

-- ----------------------------
-- Table structure for Remarks
-- ----------------------------
DROP TABLE IF EXISTS `Remarks`;
CREATE TABLE `Remarks` (
  `remarkID` int NOT NULL AUTO_INCREMENT,
  `pairsID` int DEFAULT NULL,
  `userID` int DEFAULT NULL,
  `result` text,
  `feedback` text,
  PRIMARY KEY (`remarkID`),
  KEY `pairsID` (`pairsID`),
  KEY `userID` (`userID`),
  CONSTRAINT `remarks_ibfk_1` FOREIGN KEY (`pairsID`) REFERENCES `Pairs` (`pairsID`),
  CONSTRAINT `remarks_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `Users` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Remarks
-- ----------------------------
BEGIN;
INSERT INTO `Remarks` (`remarkID`, `pairsID`, `userID`, `result`, `feedback`) VALUES (1, 1, 1, '4', '');
INSERT INTO `Remarks` (`remarkID`, `pairsID`, `userID`, `result`, `feedback`) VALUES (2, 2, 1, '2', '');
COMMIT;

-- ----------------------------
-- Table structure for Users
-- ----------------------------
DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `userID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '123456',
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Users
-- ----------------------------
BEGIN;
INSERT INTO `Users` (`userID`, `username`, `password`) VALUES (1, 'fudan11', '123456');
INSERT INTO `Users` (`userID`, `username`, `password`) VALUES (2, 'fudan22', '123456');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
