from pyscript import document, when
from random import randint
import asyncio


# ==================================================
# JOGADOR
# ==================================================

x = 100
y = 100

velocidade = 10

jogador = document.querySelector("#jogador")


def atualizar_jogador():

    jogador.style.left = f"{x}px"

    jogador.style.top = f"{y}px"


# ==================================================
# MOEDA
# ==================================================

moeda_x = 300
moeda_y = 200

moeda = document.querySelector("#moeda")


def mover_moeda():

    global moeda_x, moeda_y

    moeda_x = randint(20, 650)

    moeda_y = randint(20, 410)

    moeda.style.left = f"{moeda_x}px"

    moeda.style.top = f"{moeda_y}px"


# ==================================================
# PONTUAÇÃO
# ==================================================

pontos = 0

placar = document.querySelector("#placar")

mensagem = document.querySelector("#mensagem")


# ==================================================
# VERIFICAR MOEDA
# ==================================================

def verificar_moeda():

    global pontos

    distancia_x = abs(x - moeda_x)

    distancia_y = abs(y - moeda_y)

    if distancia_x < 40 and distancia_y < 40:

        pontos = pontos + 1

        placar.innerText = pontos

        mensagem.innerText = "🪙 Moeda coletada! +1 ponto!"

        mover_moeda()


# ==================================================
# INIMIGO
# ==================================================

inimigo_x = 500

inimigo_y = 200

velocidade_inimigo = 5

inimigo = document.querySelector("#inimigo")


# ==================================================
# MOVER INIMIGO
# ==================================================

def mover_inimigo():

    global inimigo_x

    inimigo_x = inimigo_x - velocidade_inimigo

    if inimigo_x < 0:

        inimigo_x = 650

    inimigo.style.left = f"{inimigo_x}px"

    inimigo.style.top = f"{inimigo_y}px"


# ==================================================
# CONTROLE DO JOGADOR
# ==================================================

@when("keydown", "body")
def tecla_pressionada(evento):

    global x, y

    if evento.key == "ArrowRight":

        x += velocidade

    elif evento.key == "ArrowLeft":

        x -= velocidade

    elif evento.key == "ArrowDown":

        y += velocidade

    elif evento.key == "ArrowUp":

        y -= velocidade

    else:

        return


    # ==============================================
    # LIMITES
    # ==============================================

    if x < 0:

        x = 0

    if x > 650:

        x = 650

    if y < 0:

        y = 0

    if y > 410:

        y = 410


    # ==============================================
    # ATUALIZA JOGADOR
    # ==============================================

    atualizar_jogador()


    # ==============================================
    # VERIFICA MOEDA
    # ==============================================

    verificar_moeda()


# ==================================================
# LOOP DO INIMIGO
# ==================================================

async def jogo():

    while True:

        mover_inimigo()

        await asyncio.sleep(0.03)


# ==================================================
# INICIALIZAÇÃO
# ==================================================

atualizar_jogador()

mover_moeda()

asyncio.create_task(jogo())