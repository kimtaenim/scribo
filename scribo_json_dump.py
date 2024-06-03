# Description: This script is used to dump the json file of the dictionary.
import json

# GREEK DICTIONARY
# roman alphabet이 key값, classical Greek가 value값인 dictionary 생성
greek_dict_multi_letter = {
    "CH": "Χ", "Ch": "Χ","ch": "χ",
    "KH": "Χ", "Kh": "Χ", "kh": "χ",
    "PH": "Φ", "Ph": "Φ", "ph": "φ",
    "TH": "Θ", "Th": "Θ", "th": "θ",
    "PS": "Ψ", "Ps": "Ψ", "ps": "ψ",
    "UI": "ΥΙ", "Ui": "ΥΙ", "ui": "υι",
    "NG": "ΓΓ", "ng": "γγ",
    "nkh": "γχ", "nch": "γχ",  
    "NK": "ΓΚ", "nk": "γκ",
    "NX": "ΓΞ", "nx": "γξ",
}

with open('greek_dict_multi_letter.json', 'w', encoding='utf-8') as f:
    json.dump(greek_dict_multi_letter, f, ensure_ascii=False, indent=4)

greek_dict_accent = {
    # mostly confused vowels
        "i)a" : "ἰα", # ἰα

    # breathings and long vowels (iota subscripts) "A"
        "a)|" : "ᾀ", "a).i" : "ᾀ", "a)-i" : "ᾀ",
        "a))|" : "ᾀ", "a)).i" : "ᾀ", "a))-i" : "ᾀ", 
            ")a|" : "ᾀ", ")a.i": "ᾀ", ")a-i": "ᾀ", # ᾀ
        "a(|" : "ᾁ", "a(|.i": "ᾁ", "a(-i": "ᾁ",
            "(a|" : "ᾁ", "(a.i": "ᾁ", "(a-i": "ᾁ",
            "ha|" : "ᾁ", "ha.i": "ᾁ", "ha-i": "ᾁ", # ᾁ
        "a)\\|" : "ᾂ", "a)\\.i": "ᾂ", "a)-\\i": "ᾂ",
        "a))\\|" : "ᾂ", "a))\\.i": "ᾂ", "a))-\\i": "ᾂ",
            ")a\\|" : "ᾂ", ")a\\.i": "ᾂ", ")a-\\i": "ᾂ", # ᾂ
        "a(/|" : "ᾃ", "a(/.i": "ᾃ", "a(-.i": "ᾃ",
            "(a/|" : "ᾃ", "(a/.i": "ᾃ", "(a-.i": "ᾃ",
            "ha/|" : "ᾃ", "ha/.i": "ᾃ", "ha-.i": "ᾃ", # ᾃ
        "a)/|" : "ᾄ", "a)/.i": "ᾄ", "a)/-i": "ᾄ",
        "a))/|" : "ᾄ", "a))/.i": "ᾄ", "a))/-i": "ᾄ",
            ")a/|" : "ᾄ", ")a/.i": "ᾄ", ")a/-i": "ᾄ", # ᾄ
        "a(/|" : "ᾅ", "a(/.i": "ᾅ", "a(/-i": "ᾅ",
            "(a/|" : "ᾅ", "(a/.i": "ᾅ", "(a/-i": "ᾅ",
            "ha/|" : "ᾅ", "ha/.i": "ᾅ", "ha/-i": "ᾅ", # ᾅ
        "a)=|" : "ᾆ", "a)=.i" : "ᾆ", "a)=-i" : "ᾆ",
            "a))=|" : "ᾆ", "a))=.i" : "ᾆ", "a))=-i" : "ᾆ",
            ")a=|" : "ᾆ", ")a=.i" : "ᾆ", ")a=-i" : "ᾆ", 
            "a)^|" : "ᾆ", "a)^.i" : "ᾆ", "a)^-i" : "ᾆ", 
            "a))^|" : "ᾆ", "a))^.i" : "ᾆ", "a))^-i" : "ᾆ", 
            ")a^|" : "ᾆ", ")a^.i" : "ᾆ", ")a^-i" : "ᾆ", 
            "a)~|" : "ᾆ", "a)~.i" : "ᾆ", "a)~-i" : "ᾆ", 
            "a))~|" : "ᾆ", "a))~.i" : "ᾆ", "a))~-i" : "ᾆ", 
            ")a~|" : "ᾆ", ")a~.i" : "ᾆ", ")a~-i" : "ᾆ", # ᾆ
        "a(=|" : "ᾇ", "a(=.i" : "ᾇ", "a(=-i" : "ᾇ",
            "(a=|" : "ᾇ", "(a=.i" : "ᾇ", "(a=-i" : "ᾇ",
            "ha=|" : "ᾇ", "ha=.i" : "ᾇ", "ha=-i" : "ᾇ", 
            "a(^|" : "ᾆ", "a(^.i" : "ᾆ", "a(^-i" : "ᾆ", 
            "(a^|" : "ᾆ", "(a^.i" : "ᾆ", "(a^-i" : "ᾆ",
            "ha^|" : "ᾆ", "ha^.i" : "ᾆ", "ha^-i" : "ᾆ", 
            "a(~|" : "ᾆ", "a(~.i" : "ᾆ", "a(~-i" : "ᾆ",
            "(a~|" : "ᾆ", "(a~.i" : "ᾆ", "(a~-i" : "ᾆ", 
            "ha~|" : "ᾆ", "ha~.i" : "ᾆ", "ha~-i" : "ᾆ", # ᾆ        # ᾇ
        "A)|" : "ᾈ", "A).i" : "ᾈ", "A)-i" : "ᾈ", 
            ")A|" : "ᾈ", ")A.i": "ᾈ", ")A-i": "ᾈ", # ᾈ
        "A(|" : "ᾉ", "A(|.i": "ᾉ", "A(-i": "ᾉ",
            "(A|" : "ᾉ", "(A.i": "ᾉ", "(A-i": "ᾉ",
            "Ha|" : "ᾉ", "Ha.i": "ᾉ", "Ha-i": "ᾉ", # ᾉ
        "A)\\|" : "ᾊ", "A)\\.i": "ᾊ", "A)-\\i": "ᾊ",
            ")A\\|" : "ᾊ", ")A\\.i": "ᾊ", ")A-\\i": "ᾊ", # ᾊ
        "A(/|" : "ᾋ", "A(/.i": "ᾋ", "A(-.i": "ᾋ",
            "(A/|" : "ᾋ", "(A/.i": "ᾋ", "(A-.i": "ᾋ",
            "Ha/|" : "ᾋ", "Ha/.i": "ᾋ", "Ha-.i": "ᾋ", # ᾋ
        "A)/|" : "ᾌ", "A)/.i": "ᾌ", "A)/-i": "ᾌ",
            ")A/|" : "ᾌ", ")A/.i": "ᾌ", ")A/-i": "ᾌ", # ᾌ
        "A(/|" : "ᾅ", "A(/.i": "ᾅ", "A(/-i": "ᾅ",
            "(a/|" : "ᾅ", "(a/.i": "ᾅ", "(a/-i": "ᾅ",
            "Ha/|" : "ᾅ", "Ha/.i": "ᾅ", "Ha/-i": "ᾅ", # ᾍ
        "A(/|" : "ᾍ", "A(/.i": "ᾍ", "A(/-i": "ᾍ",
            "(A/|" : "ᾍ", "(A/.i": "ᾍ", "(A/-i": "ᾍ",
            "Ha/|" : "ᾍ", "Ha/.i": "ᾍ", "Ha/-i": "ᾍ", # ᾍ
        "A)=|" : "ᾎ", "A)=.i" : "ᾎ", "A)=-i" : "ᾎ",
            ")A=|" : "ᾎ", ")A=.i" : "ᾎ", ")A=-i" : "ᾎ", 
            "A)^|" : "ᾎ", "A)^.i" : "ᾎ", "A)^-i" : "ᾎ", 
            ")A^|" : "ᾎ", ")A^.i" : "ᾎ", ")A^-i" : "ᾎ", 
            "A)~|" : "ᾎ", "A)~.i" : "ᾎ", "A)~-i" : "ᾎ", 
            ")A~|" : "ᾎ", ")A~.i" : "ᾎ", ")A~-i" : "ᾎ", # ᾎ
        "A(=|" : "ᾏ", "A(=.i" : "ᾏ", "A(=-i" : "ᾏ",
            "(A=|" : "ᾏ", "(A=.i" : "ᾏ", "(A=-i" : "ᾏ",
            "Ha=|" : "ᾏ", "Ha=.i" : "ᾏ", "Ha=-i" : "ᾏ", 
            "A(^|" : "ᾏ", "A(^.i" : "ᾏ", "A(^-i" : "ᾏ", 
            "(A^|" : "ᾏ", "(A^.i" : "ᾏ", "(A^-i" : "ᾏ",
            "Ha^|" : "ᾏ", "Ha^.i" : "ᾏ", "Ha^-i" : "ᾏ", 
            "A(~|" : "ᾏ", "A(~.i" : "ᾏ", "A(~-i" : "ᾏ",
            "(A~|" : "ᾏ", "(A~.i" : "ᾏ", "(A~-i" : "ᾏ", 
            "Ha~|" : "ᾏ", "Ha~.i" : "ᾏ", "Ha~-i" : "ᾏ", # ᾏ

    # breathing and long vowels (iota subscripts) "H"
        "e-)|" : "ᾐ", "e-).i" : "ᾐ", 
            ")e-|" : "ᾐ", ")e-.i": "ᾐ",  # ᾐ
        "e-(|" : "ᾑ", "e-(|.i": "ᾑ", 
            "(e-|" : "ᾑ", "(e-.i": "ᾑ", 
            "he-|" : "ᾑ", "he-.i": "ᾑ",  # ᾑ
        "e-)\\|" : "ᾒ", "e-)\\.i": "ᾒ", 
            ")e-\\|" : "ᾒ", ")e-\\.i": "ᾒ",  # ᾒ
        "e-(/|" : "ᾓ", "e-(/.i": "ᾓ", 
            "(e-/|" : "ᾓ", "(e-/.i": "ᾓ", 
            "he-/|" : "ᾓ", "he-/.i": "ᾓ",  # ᾓ
        "e-)/|" : "ᾔ", "e-)/.i": "ᾔ", 
            ")e-/|" : "ᾔ", ")e-/.i": "ᾔ",  # ᾔ
        "e-(/|" : "ᾕ", "e-(/.i": "ᾕ", 
            "(e-/|" : "ᾕ", "(e-/.i": "ᾕ", 
            "he-/|" : "ᾕ", "he-/.i": "ᾕ",  # ᾕ
        "e-)=|" : "ᾖ", "e-)=.i" : "ᾖ", 
            ")e-=|" : "ᾖ", ")e-=.i" : "ᾖ",  
            "e-)^|" : "ᾖ", "e-)^.i" : "ᾖ",  
            ")e-^|" : "ᾖ", ")e-^.i" : "ᾖ",  
            "e-)~|" : "ᾖ", "e-)~.i" : "ᾖ",  
            ")e-~|" : "ᾖ", ")e-~.i" : "ᾖ",  # ᾖ
        "e-(=|" : "ᾗ", "e-(=.i" : "ᾗ",
            "(e-=|" : "ᾗ", "(e-=.i" : "ᾗ",
            "he-=|" : "ᾗ", "he-=.i" : "ᾗ", 
            "e-(^|" : "ᾖ", "e-(^.i" : "ᾖ",  
            "(e-^|" : "ᾖ", "(e-^.i" : "ᾖ", 
            "he-^|" : "ᾖ", "he-^.i" : "ᾖ",
            "(e-~|" : "ᾖ", "(e-~.i" : "ᾖ", 
            "he-~|" : "ᾖ", "he-~.i" : "ᾖ",    # ᾖ
        "E-)|" : "ᾘ", "E-).i" : "ᾘ",
            ")E-|" : "ᾘ", ")E-.i": "ᾘ",  # ᾘ
        "E-(|" : "ᾙ", "E-(|.i": "ᾙ",
            "(E-|" : "ᾙ", "(E-.i": "ᾙ",
            "He-|" : "ᾙ", "He-.i": "ᾙ",  # ᾙ
        "E-)\\|" : "ᾚ", "E-)\\.i": "ᾚ",
            ")E-\\|" : "ᾚ", ")E-\\.i": "ᾚ",  # ᾚ
        "E-(/|" : "ᾛ", "E-(/.i": "ᾛ",
            "(E-/|" : "ᾛ", "(E-/.i": "ᾛ",
            "He-/|" : "ᾛ", "He-/.i": "ᾛ",  # ᾛ
        "E-)/|" : "ᾜ", "E-)/.i": "ᾜ",
            ")E-/|" : "ᾜ", ")E-/.i": "ᾜ",  # ᾜ
        "E-(/|" : "ᾝ", "E-(/.i": "ᾝ",
            "(E-/|" : "ᾝ", "(E-/.i": "ᾝ",
            "He-/|" : "ᾝ", "He-/.i": "ᾝ",  # ᾝ
        "E-)=|" : "ᾞ", "E-)=.i" : "ᾞ",
            ")E-=|" : "ᾞ", ")E-=.i" : "ᾞ",  
            "E-)^|" : "ᾞ", "E-)^.i" : "ᾞ",  
            ")E-^|" : "ᾞ", ")E-^.i" : "ᾞ",  
            "E-)~|" : "ᾞ", "E-)~.i" : "ᾞ",  
            ")E-~|" : "ᾞ", ")E-~.i" : "ᾞ",  # ᾞ
        "E-(=|" : "ᾟ", "E-(=.i" : "ᾟ",
            "(E-=|" : "ᾟ", "(E-=.i" : "ᾟ",
            "He-=|" : "ᾟ", "He-=.i" : "ᾟ", 
            "E-(^|" : "ᾞ", "E-(^.i" : "ᾞ",  
            "(E-^|" : "ᾞ", "(E-^.i" : "ᾞ", 
            "He-^|" : "ᾞ", "He-^.i" : "ᾞ",  # ᾞ

    # breathings and long vowels (iota subscripts) "O-"
        "o)|" : "ᾠ", "o).i" : "ᾠ", 
            ")o|" : "ᾠ", ")o.i": "ᾠ", # ᾠ
        "o(|" : "ᾡ", "o(|.i": "ᾡ", 
            "(o|" : "ᾡ", "(o.i": "ᾡ", 
            "ho|" : "ᾡ", "ho.i": "ᾡ", # ᾡ
        "o)\\|" : "ᾢ", "o).i": "ᾢ",
            ")o\\|" : "ᾢ", ")o.i": "ᾢ", # ᾢ
        "o(/|" : "ᾣ", "o(/.i": "ᾣ",
            "(o/|" : "ᾣ", "(o/.i": "ᾣ",
            "ho/|" : "ᾣ", "ho/.i": "ᾣ", # ᾣ
        "o)/|" : "ᾤ", "o)/.i": "ᾤ",
            ")o/|" : "ᾤ", ")o/.i": "ᾤ", # ᾤ
        "o(/|" : "ᾥ", "o(/.i": "ᾥ",
            "(o/|" : "ᾥ", "(o/.i": "ᾥ",
            "ho/|" : "ᾥ", "ho/.i": "ᾥ", # ᾥ
        "o)=|" : "ᾦ", "o)=.i" : "ᾦ",
            ")o=|" : "ᾦ", ")o=.i" : "ᾦ",
            "o)^|" : "ᾦ", "o)^.i" : "ᾦ",
            ")o^|" : "ᾦ", ")o^.i" : "ᾦ",
            "o)~|" : "ᾦ", "o)~.i" : "ᾦ",
            ")o~|" : "ᾦ", ")o~.i" : "ᾦ", # ᾦ
        "o(=|" : "ᾧ", "o(=.i" : "ᾧ",
            "(o=|" : "ᾧ", "(o=.i" : "ᾧ",
            "ho=|" : "ᾧ", "ho=.i" : "ᾧ", "ho-=.i" : "ᾧ", 
            "o^|" : "ᾦ", "o^.i" : "ᾦ",
            "(o^|" : "ᾦ", "(o^.i" : "ᾦ",
            "ho^|" : "ᾦ", "ho^.i" : "ᾦ", # ᾦ
        "O)|" : "ᾨ", "O).i" : "ᾨ",
            ")O|" : "ᾨ", ")O.i": "ᾨ", # ᾨ
        "O(|" : "ᾩ", "O(|.i": "ᾩ",
            "(O|" : "ᾩ", "(O.i": "ᾩ",
            "HO|" : "ᾩ", "HO.i": "ᾩ", # ᾩ   
        "O)\\|" : "ᾪ", "O).i": "ᾪ",
            ")O\\|" : "ᾪ", ")O.i": "ᾪ", # ᾪ
        "O(/|" : "ᾫ", "O(/.i": "ᾫ",
            "(O/|" : "ᾫ", "(O/.i": "ᾫ",
            "HO/|" : "ᾫ", "HO/.i": "ᾫ", # ᾫ
        "O)/|" : "ᾬ", "O)/.i": "ᾬ",
            ")O/|" : "ᾬ", ")O/.i": "ᾬ", # ᾬ
        "O(/|" : "ᾭ", "O(/.i": "ᾭ",
            "(O/|" : "ᾭ", "(O/.i": "ᾭ",
            "HO/|" : "ᾭ", "HO/.i": "ᾭ", # ᾭ
        "O)=|" : "ᾮ", "O)=.i" : "ᾮ",
            ")O=|" : "ᾮ", ")O=.i" : "ᾮ",
            "O)^|" : "ᾮ", "O)^.i" : "ᾮ",
            ")O^|" : "ᾮ", ")O^.i" : "ᾮ",
            "O)~|" : "ᾮ", "O)~.i" : "ᾮ",
            ")O~|" : "ᾮ", ")O~.i" : "ᾮ", # ᾮ
        "O(=|" : "ᾯ", "O(=.i" : "ᾯ",
            "(O=|" : "ᾯ", "(O=.i" : "ᾯ",
            "HO=|" : "ᾯ", "HO=.i" : "ᾯ", 
            "O^|" : "ᾮ", "O^.i" : "ᾮ",
            "(O^|" : "ᾮ", "(O^.i" : "ᾮ",
            "HO^|" : "ᾮ", "HO^.i" : "ᾮ", # ᾮ

    # iota subscripts (without breathings)
        "a\\|": "ᾲ", "a\\.i": "ᾲ", "a-\\i": "ᾲ", # ᾲ
        "a|" : "ᾳ", "a.i": "ᾳ", "a-i": "ᾳ", # ᾳ
        "a/|" : "ᾴ", "a/.i": "ᾴ", "a/-.i": "ᾴ", # ᾴ
        "a^|" : "ᾷ", "a^.i": "ᾷ", "a^-i": "ᾷ",
            "a~|" : "ᾷ", "a~.i": "ᾷ", "a~-i": "ᾷ", 
            "a=|" : "ᾷ", "a=.i": "ᾷ", "a=-i": "ᾷ", # ᾷ

        "e\\|": "ῂ", "e\\.i": "ῂ", "e-\\i": "ῂ", # ῂ
        "e|" : "ῃ", "e|.i": "ῃ", "e-.i": "ῃ", # ῃ
        "e/|" : "ῄ", "e/.i": "ῄ", "e/-i": "ῄ", # ῄ
        "e^|" : "ῇ", "e^.i": "ῇ", "e^-i": "ῇ",
            "e~|" : "ῇ", "e~.i": "ῇ", "e~-i": "ῇ", 
            "e=|" : "ῇ", "e=.i": "ῇ", "e=-i": "ῇ", # ῇ

        "o\\|": "ῲ", "o\\.i": "ῲ", "o-\\i": "ῲ", # ῲ
        "o|" : "ῳ", "o|.i": "ῳ", "o-.i": "ῳ", # ῳ
        "o/|" : "ῴ", "o/.i": "ῴ", "o/-.i": "ῴ", # ῴ
        "o^|" : "ῷ", "o^.i": "ῷ", "o^-i": "ῷ",
            "o~|" : "ῷ", "o~.i": "ῷ", "o~-i": "ῷ",
            "o=|" : "ῷ", "o=.i": "ῷ", "o=-i": "ῷ", # ῷ

    # breathings and long vowels
        "e-(\\" : "ἣ", "he-\\" : "ἣ", # ἣ
        "e-)\\" : "ἢ", "e)-\\" : "ἢ", # ἢ
        "e)-/" : "ἤ", 
            "e-(/" : "ἥ", "e-(/" : "ἥ", "he-/" : "ἥ", # ἥ
        "e-)=" : "ἦ",  "e)-=" : "ἦ", "e)=" : "ἦ",
            "e-)^" : "ἦ", "e)-^" : "ἦ",
            "e-)~" : "ἦ", "e)-~" : "ἦ",
            "e)^" : "ἦ", "e)^" : "ἦ", "e)~" : "ἦ", # ἦ
            # ἦ
        "e(-=" : "ἧ", "e(-=" : "ἧ",
            "e-(=" : "ἧ", "he-=" : "ἧ",
            "e(-^" : "ἦ", 
            "e-(^" : "ἦ", "he-^" : "ἦ", 
            "e-(~" : "ἦ", "he-~" : "ἦ", # ἧ
        "e)-" : "ἠ", # ἠ
        "e(-" : "ἡ", "he-" : "ἡ", # ἠ
       
        "E)-\\" : "Ἢ", # Ἢ
        "E)-\\" : "Ἣ", "HE-\\" : "Ἣ", # Ἣ
        "E)-/" : "Ἤ",  # Ἤ
        "E)-/" : "Ἥ", "HE-/" : "Ἥ", # Ἥ
        "E)-=" : "Ἦ", 
            "E-)^" : "Ἦ", 
            "E-)~" : "Ἦ",  # Ἦ
        "E-(=" : "Ἧ", "HE-=" : "Ἧ",
            "E-^" : "Ἦ", "HE-^" : "Ἦ", 
            "E-~" : "Ἦ", "HE-~" : "Ἦ", # Ἧ
        "E)-" : "Ἠ",  # Ἠ
        "E(-" : "Ἡ", "HE-" : "Ἡ", # Ἡ

        "o)-\\" : "ὢ", # ὢ
        "o))-\\" : "ὢ", 
        "o(-\\" : "ὣ", "ho-\\" : "ὣ", # ὣ
        "o)-/" : "ὤ",  # ὤ
        "o(-/" : "ὥ",  "ho-/" : "ὥ", # ὥ
        "o)-=" : "ὦ",  
            "o-)^" : "ὦ", 
            "o-)~" : "ὦ",  # ὦ
        "o-(=" : "ὧ", "ho-=" : "ὧ",
            "o-^" : "ὦ", "ho-^" : "ὦ", 
            "o-~" : "ὦ", "ho-~" : "ὦ", # ὧ
        "o)-" : "ὠ", # ὠ
        "o(-" : "ὡ", "ho-" : "ὡ", # ὡ
        
        "O)-\\" : "Ὢ", ")O-\\" : "Ὢ", # Ὢ
        "O(-\\" : "Ὣ", "(O-\\" : "Ὣ", "HO-\\" : "Ὣ", # Ὣ
        "O)-/" : "Ὤ", ")O-/" : "Ὤ", # Ὤ
        "O(-/" : "Ὥ", "(O-/" : "Ὥ", "HO-/" : "Ὥ", # Ὥ
        "O)-=" : "Ὦ", ")O-=" : "Ὦ", 
            "O-)^" : "Ὦ", ")O-^" : "Ὦ",
            "O-)~" : "Ὦ", ")O-~" : "Ὦ", # Ὦ
        "O-(=" : "Ὧ", "(O-=" : "Ὧ", "HO-=" : "Ὧ",
            "O-^" : "Ὦ", "(O-^" : "Ὦ", "HO-^" : "Ὦ", 
            "O-~" : "Ὦ", "(O-~" : "Ὦ", "HO-~" : "Ὦ", # Ὧ
        "O)-" : "Ὠ", ")O-" : "Ὠ", # Ὠ
        "O(-" : "Ὡ", "(O-" : "Ὡ", "HO-" : "Ὡ", # Ὡ
        
        "u)\\": "ὒ", ")u\\" : "ὒ", # ὒ
        "u(/": "ὓ", "(u/" : "ὓ", "hu/" : "ὓ", # ὓ
        "u)/" : "ὔ", ")u/" : "ὔ", # ὔ
        "u(/" : "ὕ", "(u/" : "ὕ", "hu/" : "ὕ", # ὕ
        "u)=" : "ὖ", ")u=" : "ὖ", 
            "u)^" : "ὖ", ")u^" : "ὖ",
            "u)~" : "ὖ", ")u~" : "ὖ", # ὖ
        "u(=" : "ὗ", "(u=" : "ὗ", "hu=" : "ὗ",
            "u^" : "ὖ", "(u^" : "ὖ", "hu^" : "ὖ", 
            "u~" : "ὖ", "(u~" : "ὖ", "hu~" : "ὖ", # ὗ
        "U)\\": "ὒ", ")U\\" : "ὒ", # ὒ
        "U(/": "ὓ", "(U/" : "ὓ", "HU/" : "ὓ", # ὓ
        "U)/" : "ὔ", ")U/" : "ὔ", # ὔ
        "U(/" : "ὕ", "(U/" : "ὕ", "HU/" : "ὕ", # ὕ
        "U)=" : "ὖ", ")U=" : "ὖ", 
            "U)^" : "ὖ", ")U^" : "ὖ",
            "U)~" : "ὖ", ")U~" : "ὖ", # ὖ
        "U(=" : "ὗ", "(U=" : "ὗ", "HU=" : "ὗ",
            "U^" : "ὖ", "(U^" : "ὖ", "HU^" : "ὖ", 
            "U~" : "ὖ", "(U~" : "ὖ", "HU~" : "ὖ", # ὗ
        
        "y)\\" : "ὒ", ")y\\" : "ὒ", # ὒ
        "y(/" : "ὕ", "(y/" : "ὕ", "hy/" : "ὕ", # ὕ
        "Y)\\" : "ὒ", ")Y\\" : "ὒ", # ὒ
        "Y(/" : "ὓ", "(Y/" : "ὓ", "HY/" : "ὓ", # ὓ
        "Y)/" : "ὔ", ")Y/" : "ὔ", # ὔ
        "Y(/" : "ὕ", "(Y/" : "ὕ", "HY/" : "ὕ", # ὕ
        "Y)=" : "ὖ", ")Y=" : "ὖ", 
            "Y)^" : "ὖ", ")Y^" : "ὖ",
            "Y)~" : "ὖ", ")Y~" : "ὖ", # ὖ
        "Y(=" : "ὗ", "(Y=" : "ὗ", "HY=" : "ὗ",
            "Y^" : "ὖ", "(Y^" : "ὖ", "HY^" : "ὖ", 
            "Y~" : "ὖ", "(Y~" : "ὖ", "HY~" : "ὖ", # ὗ

        "i)\\" : "ἲ", ")i\\" : "ἲ", # ἲ
        "i(/" : "ἳ", "(i/" : "ἳ", "hi/" : "ἳ", # ἳ
        "i)/" : "ἴ", ")i/" : "ἴ", # ἴ
        "i(/" : "ἵ", "(i/" : "ἵ", "hi/" : "ἵ", # ἵ
        "i)=" : "ἶ", ")i=" : "ἶ", 
            "i)^" : "ἶ", ")i^" : "ἶ",
            "i)~" : "ἶ", ")i~" : "ἶ", # ἶ
        "i(=" : "ἷ", "(i=" : "ἷ", "hi=" : "ἷ",
            "i^" : "ἶ", "(i^" : "ἶ", "hi^" : "ἶ", 
            "i~" : "ἶ", "(i~" : "ἶ", "hi~" : "ἶ", # ἷ
        "I)\\" : "Ἲ", ")I\\" : "Ἲ", # Ἲ
        "I(/" : "Ἳ", "(I/" : "Ἳ", "HI/" : "Ἳ", # Ἳ
        "I)/" : "Ἴ", ")I/" : "Ἴ", # Ἴ
        "I(/" : "Ἵ", "(I/" : "Ἵ", "HI/" : "Ἵ", # Ἵ
        "I)=" : "Ἶ", ")I=" : "Ἶ", 
            "I)^" : "Ἶ", ")I^" : "Ἶ",
            "I)~" : "Ἶ", ")I~" : "Ἶ", # Ἶ
        "I(=" : "Ἷ", "(I=" : "Ἷ", "HI=" : "Ἷ",
            "I^" : "Ἶ", "(I^" : "Ἶ", "HI^" : "Ἶ", 
            "I~" : "Ἶ", "(I~" : "Ἶ", "HI~" : "Ἶ", # Ἷ

    # breathings and dipthongs
        "hai/" : "αἵ", #αἵ
        "hai\\" : "αἳ", #αἳ
        "hei/" : "εἵ", #εἵ
        "hei\\" : "εἳ", #εἳ
        "hoi/" : "οἵ", #οἵ
        "hoi\\" : "οἳ", #οἳ
        "hui/" : "υἵ", #υἵ
        "hui\\" : "υἳ", #υἳ
        "hyi/" : "υἵ", #υἵ
        "hyi\\" : "υἳ", #υἳ
        "Hai/" : "Αἵ", #Αἵ
        "Hai\\" : "Αἳ", #Αἳ
        "Hei/" : "Εἵ", #Εἵ
        "Hei\\" : "Εἳ", #Εἳ
        "Hoi/" : "Οἵ", #Οἵ
        "Hoi\\" : "Οἳ", #Οἳ
        "Hui/" : "Υἵ", #Υἵ
        "Hui\\" : "Υἳ", #Υἳ
        "Hyi/" : "Υἵ", #Υἵ
        "Hyi\\" : "Υἳ", #Υἳ

        "ai)/" : "αἵ", #αἵ
        "ai)\\" : "αἲ", #αἲ
        "ei)/" : "εἵ", #εἵ
        "ei)\\" : "εἲ", #εἲ
        "oi)/" : "οἵ", #οἵ
        "oi)\\" : "οἲ", #οἲ
        "ui)/" : "υἵ", #υἵ
        "ui)\\" : "υἲ", #υἲ
        "yi)/" : "υἵ", #υἵ
        "yi)\\" : "υἲ", #υἲ
        "Yi)/" : "Υἵ", #Υἵ
        "Yi)\\" : "Υἲ", #Υἲ
        
        "au)/" : "αὔ", #αὔ
        "au)\\" : "αὒ", #αὒ
        "eu)/" : "εὔ", #εὔ
        "eu)\\" : "εὒ", #εὒ
        "ou)/" : "οὔ", #οὔ
        "ou)\\" : "οὒ", #οὒ
        
        "hau/" : "αὕ", #αὕ
        "hau\\" : "αὓ", #αὓ
        "heu/" : "εὕ", #εὕ
        "heu\\" : "εὓ", #εὓ
        "hou/" : "οὕ", #οὕ
        "hou\\" : "οὓ", #οὓ
        
    
        "ai)" : "αἰ", # αἰ
        "ai(" : "αἱ", "hai" : "αἱ", # αἱ
        "Ai)" : "Αἰ", # Αἰ
        "Ai(" : "Αἱ", "Hai" : "Αἱ", # Αἱ
        "ei)" : "εἰ", # εἰ
        "ei(" : "εἱ", "hei" : "εἱ", # εἱ
        "Ei)" : "Εἰ", # Εἰ
        "Ei(" : "Εἱ", "Hei" : "Εἱ", # Εἱ
        "oi)" : "οἰ", # οἰ
        "oi(" : "οἱ", "hoi" : "οἱ", # οἱ
        "Oi)" : "Οἰ", # Οἰ
        "Oi(" : "Οἱ", "Hoi" : "Οἱ", # Οἱ
        "ui)" : "υἰ", # υἰ
        "ui(" : "υἱ", "hui" : "υἱ", # υἱ
        "Ui)" : "Υἰ", # Υἰ
        "Ui(" : "Υἱ", "Hui" : "Υἱ", # Υἱ
        "yi)" : "υἱ", # υἱ
        "yi(" : "υἱ", "hyi" : "υἱ", # υἱ
        "Yi)" : "Υἱ", # Υἱ
        "Yi(" : "Υἱ", "Hyi" : "Υἱ", # Υἱ

        "au)" : "αὐ", # αὐ
        "au(" : "αὑ", "hau" : "αὑ", # αὑ
        "Au)" : "Αὐ", # Αὐ
        "Au(" : "Αὑ", "Hau" : "Αὑ", # Αὑ
        "eu)" : "εὐ", # εὐ
        "eu(" : "εὑ", "heu" : "εὑ", # εὑ
        "Eu)" : "Εὐ", # Εὐ
        "Eu(" : "Εὑ", "Heu" : "Εὑ", # Εὑ
        "ou)" : "οὐ", # οὐ
        "ou(" : "οὑ", "hou" : "οὑ", # οὑ
        "Ou)" : "Οὐ", # Οὐ
        "Ou(" : "Οὑ", "Hou" : "Οὑ", # Οὑ


# breathings(vowel "a")  
        "a)\\" : "ἂ", ")a\\" : "ἂ", # ἂ
        "a(\\" : "ἃ", "(a\\" : "ἃ", "ha\\" : "ἃ", # ἃ
        "a)/" : "ἄ", ")a/" : "ἄ", # ἄ
        "a(/" : "ἅ", "(a/" : "ἅ", "ha/" : "ἅ", # ἅ
        "a)=" : "ἆ", ")a=" : "ἆ",
            "a)^" : "ἆ", ")a^" : "ἆ",
            "a)~" : "ἆ", ")a~" : "ἆ", # ἆ
        "a(=" : "ἇ", "(a=" : "ἇ", "ha=" : "ἇ",
            "a^" : "ἆ", "(a^" : "ἆ", "ha^" : "ἆ",
            "a~" : "ἆ", "(a~" : "ἆ", "ha~" : "ἆ", # ἇ
        "a)" : "ἀ", ")a" : "ἀ", # ἀ
        "a(" : "ἁ", "(a" : "ἁ", "ha" : "ἁ", # ἁ
        
        "A)\\" : "Ἂ", ")A\\" : "Ἂ", # Ἂ
        "A(\\" : "Ἃ", "(A\\" : "Ἃ", "Ha\\" : "Ἃ", # Ἃ
        "A)/" : "Ἄ", ")A/" : "Ἄ", # Ἄ
        "A(/" : "Ἅ", "(A/" : "Ἅ", "Ha/" : "Ἅ", # Ἅ
        "A)=" : "Ἆ", ")A=" : "Ἆ",
            "A)^" : "Ἆ", ")A^" : "Ἆ",
            "A)~" : "Ἆ", ")A~" : "Ἆ", # Ἆ
        "A(=" : "Ἇ", "(A=" : "Ἇ", "Ha=" : "Ἇ",
            "A^" : "Ἆ", "(A^" : "Ἆ", "Ha^" : "Ἆ",
            "A~" : "Ἆ", "(A~" : "Ἆ", "Ha~" : "Ἆ", # Ἇ
        "A)" : "Ἀ", ")A" : "Ἀ", # Ἀ
        "A(" : "Ἁ", "(A" : "Ἁ", "Ha" : "Ἁ", # Ἁ


   # breathings, short vowels, et cetera
        "e)\\": "ἒ", ")e\\" : "ἒ", # ἒ
        "e(\\": "ἓ", "(e\\" : "ἓ", "he\\" : "ἓ", # ἓ
        "e)/" : "ἔ", ")e/" : "ἔ", # ἔ
        "e(/" : "ἕ", "(e/" : "ἕ", "he/" : "ἕ", # ἕ
        "E)\\": "Ἒ", ")E\\" : "Ἒ", # Ἒ
        "E(/": "Ἓ", "(E/" : "Ἓ", "He/" : "Ἓ", # Ἓ
        "E)/" : "Ἔ", # Ἔ
        "E(/" : "Ἕ", "He/" : "Ἕ", # Ἕ

        "rh" : "ῥ", "Rh" : "Ῥ", # Ῥ
        "a)" : "ἀ", # ἀ
        "a(" : "ἁ", "ha" : "ἁ", # ἁ
        "A)" : "Ἀ",  # Ἀ
        "A(" : "Ἁ", "Ha" : "Ἁ", # Ἁ
        "e)" : "ἐ",  # ἐ
        "e(" : "ἑ",  "he" : "ἑ", # ἑ)
        "E)" : "Ἐ",  # Ἐ
        "E(" : "Ἑ",  "He" : "Ἑ", # Ἑ
        "i)" : "ἰ", # ἰ
        "i(" : "ἱ", "hi" : "ἱ", # ἱ
        "I)" : "Ἰ",  # Ἰ
        "I(" : "Ἱ", "Hi" : "Ἱ", # Ἱ

        "o)/" : "ὄ", # ὄ
        "o)\\" : "ὂ", # ὂ
            "o)" : "ὀ",  # ὀ
        "o(/" : "ὅ", "ho/" :"ὅ", # ὅ
        "o(\\" : "ὃ", "ho\\" : "ὃ", # ὃ
            "o(" : "ὁ", "ho" : "ὁ", # ὁ

        "O)" : "Ὀ",  # Ὀ
        "O(" : "Ὁ", "HO" : "Ὁ", # Ὁ
        "u)" : "ὐ", ")u" : "ὐ", # ὐ
        "u(" : "ὑ", "(u" : "ὑ", "hu" : "ὑ", # ὑ
        "U)" : "Ὑ", ")U" : "Ὑ", # Ὑ
        "U(" : "Ὕ", "(U" : "Ὕ", "HU" : "Ὕ", # Ὕ
        "y)" : "ὐ", ")y" : "ὐ", # ὐ
        "y(" : "ὑ", "(y" : "ὑ", "hy" : "ὑ", # ὑ
        "Y(" : "Ὑ", "(Y" : "Ὑ", "Hy" : "Ὑ", # Ὑ
    

    # vowels with accents and circumflexes
        "a\\" : "ὰ", # ὰ
        "a/" : "ά", # ά
        "a=" : "ᾶ", "a~" : "ᾶ", "a^" : "ᾶ", # ᾶ

        "e\\" : "ὲ", # ὲ
        "e/" : "έ", # έ
        "e=" : "ῆ", "e~" : "ῆ", "e^" : "ῆ", # ῆ
        "e-=" : "ῆ", "e-~" : "ῆ", "e-^" : "ῆ", # ῆ
        "e-\\" : "ὴ", # ὴ
        "e-/" : "ή", # ή
        

        "i\\" : "ὶ", # ὶ
        "i/" : "ί", # ί
        "i=" : "ῖ", "i~" : "ῖ", "i^" : "ῖ", # ῖ

        "o\\" : "ὸ", # ὸ
        "o/" : "ό", # ό
        "o=" : "ῶ", "o~" : "ῶ", "o^" : "ῶ", # ῶ
        "o-=" : "ῶ", "o-~" : "ῶ", "o-^" : "ῶ", # ῶ
        "o-/" : "ώ", # ώ
        "o-\\" : "ὼ", # ὼ

        "u\\" : "ὺ", # ὺ
        "u/" : "ύ", # ύ
        "u=" : "ῦ", "u~" : "ῦ", "u^" : "ῦ", # ῦ

        "y\\" : "ὺ", # ὺ
        "y/" : "ύ", # ύ
        "y=" : "ῦ", "y~" : "ῦ", "y^" : "ῦ", # ῦ

        "o-\\" : "ὼ", # ὼ
        "o-/" : "ώ", # ώ
        "o-=" : "ῶ", "o-~" : "ῶ", "o-^" : "ῶ", # ῶ
        

    # diaresis
        "i**" : "ϊ", # ϊ
        "i*\\*" : "ῒ", "i\\**" : "ῒ", "i**\\" : "ῒ", # ῒ
        "i*/*" : "ΐ", "i/**" : "ΐ", "i**/" : "ΐ", # ΐ
        "i*=*" : "ῗ", "i=**" : "ῗ", "i**=" : "ῗ", 
            "i*^*" : "ῗ", "i^**" : "ῗ", "i**^" : "ῗ", 
            "i*~*" : "ῗ", "i~**" : "ῗ", "i**~" : "ῗ",# ῖ 

        "u**" : "ϋ", # ϋ
        "u*\\*" : "ῢ", "u\\**" : "ῢ", "u**\\" : "ῢ", # ῢ
        "u*/*" : "ΰ", "u/**" : "ΰ", "u**/" : "ΰ", # ΰ
        "u*=*" : "ῧ", "u=**" : "ῧ", "u**=" : "ῧ",
           "u*^*" : "ῧ", "u^**" : "ῧ", "u**^" : "ῧ",
            "u*~*" : "ῧ", "u~**" : "ῧ", "u**~" : "ῧ", # ῦ
    
        "y**" : "ϋ", # ϋ
        "y*\\*" : "ῢ", "y\\**" : "ῢ", "y**\\" : "ῢ", # ῢ
        "y*/*" : "ΰ", "y/**" : "ΰ", "y**/" : "ΰ", # ΰ
        "y*=*" : "ῧ", "y=**" : "ῧ", "y**=" : "ῧ",
           "y*^*" : "ῧ", "y^**" : "ῧ", "y**^" : "ῧ",
            "y*~*" : "ῧ", "y~**" : "ῧ", "y**~" : "ῧ", # ῦ

}

with open("greek_dict_accent.json", "w", encoding='utf-8') as f:
    json.dump(greek_dict_accent, f, ensure_ascii=False, indent=4)

# greek_dict_one_letter
greek_dict_one_letter = {
    # 장모음
    "O-":"Ω", "o-": "ω",
    "E-": "Η", "e-": "η",
    # 단모음과 자음
    "A": "Α", "a": "α",
    "B": "Β", "b": "β",
    "G": "Γ", "g": "γ",
    "D": "Δ", "d": "δ",
    "E": "Ε", "e": "ε",
    "I": "Ι", "i": "ι",
    "X": "Ξ", "x": "ξ",
    "C": "Κ", "c": "κ",
    "K": "Κ", "k": "κ",
    "L": "Λ", "l": "λ",
    "M": "Μ", "m": "μ",
    "N": "Ν", "n": "ν",
    "O": "Ο", "o": "ο",
    "P": "Π", "p": "π",
    "Q": "Θ", "q": "θ",
    "R": "Ρ", "r": "ρ",
    "S": "Σ", "s": "σ",
    "T": "Τ", "t": "τ",
    "U": "Υ", "u": "υ",
    "F": "Φ", "f": "φ",
    "W": "Ϝ", "w": "ϝ",
    "Y": "Υ", "y": "υ",
    "Z": "Ζ", "z": "ζ",

    "?" : ";",
    ":" : "·"

}

with open("greek_dict_one_letter.json", "w", encoding='utf-8') as f:
    json.dump(greek_dict_one_letter, f, ensure_ascii=False, indent=4)


# te_and_pote
te_and_pote = ['te', 't\'', 'te/', 'ge', 'g\'', 'ge/', 'pote', 'pot\'',
            'se', 's\'', 'se/', 'me', 'me/', 'moi', 'm\'', 'moi/',
            'tis', 'ti/s','ti', 'ti/',
            'he', 'he/', 
            'hoi', 'nu/', 'nu', 'pou', 'pou/',
            'sphisi', 'sphin', 'sphi/n', 'sph\'', 
            'sfisi', 'sfin', 'sfi/n', 'sf\'',
            'ke', 'ke/',   
    ]

with open("te_and_pote.json", "w", encoding='utf-8') as f:
    json.dump(te_and_pote, f, ensure_ascii=False, indent=4)

# Ugaritic
# ugaritic_conversion_list
ugaritic_conversion_list = [
    (")a", "ʾa", "𐎀"),
    ("b", "b", "𐎁"),
    ("h_", "ḫ", "𐎃"),
    ("h.", "ḥ", "𐎈"),
    ("h", "h", "𐎅"),
    ("w", "w", "𐎆"),
    ("t.", "ṭ", "𐎉"),
    ("y", "y", "𐎊"),
    ("k", "k", "𐎋"),
    ("s^", "š", "𐎌"),
    ("l", "l", "𐎍"),
    ("m", "m", "𐎎"),
    ("d_", "ḏ", "𐎏"),
    ("d", "d", "𐎄"),
    ("n", "n", "𐎐"),
    ("z.", "ẓ", "𐎑"),
    ("z", "z", "𐎇"),
    ("s.", "ṣ", "𐎕"),
    ("s", "s", "𐎒"),
    ("(", "ʿ", "𐎓"),
    ("p", "p", "𐎗"),
    ("q", "q", "𐎖"),
    ("r", "r", "𐎗"),
    ("t_", "ṯ", "𐎘"),
    ("g^", "ġ", "𐎙"),
    ("g", "g", "𐎂"),
    ("t", "t", "𐎚"),
    (")i", "ʾi", "𐎛"),
    (")u", "ʾu", "𐎜"),
    (")", "ʾ", "𐎓"),
    ("(", "ʿ", ),
    ("a-", "ā", ""),
    ("e-", "ē", ""),
    ("i-", "ī", ""),
    ("u-", "ū", ""),
    ("a^", "â", ""),
    ("e^", "ê", ""),
    ("i^", "î", ""),
    ("u^", "û", ""),
    ("s2", "s2", "𐎝"),
    (" .", " .", "𐎟"),
    ("R", "√", "")
]

with open("ugaritic_conversion_list.json", "w", encoding='utf-8') as f:
    json.dump(ugaritic_conversion_list, f, ensure_ascii=False, indent=4)


# latin_dict
latin_dict = {
    "AE": "Æ", "Ae":"Æ" ,"ae": "æ", # æ
    "OE": "Œ", "Oe":"Œ", "oe": "œ", # œ
    "a-": "ā", "A-": "Ā", # ā
    "e-": "ē", "E-": "Ē", # ē
    "i-": "ī", "I-": "Ī", # ī
    "o-": "ō", "O-": "Ō", # ō
    "u-": "ū", "U-": "Ū", # ū
    "a'": "ă", "A'": "Ă", # ă
    "e'": "ĕ", "E'": "Ĕ", # ĕ
    "i'": "ĭ", "I'": "Ĭ", # ĭ
    "o'": "ŏ", "O'": "Ŏ", # ŏ
    "u'": "ŭ", "U'": "Ŭ", # ŭ
    "a-'":"ā̌", "a'-":"ā̌", "A-'":"Ā̌", "A'-":"Ā̌", # ā̌
    "e-'":"ē̌", "e'-":"ē̌", "E-'":"Ē̌", "E'-":"Ē̌", # ē̌
    "i-'":"ī̌", "i'-":"ī̌", "I-'":"Ī̌", "I'-":"Ī̌", # ī̌
    "o-'":"ō̌", "o'-":"ō̌", "O-'":"Ō̌", "O'-":"Ō̌", # ō̌
    "u-'":"ū̌", "u'-":"ū̌", "U-'":"Ū̌", "U'-":"Ū̌", # ū̌
}

with open("latin_dict.json", "w", encoding='utf-8') as f:
    json.dump(latin_dict, f, ensure_ascii=False, indent=4)


# 범례 설명 try_these 리스트
try_these = [
    "en arche^.i e-^n ho lo/gos", 
    "chalepa/ ta/ kala/",
    "me-=nin a/eide thea/ Pe-le-i**a/deo- Achile=os",
    "a/ndra moi e/nnepe, mou~sa,",
    "en arche^.i epoi/e-sen ho theo/s to/n ourano/n kai/ te-/n ge^n",
    "gno^thi seauto/n",
    "me-de/n a/gan",
    "engy/a pa/ra d' A/ta",
    "he/n oi=da ho/ti oude/n oi=da",
    "ho a/nthro-pos phy/sei politiko/n zo=.ion",
    "e-/ ta/n e-/ epi/ ta~s",
    "kai/ su/ te/knon?",
    "koina/ ta/ phi/lo-n",
    "Kre=tes aei/ pseu^stai",
    "pa/nta rhei~",
    "apo/ me-chane~s theo/s",
    "ha/pax lego/menon",
    "ou~tis emoi/ g' o/noma",
    "rhododa/ktylos E-o-/s",
    "ta/ pa/nta rhei~ kai/ oude/n me/nei.",
    "hyio/s monogene-/s",
    "psyche=s iatrei=on",
    "Caesar no-n super grammatico-s",
    "ve-ni- vi-di- vi-ci-",
    "kt_r w h_ss",
    ")al)eyuna ba(li",
    "R)mr"
]
             
with open("try_these.json", "w", encoding='utf-8') as f:
    json.dump(try_these, f, ensure_ascii=False, indent=4)