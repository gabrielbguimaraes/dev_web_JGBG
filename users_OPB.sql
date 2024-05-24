CREATE DATABASE IF NOT EXISTS registro_onepiece;

USE registro_onepiece;

CREATE TABLE IF NOT EXISTS users_opb (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);
