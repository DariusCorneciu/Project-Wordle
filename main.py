import bot
import player
import os
from termcolor import cprint
alegere=-1

def meniu():

    cprint("---JOC WORDLE REALIZAT DE ECHIPA RACHETA---", "grey","on_red",attrs=["bold", "underline"])
    cprint("1.JOCUL DE WORDLE OBISNUIT","white","on_red",attrs=["underline"])
    cprint("2.BOTUL DE WORDLE","white","on_red",attrs=["underline"])
    cprint("IESI DIN JOCUL DE WORDLE(orice tasta)","white","on_red",attrs=["underline"])

while alegere!=0:
    meniu()
    alegere=int(input("Alege:"))
    if alegere==2:
        os.system('cls')
        bot.joc()
    elif alegere==1:
        os.system('cls')
        player.joc()
    else:
        os.system('cls')
        print("La revedere!")
        break