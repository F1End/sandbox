# Only python 3.10 or newer

class InvalidCommand(Exception):

    def __init__(self, message):
        print(message)

def handle_command(message):
    if  len(message) == 1 and type(message[0]) is str:
        message = [str(x) for x in message[0]]
    match message:
        case ['BEEPER', freqeuncy, times]:
            print(f"BEEP ({freqeuncy})" * times)
        case ['NECK', angle]:
            print(f"Robot turning its had {angle} degrees")
        case ['LED', brightness]:
            print(f"Light is now {brightness}")
        case ["S", "a", "y", *rest]:
            print("".join(rest))
        case [ int(a), str(order), int(b)] if order == "plus":
            print(a + b)
        case _:
            raise InvalidCommand("This is not a valid message")

cmd1 = ["BEEPER", "loud", 5]
cmd2 = ["NECK", 45]
cmd3 = ("LED", "very bright")
cmd4 = ["Say something"]
cmd5 = [5, "plus", 5]
handle_command(cmd5)


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:10.4f} | {lon:9.4f}')

main()