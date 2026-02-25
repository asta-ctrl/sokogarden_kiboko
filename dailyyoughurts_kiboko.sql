-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 25, 2026 at 06:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dailyyoughurts_kiboko`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text NOT NULL,
  `product_cost` int(11) NOT NULL,
  `product_photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Uzima', 'yummy', 135, 'animelogo2.jpg'),
(2, 'KIDS ', 'Tasty', 135, 'animelogo2.jpg'),
(3, 'Best Health Goods', 'Munchy', 140, 'animelogo2.jpg'),
(4, 'Builtbest Youghurts', 'delicacy', 135, 'animelogo2.jpg'),
(5, 'Eden', 'Tasty', 135, 'animelogo2.jpg'),
(6, 'Delamarex', 'fruitful', 140, 'animelogo2.jpg'),
(7, 'Uzima', 'yummy', 135, 'animelogo2.jpg'),
(8, 'Canaan', 'nutricious', 135, 'animelogo2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'asta', '54321', 'test1@gmail.com', '079854237'),
(2, 'asta', '54321 ', 'test1@gmail.com', '079854237'),
(3, 'asta', '54321 ', 'test1@gmail.com', '079854237'),
(4, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(5, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(6, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(7, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(8, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(9, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(10, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(11, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(12, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(13, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(14, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(15, 'asta', '54321 ', 'test1 @gmail.com', '079854237'),
(16, 'asta', '54321', 'test1@gmail.com', '079854237'),
(17, 'asta', '54321', 'test1', '079854237'),
(18, 'asta', '54321', 'test1@gmail.com', '079854237');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
