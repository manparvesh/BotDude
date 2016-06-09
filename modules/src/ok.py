from templates.text import TextTemplate


def process(input):
    ok = 'Yo'
    output = {
        'input': input,
        'output': TextTemplate(ok).get_message(),
        'success': True
    }
    return output
