# roman alphabet을 classical Greek로 convert해주는 프로그램을 stremlit으로 구현

import re
import streamlit as st
import random
import json

# dict : greek_dict_multi_letter
with open('greek_dict_multi_letter.json', 'r', encoding='utf-8') as f:
    greek_dict_multi_letter = json.load(f)

# dict : greek_dict_accent
with open('greek_dict_accent.json', 'r', encoding='utf-8') as f:
    greek_dict_accent = json.load(f)

# dict : greek_dict_one_letter
with open('greek_dict_one_letter.json', 'r', encoding='utf-8') as f:  
    greek_dict_one_letter = json.load(f)

# list : te_and_pote
with open('te_and_pote.json', 'r', encoding='utf-8') as f:
    te_and_pote = json.load(f)

# list : ugaritic_conversion_list
with open('ugaritic_conversion_list.json', 'r', encoding='utf-8') as f:
    ugaritic_conversion_list = json.load(f) 

# dict : latin_dict 
with open('latin_dict.json', 'r', encoding='utf-8') as f: 
    latin_dict = json.load(f)

# list : try_these
with open('try_these.json', 'r', encoding='utf-8') as f:
    try_these = json.load(f)


# final sigma 문제를 regex로 처리하는 함수
# convert_to_greek 함수를 실행하기 앞서 먼저 처리되어야 한다.
def final_sigma(text):
    return re.sub(r's\b(?!\')', 'ς', text)

# breating을 auto-convert하는 함수
def convert_breathing(text):
    pattern = r'((^|[\s"\'`])(ai|au|ei|ou|eu|oi|ui|yi|a|e|i|o|u|y))'
    return re.sub(pattern, lambda match: f'{match[1]})', text, flags=re.I)

# apostrophe를 accent로 인식하는 함수
def apostrophe_to_accent(text):
    # 정규 표현식을 사용하여 모음 뒤의 '를 /로 대체합니다.
    return re.sub(r'([aeiouy]|a-|e-|o-|a=|e=|o=|a^|e^|o^|a~|e~|o~)\'', r'\1/', text, flags=re.IGNORECASE)

# accent를 auto-convert하는 함수
def find_last_vowel(word):
    pattern = r'([aeiouy](?!.*[aeiouy])[^aeiouy]*)$'
    match = re.search(pattern, word)
    if match:
        return match.group(1)
    return None

def replace_slash(vowel):
    if vowel:
        return vowel.replace('/', '\\')
    return None

def find_te_and_pote(next_word):
    if next_word and next_word.strip() in te_and_pote:
        return True
    return False

def accent_automation(text):
    lines = text.split('\n')
    accented_lines = []
    for line in lines:
        words = re.split(r'(\s+)', line)
        accented_words = []
        for i, word in enumerate(words):
            if re.match(r'^\s+$', word):
                accented_words.append(word)
            else:
                # 다음 단어를 가져오기
                next_word = words[i + 2] if i + 2 < len(words) else None
                
                # 문장 끝 단어인지 체크
                is_sentence_end = (i == len(words) - 1)
                # 문장 구분자 앞 단어인지 체크
                is_before_punctuation = bool(re.search(r'[\n\r,.:?\'\"]', word))

                if is_sentence_end or is_before_punctuation or find_te_and_pote(next_word):
                    accented_words.append(word)
                else:
                    last_vowel = find_last_vowel(word)
                    if last_vowel:
                        accented_vowel = replace_slash(last_vowel)
                        accented_word = word.replace(last_vowel, accented_vowel)
                        accented_words.append(accented_word)
                    else:
                        accented_words.append(word)
        accented_lines.append(''.join(accented_words))
    return '\n'.join(accented_lines)

# 먼저 greek_dict_multi_letter를 적용하여, key값을 value값으로 바꿔준다.
# 그 다음 greek_dict_accent를 적용하여, key값을 value값으로 바꿔준다.
# 마지막으로 greek_dict_one_letter를 적용하여, key값을 value값으로 바꿔준다.
def convert_to_greek(text):
    for key, value in greek_dict_multi_letter.items():
        text = text.replace(key, value)
    for key, value in greek_dict_accent.items():
        text = text.replace(key, value)
    for key, value in greek_dict_one_letter.items():
        text = text.replace(key, value)
    return text

# Ugaritic
def convert_to_ugaritic(text, conversion_list):
    output1 = ""
    output2 = ""
    i = 0
    while i < len(text):
        replaced = False
        for conversion in conversion_list:
            if text[i:i+len(conversion[0])] == conversion[0]:
                output1 += conversion[1]
                output2 += conversion[2]
                i += len(conversion[0])
                replaced = True
                break
        if not replaced:
            output1 += text[i]
            output2 += text[i]
            i += 1
    return output1, output2

# Latin
def convert_to_latin(text):
    for key, value in latin_dict.items():
        text = text.replace(key, value)
    return text

# 범례 설명을 출력하는 함수
def try_this():
    random_string = random.choice(try_these)
    st.write(f"*Try this: {random_string}*")

## main 함수
def main():
    st.title("scribo 0.01")

    text = st.text_area("Enter Roman Alphabet *(Kim Tae, 2024)*")
    try_this()
    converter_choice = st.radio("Choose your converter", ("Classical Greek", "Ugaritic", "Latin"))

    if st.button("Convert"):
        if converter_choice == "Classical Greek":
            text = apostrophe_to_accent(text)
            text = accent_automation(text)
            text = convert_breathing(text)
            text = final_sigma(text)
            converted_text = convert_to_greek(text)
            st.text_area("Converted Text (Unicode)", converted_text)
        if converter_choice == "Ugaritic":
            converted_text1, converted_text2 = convert_to_ugaritic(text, ugaritic_conversion_list)
            st.text_area("Converted Text 1", converted_text1)
            st.text_area("Converted Text 2", converted_text2)
        if converter_choice == "Latin":
            converted_text = convert_to_latin(text)
            st.text_area("Converted Text", converted_text)

    link = st.link_button("김태의 古典페이지", url="https://kimtaeclassics.oopy.io/")

if __name__ == "__main__":
    main()

# 이제 streamlit run classicalgreek.py를 실행하면, 웹페이지가 열리고, 
# Roman Alphabet을 입력하면 Classical Greek로 변환된 결과가 나온다.
