-- Создаём базу данных для n8n
CREATE DATABASE n8n;

-- Даём пользователю oncall полные права на эту базу
GRANT ALL PRIVILEGES ON DATABASE n8n TO oncall;

-- Разрешаем пользователю самостоятельно создавать базы (на будущее)
ALTER USER oncall CREATEDB;