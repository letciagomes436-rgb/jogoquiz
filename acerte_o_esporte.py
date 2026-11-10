import tkinter as tk
import random

janela = tk.Tk()
janela.title("Acerte o Esporte!")
janela.geometry("500x400")
janela.configure(bg="#1e90ff")

pontos = 0
pergunta_atual = 0

perguntas = [
    ["Qual esporte usa uma bola e uma cesta?",
     ["Futebol", "Basquete", "Vôlei"], "Basquete"],

    ["Qual esporte usa uma rede?",
     ["Vôlei", "Natação", "Corrida"], "Vôlei"],

    ["Quantos jogadores tem um time de futebol?",
     ["5", "11", "15"], "11"]
]

def responder(resposta):
    global pontos, pergunta_atual

    if resposta == perguntas[pergunta_atual][2]:
        pontos += 10
        resultado.config(text="Muito bem! Você acertou!")
    else:
        resultado.config(text="Ops! Resposta errada!")

    pergunta_atual += 1

    if pergunta_atual < len(perguntas):
        janela.after(1000, mostrar_pergunta)
    else:
        janela.after(1000, finalizar)

def mostrar_pergunta():
    pergunta = perguntas[pergunta_atual]

    titulo.config(text=pergunta[0])
    resultado.config(text="")

    for i in range(3):
        botoes[i].config(
            text=pergunta[1][i],
            command=lambda r=pergunta[1][i]: responder(r)
        )

    pontuacao.config(text="Pontos: " + str(pontos))

def finalizar():
    titulo.config(text="FIM DE JOGO!")
    resultado.config(text="Você fez " + str(pontos) + " pontos!")

    for botao in botoes:
        botao.pack_forget()

    pontuacao.config(text="Parabéns por jogar!")

titulo = tk.Label(
    janela,
    text="ACERTE O ESPORTE!",
    font=("Arial", 20, "bold"),
    bg="#1e90ff",
    fg="white"
)
titulo.pack(pady=30)

pontuacao = tk.Label(
    janela,
    text="Pontos: 0",
    font=("Arial", 14),
    bg="#1e90ff",
    fg="white"
)
pontuacao.pack()

resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 13, "bold"),
    bg="#1e90ff",
    fg="yellow"
)
resultado.pack(pady=10)

botoes = []

for i in range(3):
    b = tk.Button(
        janela,
        text="",
        font=("Arial", 14),
        bg="white",
        width=20,
        command=lambda: None
    )
    b.pack(pady=5)
    botoes.append(b)

mostrar_pergunta()
janela.mainloop()