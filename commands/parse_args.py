

def parse_args(command_name, text):
    query = text.replace(command_name, '').strip().split()
    args = {}

    i = 0
    while i < len(query):
        arg = query[i]
        if arg.startswith('-'):
            if i + 1 < len(query) and not query[i + 1].startswith('-'):
                args[arg] = query[i + 1]
                i += 2
            else:
                args[arg] = True
                i += 1
        else:
            i += 1

    return args
