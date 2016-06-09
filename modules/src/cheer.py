import random
from templates.text import TextTemplate


def process(input):
    cheer = [
        'Yayy!',
        'Whoohoo!',
        'Wow! You are a cheerful one!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(cheer)).get_message(),
        'success': True
    }
    return output
