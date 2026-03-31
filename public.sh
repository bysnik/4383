#!/bin/bash
# Скрипт для публикации собранной web-версии в ветку "game"

set -e  # выход при ошибке

# Запоминаем текущую ветку
current_branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "detached")

echo "Текущая ветка: $current_branch"

# Определяем путь к собранному web-проекту
# Ищем каталог вида testproject-*-dists/testproject-*-web относительно корня игры
web_build_dir=$(ls -d ../../testproject-*-dists/testproject-*-web 2>/dev/null | head -n1)

if [ -z "$web_build_dir" ]; then
    echo "Ошибка: не найден каталог с web-сборкой по шаблону ../../testproject-*-dists/testproject-*-web"
    exit 1
fi

echo "Найдена сборка: $web_build_dir"

# Убедимся, что ветка game существует (если нет, создадим от пустого коммита)
if ! git rev-parse --verify game >/dev/null 2>&1; then
    echo "Ветка game не существует. Создаём..."
    git checkout --orphan game
    git rm -rf . >/dev/null 2>&1
    git commit --allow-empty -m "Initial commit for game branch"
    git checkout "$current_branch"
fi

# Сохраняем изменения, если есть несохранённые
if ! git diff --quiet; then
    echo "Обнаружены незакоммиченные изменения. Создаём временный коммит..."
    git stash push -m "auto-stash before game branch update"
    stash_created=true
else
    stash_created=false
fi

# Переключаемся на ветку game
#git checkout game - запомнили, игра не работает в вебе с lfs

# Очищаем всё, кроме .git
git rm -rf . >/dev/null 2>&1 || true
find . -mindepth 1 -not -path "./.git*" -delete

# Копируем файлы сборки
cp -r "$web_build_dir"/* .

git lfs track game.zip

# Добавляем все файлы
git add .

# Проверяем, есть ли изменения
if git diff --cached --quiet; then
    echo "Нет изменений для коммита."
else
    git commit -m "Update web build"
fi

# Пушим в origin
git push origin game

# Возвращаемся на исходную ветку
git checkout "$current_branch"

# Восстанавливаем stash, если был
if [ "$stash_created" = true ]; then
    git stash pop
fi

echo "Готово! Ветка game обновлена и запущена."
