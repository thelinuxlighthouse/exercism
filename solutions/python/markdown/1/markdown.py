from markdown import markdown


def parse(text):
    lines = text.split('\n')
    res = ''
    for line in lines:
        res += markdown(line)

    return res
