def commands(number):
    secret_handshakes = {
        1: "wink",
        2: "double blink",
        4: "close your eyes",
        8: "jump",
    }

    handshakes = [secret_handshakes[k] for k in secret_handshakes if number & k]
    return handshakes[::-1] if number & 16 else handshakes
