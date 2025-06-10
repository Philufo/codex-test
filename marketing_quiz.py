# -*- coding: utf-8 -*-
"""Interactive quiz on digital marketing."""


def ask_question(question):
    print("\n" + question['text'])
    for key, value in question['options'].items():
        print(f"{key}. {value}")
    answer = input("Votre r\xe9ponse: ")
    return question['points'].get(answer, 0)


def main():
    print("Bienvenue dans le questionnaire marketing digital!\n")
    questions = [
        {
            'text': "1. Votre site web est-il optimis\xe9 pour le r\xe9f\xe9rencement (SEO)?",
            'options': {'1': 'Oui', '2': 'Non'},
            'points': {'1': 20, '2': 0}
        },
        {
            'text': "2. Utilisez-vous des campagnes d'e-mail marketing r\xe9guli\xe8res?",
            'options': {'1': 'Oui', '2': 'Non'},
            'points': {'1': 20, '2': 0}
        },
        {
            'text': "3. Suivez-vous vos performances marketing via des outils d'analyse?",
            'options': {'1': 'Oui', '2': 'Non'},
            'points': {'1': 20, '2': 0}
        },
        {
            'text': "4. Quelle est la fr\xe9quence de vos publications sur les r\xe9seaux sociaux?",
            'options': {'1': 'Tous les jours', '2': 'Toutes les semaines', '3': 'Rarement'},
            'points': {'1': 20, '2': 10, '3': 0}
        },
        {
            'text': "5. Avez-vous d\xe9j\xe0 mis en place des campagnes publicitaires payantes?",
            'options': {'1': 'Oui', '2': 'Non'},
            'points': {'1': 20, '2': 0}
        },
    ]

    score = 0
    for q in questions:
        score += ask_question(q)

    print(f"\nVotre score final est de {score} / 100.")


if __name__ == "__main__":
    main()
