-- Création de la base de données
CREATE DATABASE IF NOT EXISTS mydiscord;

-- Utilisation de la base de données
USE mydiscord;

-- Table pour stocker les utilisateurs
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);