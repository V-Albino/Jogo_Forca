
def selectWord():
    word = str('palavra')
    return list(word)

def verificaVitoria(word, forca):
    win = False
    for i in range(len(word)):
        if word[i] == forca[i]:
            win = True
        else:
            return False
    return win

def playAgain():
    again = str(input('Deseja jogar novamente? (s) ou (n)'))
    while again.lower() != str('s') and again.lower() != str('n'):
        again = input('Resposta invalida, apenas (s) ou (n)')
    if again.lower() == str('n'):
        print('Que peninha...')
        return True
    elif again.lower() == str('s'):
        print('Então vamos nessa!')
        return False

def tentativa(word, jogo, vida):
    acerto = False
    let = str(input())
    for i in range(len(word)):
        if word[i] == let.lower():
            jogo[i] = let.lower()
            acerto = True
    
    if acerto == False:
        vida -=1
        if vida == 0:
            print('Voce perdeu!')
            inGame = False
        else:
            print("Voce errou, tente novamente!")
        print('Voce ainda tem '+ str(vida) +' vidas')
    elif acerto == True:
            print("Voce acertou!")
            if verificaVitoria(word, jogo):
                print('Parabéns!! Você venceu!!')
                vida = 0
    print(jogo)
    return vida

def game():
    print('Vamos jogar um jogo!')
    end = False
    while end == False:
        word = selectWord()
        jogo = []
        for i in range(len(word)):
            jogo.append("_")
        vida = 5
        inGame = True

        print('Tente uma letra')
        print(jogo)
        while vida >= 1:
            vida = tentativa(word, jogo, vida)
        end = playAgain()
                          
game();