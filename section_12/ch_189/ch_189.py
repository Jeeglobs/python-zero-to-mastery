# EXERCISE: TRANSLATOR
# translate exercise.txt into Japanese

from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('section_12/ch_189/exercise.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('section_12/ch_189/exercise_ja.txt', mode='w') as my_file_2:
            my_file_2.write(translation)
except FileNotFoundError as err:
    print('check filepath')
    raise err
