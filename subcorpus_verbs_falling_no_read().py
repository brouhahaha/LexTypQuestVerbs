# -*- coding: cp1251 -*-
#import codecs

verbs = 'падать, упасть, выпасть, опасть, завалиться, повалиться, отвалиться, обвалиться, сорваться, отскочить, соскочить, рухнуть, обрушиться, сыпаться, высыпаться, осыпаться, шлепнуться, грохнуться, шмякнуться, брякнуться, бултыхнуться, плюхнуться'
list_verbs = verbs.split(', ')

target_verbs = ['\t'+verb for verb in list_verbs]

current_sentence = ''

with open('ruwac-filtered_part.out') as f:
    for line in f:
        try:
            if 'SENT' in line:
                current_sentence +='\n\n'
                if any(verb in current_sentence for verb in target_verbs):
                    with open('subcorpus_falling.txt', 'a') as file:
                        file.write(current_sentence)
                current_sentence = ''
            else:
                current_sentence += line
        except UnicodeDecodeError:
            continue

