-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2022 at 09:25 AM
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
-- Table structure for table `physics_lab_1_work_list`
--

CREATE TABLE `physics_lab_1_work_list` (
  `id` int(11) NOT NULL,
  `work_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `physics_lab_1_work_list`
--

INSERT INTO `physics_lab_1_work_list` (`id`, `work_name`) VALUES
(1, 'آزمایش شماره 1(اندازه گیری)'),
(10, 'آزمایش شماره 10'),
(2, 'آزمایش شماره 2(قانون ارشمیدس و عکس العمل زمان)'),
(3, 'آزمایش شماره 3(اصطکاک)'),
(4, 'آزمایش شماره 4(سرعت و شتاب)'),
(5, 'آزمایش شماره 5(خط کش تعادل و میز نیرو)'),
(6, 'آزمایش شماره 6(حرکت پرتابی)'),
(7, 'آزمایش شماره 7(آونگ کاتر)'),
(8, 'آزمایش شماره 8(برخورد جداول 1تا6)'),
(9, 'آزمایش شماره 9');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `physics_lab_1_work_list`
--
ALTER TABLE `physics_lab_1_work_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `work_name` (`work_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `physics_lab_1_work_list`
--
ALTER TABLE `physics_lab_1_work_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
