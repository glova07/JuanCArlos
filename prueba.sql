-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-10-2023 a las 03:00:27
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `nombres` varchar(32) NOT NULL,
  `apellidos` varchar(32) NOT NULL,
  `tipo_documento` varchar(4) NOT NULL,
  `documento` varchar(15) NOT NULL,
  `genero` varchar(3) NOT NULL,
  `celular` varchar(10) NOT NULL,
  `correo` varchar(30) NOT NULL,
  `contra` int(128) NOT NULL,
  `fecha_nac` date NOT NULL,
  `creado` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`nombres`, `apellidos`, `tipo_documento`, `documento`, `genero`, `celular`, `correo`, `contra`, `fecha_nac`, `creado`) VALUES
('harold', 'garcia', 'C.C.', '1006229754', 'M', '3148978222', 'haroldgarciague@gmail.com', 123456789, '2003-08-26', '2023-10-11 19:55:29');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
