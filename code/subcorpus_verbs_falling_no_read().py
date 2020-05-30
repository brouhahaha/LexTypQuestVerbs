# -*- coding: cp1251 -*-
#import codecs

verbs = 'ïàäàòü, óïàñòü, âûïàñòü, îïàñòü, çàâàëèòüñÿ, ïîâàëèòüñÿ, îòâàëèòüñÿ, îáâàëèòüñÿ, ñîðâàòüñÿ, îòñêî÷èòü, ñîñêî÷èòü, ðóõíóòü, îáðóøèòüñÿ, ñûïàòüñÿ, âûñûïàòüñÿ, îñûïàòüñÿ, øëåïíóòüñÿ, ãðîõíóòüñÿ, øìÿêíóòüñÿ, áðÿêíóòüñÿ, áóëòûõíóòüñÿ, ïëþõíóòüñÿ'
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

