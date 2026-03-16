-- Создаем базу данных (если еще нет)
CREATE DATABASE IF NOT EXISTS JWC;
USE JWC;

-- Таблица пользователей (предположительно)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для курсов
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INT,
    room_id INT,
    course_time VARCHAR(100)
);

-- Таблица для аудиторий
CREATE TABLE IF NOT EXISTS rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    capacity INT
);

-- Добавляем тестового пользователя
INSERT INTO users (username, password, role) VALUES 
('admin', 'admin123', 'ADMIN'),
('teacher1', 'teacher123', 'TEACHER');

-- Добавляем тестовые аудитории
INSERT INTO rooms (name, capacity) VALUES 
('Аудитория 101', 30),
('Аудитория 102', 25);