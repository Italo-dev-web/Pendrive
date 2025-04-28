import random

#isso foi um desvio da aula, espero que nao acontecça novamente e eu saiba diferenciar escola de estudos a parte
# Perguntas sobre comandos Git e suas respostas corretas
perguntas = [
    {
        "pergunta": "Qual comando é usado para iniciar um novo repositório Git?",
        "opcoes": ["A) git start", "B) git init", "C) git create", "D) git new"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual comando adiciona um arquivo para a área de stage?",
        "opcoes": ["A) git add", "B) git commit", "C) git push", "D) git stage"],
        "resposta": "A"
    },
    {
        "pergunta": "Qual comando cria um novo branch?",
        "opcoes": ["A) git branch new", "B) git create branch", "C) git branch", "D) git checkout -b"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual comando salva as mudanças no repositório com uma mensagem?",
        "opcoes": ["A) git save", "B) git add", "C) git message", "D) git commit"],
        "resposta": "D"
    },
    {
        "pergunta": "Qual comando envia as mudanças para um repositório remoto?",
        "opcoes": ["A) git upload", "B) git push", "C) git send", "D) git deploy"],
        "resposta": "B"
    }
]

def jogar_quiz():
    pontuacao = 0
    random.shuffle(perguntas)  # Embaralha as perguntas para cada jogo

    for pergunta in perguntas:
        print("\n" + pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)
        resposta = input("Escolha a opção correta (A, B, C ou D): ").upper()

        if resposta == pergunta["resposta"]:
            print("Correto! Você ganhou 1 ponto.")
            pontuacao += 1
        else:
            print(f"Incorreto. A resposta correta era: {pergunta['resposta']}")

    print(f"\nJogo encerrado! Sua pontuação final é: {pontuacao}/{len(perguntas)}")

# Inicia o jogo
jogar_quiz()
