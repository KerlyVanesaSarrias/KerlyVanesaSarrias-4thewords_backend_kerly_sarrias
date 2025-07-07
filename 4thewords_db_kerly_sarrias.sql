-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 07-07-2025 a las 13:40:29
-- Versión del servidor: 11.5.2-MariaDB
-- Versión de PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `4thewords_db_kerly_sarrias`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `canton`
--

DROP TABLE IF EXISTS `canton`;
CREATE TABLE IF NOT EXISTS `canton` (
  `id` char(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `province_id` char(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `province_id` (`province_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `canton`
--

INSERT INTO `canton` (`id`, `name`, `province_id`) VALUES
('1d05c04a-6055-4978-a972-0e8962a1f86a', 'San josé central', '67747756-15dd-49b8-a34b-9f0a38d4705d'),
('853e4e03-dd49-40b4-9b41-c7ae2749cfd2', 'Desamparados', '67747756-15dd-49b8-a34b-9f0a38d4705d'),
('270bc31a-1747-4ca5-96d9-b3aff2916064', 'Puriscal', '67747756-15dd-49b8-a34b-9f0a38d4705d'),
('2505a64c-fc87-4210-8b82-7112dcfa6b2b', 'Alajuala', 'af940357-9768-43f8-a33f-602a6b70917c'),
('32f7b442-4afa-42e4-a991-87a1c3fd8a6e', 'San ramón', 'af940357-9768-43f8-a33f-602a6b70917c'),
('37df5422-5ed1-4766-89cd-f2e24adde115', 'Grecia', 'af940357-9768-43f8-a33f-602a6b70917c');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id` char(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
('d154b23a-87c6-4a43-bcb1-96fe7cd56cb1', 'Leyenda mítica'),
('e5120a2c-2c98-4f9e-a3e2-f882f1a093cb', 'Leyenda urbana'),
('f129ed13-bc79-496b-85c3-9a8e8d7b85d6', 'Leyenda histórica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `district`
--

DROP TABLE IF EXISTS `district`;
CREATE TABLE IF NOT EXISTS `district` (
  `id` char(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `canton_id` char(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `canton_id` (`canton_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `district`
--

INSERT INTO `district` (`id`, `name`, `canton_id`) VALUES
('9e0e5eb4-e99f-4d69-9ab3-7ee348f90e94', 'San juan de Dios', '853e4e03-dd49-40b4-9b41-c7ae2749cfd2'),
('66fee857-67dc-4576-85dc-d3d3dbda42b5', 'San miguel', '853e4e03-dd49-40b4-9b41-c7ae2749cfd2'),
('1c916463-d007-4c20-9180-4551fe964e60', 'Damas', '853e4e03-dd49-40b4-9b41-c7ae2749cfd2'),
('082a24ff-e462-421d-8e2d-243486622d30', 'Rosario', '853e4e03-dd49-40b4-9b41-c7ae2749cfd2'),
('bae8de3c-0e4a-4a0b-9c3e-21c1de5b85b3', 'Carmen', '1d05c04a-6055-4978-a972-0e8962a1f86a'),
('9c1e489b-fabb-46f6-a83b-040c5a74e05e', 'Catedral', '1d05c04a-6055-4978-a972-0e8962a1f86a'),
('bb9fd57f-00bf-45dd-b9a7-367096889fb7', 'Santiago', '270bc31a-1747-4ca5-96d9-b3aff2916064'),
('37e397eb-ed2a-47c3-9779-e86cb805f1d5', 'Mercedes Sur', '270bc31a-1747-4ca5-96d9-b3aff2916064'),
('c9820b2b-fed4-4a6c-9ca4-da2845a2c489', 'Barbacoas', '270bc31a-1747-4ca5-96d9-b3aff2916064'),
('9393fb4c-66ec-4484-b51a-246a96439a3f', 'Alajuela centro', '2505a64c-fc87-4210-8b82-7112dcfa6b2b'),
('38fd620e-0428-4d91-9577-a7f5c42c2c82', 'San josé', '2505a64c-fc87-4210-8b82-7112dcfa6b2b'),
('7274cdc8-d6be-4e64-b2c8-6b389187e633', 'Carrizal', '2505a64c-fc87-4210-8b82-7112dcfa6b2b'),
('ff1d6f45-481b-4688-beb1-c1e0846f8517', 'San ramon centro', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e'),
('8c6bd908-34ad-49e5-b7ee-e757d229041b', 'Santiago', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e'),
('3c757121-cbd8-4283-bb8b-caa298daa04d', 'San juan', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e'),
('7099a95e-d2ec-48cb-bc78-2f228ddd6c80', 'Grecia centro', '37df5422-5ed1-4766-89cd-f2e24adde115'),
('0f66e972-3941-4dd5-9798-207e33f52c58', 'San isidro', '37df5422-5ed1-4766-89cd-f2e24adde115'),
('09d54b69-f312-4536-8c27-0f2adbadc926', 'San roque', '37df5422-5ed1-4766-89cd-f2e24adde115');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `legend`
--

DROP TABLE IF EXISTS `legend`;
CREATE TABLE IF NOT EXISTS `legend` (
  `id` varchar(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `legend_date` date NOT NULL,
  `category_id` varchar(36) NOT NULL,
  `province_id` varchar(36) NOT NULL,
  `canton_id` varchar(36) NOT NULL,
  `district_id` varchar(36) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_legend_canton_id` (`canton_id`),
  KEY `ix_legend_category_id` (`category_id`),
  KEY `ix_legend_district_id` (`district_id`),
  KEY `ix_legend_province_id` (`province_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `legend`
--

INSERT INTO `legend` (`id`, `name`, `description`, `image_url`, `legend_date`, `category_id`, `province_id`, `canton_id`, `district_id`) VALUES
('cec92d8a-fde7-4c0b-9880-fc91b9421bdc', 'La Tulevieja', 'Leyenda mítica de una mujer con alas de murciélago y patas de cabra', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751873455/legends_images/f9a8cdb9-7001-4bc3-ad2b-a7a074c9ee45.png', '1890-05-12', 'e5120a2c-2c98-4f9e-a3e2-f882f1a093cb', '67747756-15dd-49b8-a34b-9f0a38d4705d', '853e4e03-dd49-40b4-9b41-c7ae2749cfd2', '9e0e5eb4-e99f-4d69-9ab3-7ee348f90e94'),
('5a2150c0-42db-4c79-a00e-216a1edcd409', ' La Tulevieja', 'Espíritu de una mujer que murió tras perder a su hijo. Castiga a hombres mujeriegos y cuida a los niños perdidos.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751894928/leyendas/bbihvgcwpkiz52wfn2pe.png', '1993-01-07', 'd154b23a-87c6-4a43-bcb1-96fe7cd56cb1', 'af940357-9768-43f8-a33f-602a6b70917c', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e', '8c6bd908-34ad-49e5-b7ee-e757d229041b'),
('99f5c470-baf4-48a1-bd53-f978bc189144', 'tryrtut', '3wwerw', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751867177/leyendas/ql2kcuroesttqswz79vb.png', '2025-07-01', 'f129ed13-bc79-496b-85c3-9a8e8d7b85d6', 'af940357-9768-43f8-a33f-602a6b70917c', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e', '3c757121-cbd8-4283-bb8b-caa298daa04d'),
('cd8c2535-3db8-4eb4-a25a-10dfe36dc677', 'cbhawebf', 'NC SlvSB', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751873585/legends_images/c16bf174-71a4-4a4e-b8fb-7b5effef4090.png', '2025-07-12', 'e5120a2c-2c98-4f9e-a3e2-f882f1a093cb', '67747756-15dd-49b8-a34b-9f0a38d4705d', '1d05c04a-6055-4978-a972-0e8962a1f86a', 'bae8de3c-0e4a-4a0b-9c3e-21c1de5b85b3'),
('ab013fa6-5a83-47a8-b8d9-23dcdf0edeb2', 'El Padre sin Cabeza', 'Fantasma de un sacerdote decapitado que vaga en busca de justicia o penitencia.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895004/leyendas/sdqib0bib0dvcjmiaqyu.png', '2025-07-06', 'e5120a2c-2c98-4f9e-a3e2-f882f1a093cb', 'af940357-9768-43f8-a33f-602a6b70917c', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e', 'ff1d6f45-481b-4688-beb1-c1e0846f8517'),
('7d480d7c-a6dd-4cf5-903b-79342e04007d', 'El Niño y la Caverna de la Lechuza', 'Un niño desapareció misteriosamente al entrar en una cueva donde habita una lechuza mágica.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895087/leyendas/iaxzkhuk2sdrll8jexkw.png', '1988-06-15', 'e5120a2c-2c98-4f9e-a3e2-f882f1a093cb', '67747756-15dd-49b8-a34b-9f0a38d4705d', '853e4e03-dd49-40b4-9b41-c7ae2749cfd2', '082a24ff-e462-421d-8e2d-243486622d30'),
('37bddc19-80b3-4d45-b116-2fc374b082a2', ' La Llorona', 'Mujer que llora eternamente buscando a sus hijos. Su llanto se escucha cerca de ríos o quebradas.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895186/leyendas/czlbjr3hqep4lj40iy7v.png', '1999-06-07', 'e5120a2c-2c98-4f9e-a3e2-f882f1a093cb', '67747756-15dd-49b8-a34b-9f0a38d4705d', '1d05c04a-6055-4978-a972-0e8962a1f86a', 'bae8de3c-0e4a-4a0b-9c3e-21c1de5b85b3'),
('c242688a-55bc-473b-ae7d-fbaef735f846', 'La Mona', 'Hechicera que se convierte en un simio gigante y persigue a quienes la ofenden o invaden su territorio.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895257/leyendas/k7uareoojlyht976nn1j.png', '1888-10-12', 'f129ed13-bc79-496b-85c3-9a8e8d7b85d6', 'af940357-9768-43f8-a33f-602a6b70917c', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e', '3c757121-cbd8-4283-bb8b-caa298daa04d'),
('abd4675d-5d34-4c5f-8464-59fd5b472361', 'El Tesoro del Diquís', 'Tesoro indígena protegido por espíritus y energías sobrenaturales. Muchos han intentado buscarlo sin éxito.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895337/leyendas/cijt6zkna3auoqhq8ufh.png', '1762-11-11', 'e5120a2c-2c98-4f9e-a3e2-f882f1a093cb', '67747756-15dd-49b8-a34b-9f0a38d4705d', '853e4e03-dd49-40b4-9b41-c7ae2749cfd2', '1c916463-d007-4c20-9180-4551fe964e60'),
('2725b393-ccf3-4d66-a323-3165272436c5', ' La Cegua de Turrialba', ' La Cegua de Turrialba', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895422/leyendas/ptwlk82pkeumx0be4l0r.png', '1985-03-11', 'd154b23a-87c6-4a43-bcb1-96fe7cd56cb1', 'af940357-9768-43f8-a33f-602a6b70917c', '2505a64c-fc87-4210-8b82-7112dcfa6b2b', '7274cdc8-d6be-4e64-b2c8-6b389187e633'),
('84862181-6e02-4f04-9e3b-7de6ce64fb9f', 'El Cadejos', 'Un perro fantasmal de ojos rojos que protege (o castiga) a los borrachos y caminantes nocturnos.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895504/leyendas/hqiz5sun8lvqu3kcuwjl.png', '1888-11-11', 'd154b23a-87c6-4a43-bcb1-96fe7cd56cb1', 'af940357-9768-43f8-a33f-602a6b70917c', '32f7b442-4afa-42e4-a991-87a1c3fd8a6e', '8c6bd908-34ad-49e5-b7ee-e757d229041b'),
('5a7458bb-f0f4-4906-9cd1-92700dd68962', 'La Segua', 'Mujer hermosa que se transforma en un espectro con rostro de caballo para castigar a hombres lujuriosos.', 'https://res.cloudinary.com/dc38afvjc/image/upload/v1751895585/leyendas/b0xcsx7t7uavwirw0pgh.png', '1997-11-11', 'd154b23a-87c6-4a43-bcb1-96fe7cd56cb1', 'af940357-9768-43f8-a33f-602a6b70917c', '37df5422-5ed1-4766-89cd-f2e24adde115', '0f66e972-3941-4dd5-9798-207e33f52c58');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `province`
--

DROP TABLE IF EXISTS `province`;
CREATE TABLE IF NOT EXISTS `province` (
  `id` char(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `province`
--

INSERT INTO `province` (`id`, `name`) VALUES
('67747756-15dd-49b8-a34b-9f0a38d4705d', 'San josé'),
('af940357-9768-43f8-a33f-602a6b70917c', 'Alajuala');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` varchar(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `hashed_password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`) USING HASH,
  KEY `ix_user_id` (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `hashed_password`) VALUES
('0f35e06b-cdf3-4744-9f2d-d8f8d62b0897', 'Kerly Vanessa', 'kerlysarrias011@gmail.com', '$2b$12$uEknInSKbDDl2n7bwZ8a4e8prY4U0scgf09vuXLq31/XzxdeAQBvG');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
