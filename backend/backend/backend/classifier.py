SUBJECTS = {
    "matemática": [
        "equação",
        "fração",
        "porcentagem",
        "raiz",
        "potência",
        "logaritmo"
    ],

    "biologia": [
        "célula",
        "fotossíntese",
        "mitose",
        "dna",
        "rna",
        "respiração"
    ],

    "história":[
        "segunda guerra",
        "idade média",
        "império",
        "revolução"
    ],

    "geografia":[
        "clima",
        "solo",
        "relevo",
        "vegetação"
    ]
}


def classify(question):

    text = question.lower()

    for subject, words in SUBJECTS.items():

        for word in words:

            if word in text:

                return subject

    return "geral"
