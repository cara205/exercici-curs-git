def on_button_pressed_a():
    radio.send_string("\"hola què tal?")
    basic.show_string("\"Missatge enviat!\"")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string("\"hola què tal?\"")
radio.on_received_string(on_received_string)

def on_forever():
    pass
basic.forever(on_forever)
