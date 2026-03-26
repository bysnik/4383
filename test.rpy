# tests.rpy
python early:
    def handle_choices():
        if renpy.get_screen("choice"):
            renpy.run(renpy.ui.action("choice1"))
            return True
        return False

testsuite my_tests:
    setup:
        $ _test.timeout = 600.0
        $ _test.maximum_framerate = True
        $ _test.transition_timeout = 0.1

    testcase full_game:
        run Jump("start")
        if screen "main_menu":
            click "Start"
        skip until label "end_of_game"
        exit

    testcase assets_check:
        run Jump("start")
        advance repeat 10
        exit