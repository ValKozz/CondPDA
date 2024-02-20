from tika import parser
from gtts import gTTS
import sys

DESC = '''Usage:
        conpda [pdf file] [output name]'''

try:
    FN_ARG = sys.argv[1]
    OUT_ARG = sys.argv[2]
except IndexError:
    print('Missing arguments!')
    print(DESC)
    exit(code=1)


def convert():
    print('Converting...')
    try:
        raw = parser.from_file(FN_ARG)
    except FileNotFoundError:
        print('File not found!')
        print(DESC)
        exit(1)

    name = OUT_ARG

    if name[-4] != 'mp3':
        name += '.mp3'
    tts = gTTS(raw['content'])

    try:
        tts.save(name)
    except FileNotFoundError:
        print(f'Cannot save to {OUT_ARG}. Does the directory exist?')
        print(DESC)
        exit(1)
    print(f'Done! File save as {name}')

convert()
