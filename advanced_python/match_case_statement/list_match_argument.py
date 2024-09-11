def greetings(details: str):
    match details:
        case[time, name]: return f'Good {time} {name}!'
        case [time, *names]:
            msg = ''
            for name in names:
                msg += f'Good {time} {name}!\n'
            return msg

print (greetings(["Evening", "Sillians", "George", "Alfred"]))