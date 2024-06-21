input.onButtonPressed(Button.A, function () {
    radio.sendString("\"hola què tal?")
    basic.showString("\"Missatge enviat!\"")
})
radio.onReceivedString(function (receivedString) {
    basic.showString("\"hola què tal?\"")
})
basic.forever(function () {
	
})
