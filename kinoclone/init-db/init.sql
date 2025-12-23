-- Создание расширения для UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Тестовые данные
INSERT INTO content (id, title, original_title, type, year, description, duration_minutes, age_rating, poster_url, kp_rating) VALUES
(uuid_generate_v4(), 'Матрица', 'The Matrix', 'movie', 1999, 'Хакер узнает о реальности', 136, '16+', 'https://example.com/matrix.jpg', 8.5),
(uuid_generate_v4(), 'Интерстеллар', 'Interstellar', 'movie', 2014, 'Путешествие в космос', 169, '12+', 'https://example.com/interstellar.jpg', 8.6);

INSERT INTO genres (id, name, slug) VALUES
(uuid_generate_v4(), 'Боевик', 'action'),
(uuid_generate_v4(), 'Фантастика', 'sci-fi');