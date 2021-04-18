"""Напишите функцию normalize, которая:

Проводит транслитерацию кириллического алфавита на латинский.
Заменяет все символы кроме латинских букв, цифр на '_'.

принимает на вход строку и возвращает строку;
проводит транслитерацию кириллических символов на латиницу;
заменяет все символы кроме букв латинского алфавита и цифр на символ '_';
транслитерация может не соответствовать стандарту, но быть читабельной;
большие буквы остаются большими, а меленькие -- маленькими после транслитерации.
"""

import re

def transliterate(text):
    dictionary = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяїіґАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЇІҐ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaiigABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUAIIG")

    raw_result = {ord(i):ord(k) for i, k in zip(*dictionary)} #маппинг 
    latin = text.translate(raw_result) #Возвращение строки с латинскими символами

    onlyalpha_latin = re.sub(r'[^\w\s]', '_', latin) #исключение всего, кроме пробелов и alphanum
    onlyalpha_latin = re.sub(r'[^\D]', '_', onlyalpha_latin) #исключение цифр и оставшихся знаков
    print(type(onlyalpha_latin))
    print(onlyalpha_latin)
    return onlyalpha_latin

transliterate('''АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьъыэюя   1234567890   !"№;%:?*()_+!@#$%^&*()_+\/*-+./.,qwertyuiop[]asdfghjkl;'\zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?''')


#Или можно написать более растянуто, но в этом случае удобнее изменять таблицу и более точно передать звук + дальнейшая доработка

Table={'А': 'A', 'а': 'a',
'Б': 'B', 'б': 'b',
'В': 'V', 'в': 'v',
'Г': 'G', 'г': 'g',
'Д': 'D', 'д': 'd',
'Е': 'E', 'е': 'e',
'Ё': 'Io', 'ё': 'io',
'Ж': 'Zh', 'ж': 'zh',
'З': 'Z', 'з': 'z',
'И': 'I', 'и': 'i',
'Й': 'J', 'й': 'j',
'К': 'K', 'к': 'k',
'Л': 'L', 'л': 'l',
'М': 'M', 'м': 'm',
'Н': 'N', 'н': 'n',
'О': 'O', 'о': 'o',
'П': 'P', 'п': 'p',
'Р': 'R', 'р': 'r',
'С': 'S', 'с': 's',
'Т': 'T', 'т': 't',
'У': 'U', 'у': 'u',
'Ф': 'F', 'ф': 'f',
'Х': 'Kh', 'х': 'kh',
'Ц': 'Ts', 'ц': 'ts',
'Ч': 'Ch', 'ч': 'ch',
'Ш': 'Sh', 'ш': 'sh',
'Щ': 'Shch', 'щ': 'shch',
'Ь': "'", 'ь': "'",
'Ы': 'Y', 'ы': 'y',
'Ъ': "", 'ъ': "",
'Э': 'E', 'э': 'e',
'Ю': 'Iu', 'ю': 'iu',
'Я': 'Ia', 'я': 'ia',
'Ї': 'Ji', 'ї': 'ji',
'І': 'I', 'і': 'i',
'Ґ': 'G', 'ґ': 'g'}

def transliterate(text, translit_table=Table):
    latin = ''
    for char in text:
        transchar = ''
        if char in translit_table:
            transchar = translit_table[char]
        elif char.isalpha():
            transchar = char
        else:
            transchar = '_'
        latin += transchar
    print("------------------------------------------")
    print(type(latin))
    return latin

transliterate('''АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьъыэюя   1234567890   !"№;%:?*()_+!@#$%^&*()_+\/*-+./.,qwertyuiop[]asdfghjkl;'\zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?''')
