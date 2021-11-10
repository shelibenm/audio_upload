def on_received_string(receivedString):
    pass
radio.on_received_string(on_received_string)

def on_forever():
    radio.set_group(1)
basic.forever(on_forever)
