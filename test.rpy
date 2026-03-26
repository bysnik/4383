# tests.rpy

python early:
    # Вспомогательная функция для автоматического выбора в меню (если понадобится)
    def handle_choices():
        if renpy.get_screen("choice"):
            renpy.run(renpy.ui.action("choice1"))
            return True
        return False

testsuite global:
    setup:
        $ _test.timeout = 300.0          # 5 минут на прохождение
        $ _test.maximum_framerate = True
        $ _test.transition_timeout = 0.5

    testcase full_game:
        # Начинаем игру с метки start (без клика по "Start", так как игра может стартовать сразу)
        run Jump("start")
        #if screen "main_menu":
        #    click "Start"
        # Проходим все диалоги (4000 кликов должно хватить для всех пяти частей)
        advance repeat 4000

        # Дополнительная проверка: делаем скриншот финального экрана (если нужно)
        #screenshot "final_screen.png"

    testcase assets_check:
        run Jump("start")
        advance repeat 10
        exit
