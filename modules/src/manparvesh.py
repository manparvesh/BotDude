import random
from templates.text import TextTemplate


def process(input):
    manparvesh = [
        'Never met him, but heard he\'s a super cool and awesome dude!',
        'He\'s awesome, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(manparvesh)).get_message(),
        'success': True
    }
    return output
