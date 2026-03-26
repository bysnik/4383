#!/bin/bash

# Если переменная окружения RENPY не задана, пытаемся найти renpy в PATH
if [ -z "$RENPY" ]; then
    if command -v renpy &> /dev/null; then
        RENPY="renpy"
    else
        echo "Ошибка: переменная RENPY не задана и renpy не найден в PATH." >&2
        exit 1
    fi
fi

echo "Используется Ren'Py: $RENPY"

GAME_DIR="${1:-..}"               # Путь к папке игры (первый аргумент или текущая)
TEST_SUITE="${2:-my_tests}"       # Имя тестового набора (второй аргумент или my_tests)

if ! command -v "$RENPY" &> /dev/null; then
    echo -e "\033[0;31mОшибка: команда '$RENPY' не найдена.\033[0m"
    echo "Установите Ren'Py или укажите путь через переменную RENPY."
    exit 1
fi

if [ ! -d "$GAME_DIR" ]; then
    echo -e "\033[0;31mОшибка: папка игры '$GAME_DIR' не существует.\033[0m"
    exit 1
fi

echo "Запуск тестов для игры в $GAME_DIR (набор: $TEST_SUITE)..."
"$RENPY" "$GAME_DIR" test "$TEST_SUITE" 2>&1 | tee test_output.log
EXIT_CODE=${PIPESTATUS[0]}

if [ $EXIT_CODE -ne 0 ]; then
    echo -e "\033[0;31mТесты завершились с ошибкой (код $EXIT_CODE).\033[0m"
    echo "Подробности в файле test_output.log"
    exit $EXIT_CODE
fi

if grep -qE "(Failed:|XPassed:)" test_output.log; then
    echo -e "\033[0;31mОбнаружены неудачные тесты. Проверьте test_output.log.\033[0m"
    exit 1
fi

echo -e "\033[0;32mВсе тесты успешно пройдены!\033[0m"
exit 0