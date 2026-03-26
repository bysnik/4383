# tests.rpy
python early:
    def handle_choices():
        if renpy.get_screen("choice"):
            renpy.run(renpy.ui.action("choice1"))
            return True
        return False

testsuite my_tests:
    setup:
        $ _test.timeout = 600.0          # 10 минут на весь тест
        $ _test.maximum_framerate = True
        $ _test.transition_timeout = 0.1 # минимальные переходы
        $ _test.force = True

    testcase full_game:
        run Jump("start")
        if screen "main_menu":
            click "Start"
        # Включаем быстрый пропуск, но не ждём его завершения
        skip
        # Ждём, пока игра достигнет метки конца
        until label "end_of_game" timeout 300
        screenshot "final_screen.png"
        exit

    testcase assets_check:
        run Jump("start")
        advance repeat 10
        exit