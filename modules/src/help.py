from templates.text import TextTemplate


def process(input):
    help = '''Hi there! I'm Dude! \n
    I'm cool and fun.'''
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
