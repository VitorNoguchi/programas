from random import randint
placar=0
jogos=5
while jogos>0:
    pedra="1"
    papel="2"
    tesoura="3"
    lagarto="4"
    spock="5"
    computador=randint(1,5)    
    print("estou pronto")
    jogador=input("digite sua escolha:\n")
    if computador==1 and jogador=="pedra":
       jogos-=1
    elif computador==1 and jogador=="papel":
        placar-=1
        jogos-=1
    elif computador==1 and jogador=="tesoura":
        placar+=1
        jogos-=1
    elif computador==1 and jogador=="lagarto":
        placar+=1
        jogos-=1
    elif computador==1 and jogador=="spock":
        placar-=1
        jogos-=1
    elif computador==2 and jogador=="pedra":
        placar+=1
        jogos-=1
    elif computador==2 and jogador=="papel":
        jogos-=1
    elif computador==2 and jogador=="tesoura":
        placar-=1
        jogos-=1
    elif computador==2 and jogador=="lagarto":
        placar-=1
        jogos-=1
    elif computador==2 and jogador=="spock":
        placar+=1
        jogos-=1
    elif computador==3 and jogador=="pedra":
        placar-=1
        jogos-=1
    elif computador==3 and jogador=="papel":
        placar+=1
        jogos-=1
    elif computador==3 and jogador=="tesoura":
        jogos-=1
    elif computador==3 and jogador=="lagarto":
        placar+=1
        jogos-=1
    elif computador==3 and jogador=="spock":
        placar-=1
        jogos-=1
    elif computador==4 and jogador=="pedra":
        placar-=1
        jogos-=1
    elif computador==4 and jogador=="papel":
        placar+=1
        jogos-=1
    elif computador==4 and jogador=="tesoura":
        placar-=1
        jogos-=1
    elif computador==4 and jogador=="lagarto":
        jogos-=1
    elif computador==4 and jogador=="spock":
        placar+=1
        jogos-=1
    elif computador==5 and jogador=="pedra":
        placar+=1
        jogos-=1
    elif computador==5 and jogador=="papel":
        placar-=1
        jogos-=1
    elif computador==5 and jogador=="tesoura":
        placar+=1
        jogos-=1
    elif computador==5 and jogador=="lagarto":
        placar-=1
        jogos-=1
    elif computador==5 and jogador=="spock":
        jogos-=1
    else:
        computador=randint(1,5)
if placar>0:
    print("você perdeu, tente novamente")
if placar<0:
    print("parabens, voce venceu!")
if placar==0:
    print("empate")