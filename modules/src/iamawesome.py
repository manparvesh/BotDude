import random
from templates.text import TextTemplate


def process(input):
    iamawesome = [
        'I know! I\'m pretty cool!',
        'I know! B-)',
        'I know! I\'m awesome!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(iamawesome)).get_message(),
        'success': True
    }
    return output
