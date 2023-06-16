#!/bin/bash

# Збереження поточного каталогу
current_dir=$(pwd)

# Оновлення сховища
git pull --rebase

# Додавання всіх змінені файлів до індексу
git add .

# Збереження змін у коміті
timestamp=$(date +%Y-%m-%d-%H:%M:%S)
git commit -m "Sync: $timestamp"

# Відправка змін до сховища
git push

# Повернення до початкового каталогу
cd "$current_dir"

echo "Синхронізація завершена."