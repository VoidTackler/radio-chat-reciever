def on_button_pressed_a():
    radio.send_number(0)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)