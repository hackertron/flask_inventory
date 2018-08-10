-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 10, 2018 at 07:45 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `issued_stock`
--

CREATE TABLE `issued_stock` (
  `id` int(11) NOT NULL,
  `issue_to` int(11) NOT NULL,
  `package` varchar(10) NOT NULL,
  `single_key` varchar(15) NOT NULL,
  `key_range` varchar(15) NOT NULL,
  `multiple_key` varchar(20) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `issued_stock`
--

INSERT INTO `issued_stock` (`id`, `issue_to`, `package`, `single_key`, `key_range`, `multiple_key`, `time`) VALUES
(1, 41, 'Platinum', '1212', '', '', '2018-08-10 00:33:26'),
(2, 42, 'Platinum', '', '20-30', '', '2018-08-10 00:33:58'),
(3, 42, 'Platinum', '', '20-30', '', '2018-08-10 00:34:15');

-- --------------------------------------------------------

--
-- Table structure for table `packages`
--

CREATE TABLE `packages` (
  `id` int(11) NOT NULL,
  `name` enum('Platinum','Silver','Gold','Diamond') NOT NULL,
  `users_count` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `packages`
--

INSERT INTO `packages` (`id`, `name`, `users_count`) VALUES
(1, 'Platinum', 0),
(2, 'Silver', 4),
(3, 'Gold', 0),
(4, 'Diamond', 0);

-- --------------------------------------------------------

--
-- Table structure for table `serial_keys`
--

CREATE TABLE `serial_keys` (
  `id` int(11) NOT NULL,
  `key1` varchar(30) NOT NULL,
  `key2` varchar(30) NOT NULL,
  `package` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `serial_keys`
--

INSERT INTO `serial_keys` (`id`, `key1`, `key2`, `package`) VALUES
(1, '12121', '12121', 'Silver'),
(2, '12', '', 'Silver');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` enum('Admin','Distributor','Dealer','User') NOT NULL DEFAULT 'User'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`, `type`) VALUES
(38, 'test', 'test@test.com', 'test', '$5$rounds=535000$/lodDQA6DQ30xFXJ$UMrdiJhOf3X13J.43sChH2pSdKBpoQkk0jUzw8fIAB1', 'User'),
(39, 'root', 'root@root.com', 'root', '$5$rounds=535000$WTLLCXXL8MQFhp4B$PvpHeYtyifdqh2LINFQEws7Htg6Bhb8buP5CopOb2xA', 'Admin'),
(40, 'user5', 'user5@user.com', 'user5', '$5$rounds=535000$HSs/MZAiUwgto08X$gav2yOekp6CjKb4sVjUpUPAwqMmBXjED8t2QzBa/6nA', 'User'),
(41, 'dist1', 'dist1@dist.com', 'dist1', '$5$rounds=535000$C5UhBoR5OYnmija4$ZEq94qUKbilG/pwnbA49bkYqdbb0fqdAnOqf7WA3FJ.', 'Distributor'),
(42, 'deal1', 'deal1@deal.com', 'deal1', '$5$rounds=535000$/OBGffMlXsOZ.l3w$HjJd99pcoI6dpLSaP2cEUlVVdMlKtBHKXCJZqWb55B2', 'Dealer');

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `org_name` varchar(50) NOT NULL,
  `contact_person` varchar(50) NOT NULL,
  `contact_email` varchar(100) NOT NULL,
  `contact_no` bigint(11) NOT NULL,
  `address` varchar(500) NOT NULL,
  `state` varchar(30) NOT NULL,
  `pin_code` int(6) NOT NULL,
  `city` varchar(50) NOT NULL,
  `country` varchar(30) NOT NULL,
  `GSTIN_number` varchar(15) NOT NULL,
  `serial_key_2` varchar(30) NOT NULL,
  `package` varchar(10) NOT NULL,
  `tally` tinyint(1) NOT NULL,
  `busy` tinyint(1) NOT NULL,
  `openoffice` tinyint(1) NOT NULL,
  `username1` varchar(30) NOT NULL,
  `username2` varchar(30) NOT NULL,
  `username3` varchar(30) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`id`, `user_id`, `org_name`, `contact_person`, `contact_email`, `contact_no`, `address`, `state`, `pin_code`, `city`, `country`, `GSTIN_number`, `serial_key_2`, `package`, `tally`, `busy`, `openoffice`, `username1`, `username2`, `username3`, `time`) VALUES
(4, 38, 'test', 'test', 'test@test.com', 9988776655, 'asdasdasdasdasdasdasd', 'asdasdas', 110092, 'Laxmi Nagar, Delhi', 'India', '22AAAAA0000A1Z5', '12112', 'Silver', 1, 0, 0, 'asd', 'sad', 'asdas', '2018-08-05 12:59:42'),
(5, 40, 'test', 'test', 'test@test.com', 9988776655, 'asdasdasdasdasdasdasd', 'asdasdas', 110092, 'Laxmi Nagar, Delhi', 'India', '22AAAAA0000A1Z5', '12112', 'Silver', 1, 0, 0, 'asd', 'sad', 'asdas', '2018-08-08 00:33:12'),
(6, 41, 'dist1', 'dist1', 'dist1@dist.com', 9999999999, 'some random address here ', 'Goa', 111111, 'silversand', 'India', '22AAAAA0000A1Z5', '12112', 'Silver', 1, 1, 0, 'asd', 'sad', 'asdas', '2018-08-08 00:41:05'),
(7, 42, 'test', 'test', 'test@test.com', 9988776655, 'asdasdasdasdasdasdasd', 'asdasdas', 110092, 'Laxmi Nagar, Delhi', 'India', '22AAAAA0000A1Z5', '12112', 'Silver', 1, 0, 0, 'asd', 'sad', 'asdas', '2018-08-08 00:43:01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `issued_stock`
--
ALTER TABLE `issued_stock`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `packages`
--
ALTER TABLE `packages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `serial_keys`
--
ALTER TABLE `serial_keys`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `user_info`
--
ALTER TABLE `user_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `issued_stock`
--
ALTER TABLE `issued_stock`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `packages`
--
ALTER TABLE `packages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `serial_keys`
--
ALTER TABLE `serial_keys`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
--
-- AUTO_INCREMENT for table `user_info`
--
ALTER TABLE `user_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
