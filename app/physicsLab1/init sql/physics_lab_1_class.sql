-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 12, 2022 at 08:30 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `engy`
--

-- --------------------------------------------------------

--
-- Table structure for table `physics_lab_1_class`
--

CREATE TABLE `physics_lab_1_class` (
  `id` int(11) NOT NULL,
  `class_name` varchar(50) DEFAULT NULL,
  `class_day` varchar(50) DEFAULT NULL,
  `class_time` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `physics_lab_1_class`
--

INSERT INTO `physics_lab_1_class` (`id`, `class_name`, `class_day`, `class_time`) VALUES
(1, 'آزمایشگاه فیزیک 1 گروه 1', 'شنبه', '08:00 - 10:00'),
(2, 'آزمایشگاه فیزیک 1 گروه 2', 'شنبه', '10:00 - 12:00'),
(3, 'آزمایشگاه فیزیک 1 گروه 7', 'یک شنبه', '13:30 - 15:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `physics_lab_1_class`
--
ALTER TABLE `physics_lab_1_class`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `class_name` (`class_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `physics_lab_1_class`
--
ALTER TABLE `physics_lab_1_class`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
