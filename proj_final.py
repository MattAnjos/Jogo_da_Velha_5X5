# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:21:59 2022

@author: uniemanjos
"""



def criarusuario():
    os.system("cls")#Apaga o terminal
    #print ("\n" * 120)  #Apaga o terminal
    print(" ".center(70),'1 - Criar um novo jogador / usuário:')#nome do menu
    y = input("\nDigite o nome do usuario: ")#Solicita o nome do usuario
    #v=0
    #d=0
    
    if os.path.isfile(f"{y}.csv") == True: #Verifica se o jogador ja existe
        
        print(" ".center(73)+'\n\n\nNome ja escolhido, escolha outro')#Informa nome ja existente
        input(" ".center(73)+"Pressione ENTER para continuar") # Solicita apertar o botao enter para continuar    
                   
    else:   #Cria o arquivo CSV para o novo jogador
        
    
        columns = ['numero da partida', 'vitorias', 'derrotas','qtd de vitorias','qtd de derrotas'] #Lista com as colunas
        #rows = {'numero da partida':0, 'vitorias':0, 'derrotas':0,'qtd de vitorias':0,'qtd de derrotas':0} #Linhas com as informaçoes zeradas
        data = pd.DataFrame(columns=columns) #Cria o dataframe com as linhas e colunas
        data.to_csv(f"{y}.csv",sep=',', index=False) #Cria o arquivo CSV a partir do dataframe
        

    return

def historico():
    os.system("cls")#Apaga o terminal
    #print ("\n" * 120)  #Apaga o terminal
    print(" ".center(70),'2 - Exibir histórico de um jogador:')#nome do menu
    y = input("\nDigite o nome do usuario: ")#Solicita o nome do usuario
    
    if os.path.isfile(f"{y}.csv") == True: #Verifica se o jogador ja existe
        
        data=pd.read_csv(f'{y}.csv')#Le arquivo CSV
        print(f"\n\n\n{data}\n\n\n")
        input(" ".center(73)+"Pressione ENTER para continuar") # Solicita apertar o botao enter para continuar
    else:
        print("Usuario inexistente\n\n\n")
        input(" ".center(73)+"Pressione ENTER para continuar") # Solicita apertar o botao enter para continuar
    return

def excluir():
    os.system("cls")#Apaga o terminal
    #print ("\n" * 120)  #Apaga o terminal
    print(" ".center(70),'3 - Excluir um jogador / usuário:')#nome do menu
    print("\n\n\n\n\n\n\n\n\n\n") #Centraliza o cursor
    y = input("Digite o nome do usuario: ")#Solicita o nome do usuario
    if os.path.isfile(f"{y}.csv") == True: #Verifica se o jogador ja existe
        
        os.remove(f'{y}.csv') #Apaga o arquivo do usuario
        print('\n\n\n\n\n')
        print(" ".center(80),'Usuario exluido\n')#mensagem de usuario apagado
        input(" ".center(73)+"Pressione ENTER para continuar") # Solicita apertar o botao enter para continuar
    
    else:
        print("Usuario inexistente\n\n\n")
        input(" ".center(70)+"Pressione ENTER para continuar") # Solicita apertar o botao enter para continuar
    
    return

def fechar():
    
    os.system("cls")#Apaga o terminal
    sys.exit()#Sai do jogo
    


def criartabuleiro(): #Funçao para criar o tabuleiro em branco
    lista=[]
    for linha in range(5):  #Cria a matriz em branco aonde vao ser colocados os
        linha=[]            # "X" e "O"
        for coluna in range(5):
            linha.append(" ")
        lista.append(linha)
    
    
    # Mostra no terminal o tabuleiro em branco
    
    print("\n\n\n\n\n\n\n\n\n\n") #Centraliza o cursor
    print(" ".center(73)," 0 "," 1 "," 2 "," 3 "," 4 ", sep=' ')
    print(" ".center(73),f" {lista[0][0]} ",f" {lista[0][1]} ",f" {lista[0][2]} ",f" {lista[0][3]} ",f" {lista[0][4]} "," 0 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {lista[1][0]} ",f" {lista[1][1]} ",f" {lista[1][2]} ",f" {lista[1][3]} ",f" {lista[1][4]} "," 1 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {lista[2][0]} ",f" {lista[2][1]} ",f" {lista[2][2]} ",f" {lista[2][3]} ",f" {lista[2][4]} "," 2 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {lista[3][0]} ",f" {lista[3][1]} ",f" {lista[3][2]} ",f" {lista[3][3]} ",f" {lista[3][4]} "," 3 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {lista[4][0]} ",f" {lista[4][1]} ",f" {lista[4][2]} ",f" {lista[4][3]} ",f" {lista[4][4]} "," 4 ", sep='|')
 
    return lista

def atualizatabuleiro(tabuleiro):
    print("\n\n\n\n\n\n\n\n\n\n") #Centraliza o cursor
    print(" ".center(73)," 0 "," 1 "," 2 "," 3 "," 4 ", sep=' ')
    print(" ".center(73),f" {tabuleiro[0][0]:} ",f" {tabuleiro[1][0]} ",f" {tabuleiro[2][0]} ",f" {tabuleiro[3][0]} ",f" {tabuleiro[4][0]} "," 0 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {tabuleiro[0][1]} ",f" {tabuleiro[1][1]} ",f" {tabuleiro[2][1]} ",f" {tabuleiro[3][1]} ",f" {tabuleiro[4][1]} "," 1 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {tabuleiro[0][2]} ",f" {tabuleiro[1][2]} ",f" {tabuleiro[2][2]} ",f" {tabuleiro[3][2]} ",f" {tabuleiro[4][2]} "," 2 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {tabuleiro[0][3]} ",f" {tabuleiro[1][3]} ",f" {tabuleiro[2][3]} ",f" {tabuleiro[3][3]} ",f" {tabuleiro[4][3]} "," 3 ", sep='|')
    print(" ".center(73),'---+---+---+---+---')
    print(" ".center(73),f" {tabuleiro[0][4]} ",f" {tabuleiro[1][4]} ",f" {tabuleiro[2][4]} ",f" {tabuleiro[3][4]} ",f" {tabuleiro[4][4]} "," 4 ", sep='|')

    return

def varredura(tabuleiro):
    
    vitoria=0 #Flag que detecta vitoria ou empate
    # 1 para vitoria, 2 para empate.
    
    #Varreduta das linhas
    
    #Varredura das linhas combinaçao X
    if (((tabuleiro[0][0]=="X") and (tabuleiro[1][0]=="X") and (tabuleiro[2][0]=="X") and (tabuleiro[3][0]=="X")) or 
        ((tabuleiro[1][0]=="X") and (tabuleiro[2][0]=="X") and (tabuleiro[3][0]=="X") and (tabuleiro[4][0]== "X")) or
        # Varredura coluna 0
        ((tabuleiro[0][1]=="X") and (tabuleiro[1][1]=="X") and (tabuleiro[2][1]=="X") and (tabuleiro[3][1]=="X")) or 
        ((tabuleiro[1][1]=="X") and (tabuleiro[2][1]=="X") and (tabuleiro[3][1]=="X") and (tabuleiro[4][1]== "X")) or
        # Varredura coluna 1
        ((tabuleiro[0][2]=="X") and (tabuleiro[1][2]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[3][2]=="X")) or 
        ((tabuleiro[1][2]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[3][2]=="X") and (tabuleiro[4][2]== "X")) or
        # Varredura coluna 
        ((tabuleiro[0][3]=="X") and (tabuleiro[1][3]=="X") and (tabuleiro[2][3]=="X") and (tabuleiro[3][3]=="X")) or 
        ((tabuleiro[1][3]=="X") and (tabuleiro[2][3]=="X") and (tabuleiro[3][3]=="X") and (tabuleiro[4][3]== "X")) or
        # Varredura coluna 3
        ((tabuleiro[0][4]=="X") and (tabuleiro[1][4]=="X") and (tabuleiro[2][4]=="X") and (tabuleiro[3][4]=="X")) or 
        ((tabuleiro[1][4]=="X") and (tabuleiro[2][4]=="X") and (tabuleiro[3][4]=="X") and (tabuleiro[4][4]== "X"))):
        # Varredura coluna 4
        vitoria=1
        
    #Varredura das linhas combinaçao O    
    elif (((tabuleiro[0][0]=="O") and (tabuleiro[1][0]=="O") and (tabuleiro[2][0]=="O") and (tabuleiro[3][0]=="O")) or 
        ((tabuleiro[1][0]=="O") and (tabuleiro[2][0]=="O") and (tabuleiro[3][0]=="O") and (tabuleiro[4][0]== "O")) or
        # Varredura coluna 0
        ((tabuleiro[0][1]=="O") and (tabuleiro[1][1]=="O") and (tabuleiro[2][1]=="O") and (tabuleiro[3][1]=="O")) or 
        ((tabuleiro[1][1]=="O") and (tabuleiro[2][1]=="O") and (tabuleiro[3][1]=="O") and (tabuleiro[4][1]== "O")) or
        # Varredura coluna 1
        ((tabuleiro[0][2]=="O") and (tabuleiro[1][2]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[3][2]=="O")) or 
        ((tabuleiro[1][2]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[3][2]=="O") and (tabuleiro[4][2]== "O")) or
        # Varredura coluna 
        ((tabuleiro[0][3]=="O") and (tabuleiro[1][3]=="O") and (tabuleiro[2][3]=="O") and (tabuleiro[3][3]=="O")) or 
        ((tabuleiro[1][3]=="O") and (tabuleiro[2][3]=="O") and (tabuleiro[3][3]=="O") and (tabuleiro[4][3]== "O")) or
        # Varredura coluna 3
        ((tabuleiro[0][4]=="O") and (tabuleiro[1][4]=="O") and (tabuleiro[2][4]=="O") and (tabuleiro[3][4]=="O")) or 
        ((tabuleiro[1][4]=="O") and (tabuleiro[2][4]=="O") and (tabuleiro[3][4]=="O") and (tabuleiro[4][4]== "O"))):
        # Varredura coluna 4
        vitoria=1

        
    #Varreduta das colunas
    
    #Varredura das colunas combinaçao X
    elif (((tabuleiro[0][0]=="X") and (tabuleiro[0][1]=="X") and (tabuleiro[0][2]=="X") and (tabuleiro[0][3]=="X")) or 
        ((tabuleiro[0][1]=="X") and (tabuleiro[0][2]=="X") and (tabuleiro[0][3]=="X") and (tabuleiro[0][4]== "X")) or
        # Varredura coluna 0
        ((tabuleiro[1][0]=="X") and (tabuleiro[1][1]=="X") and (tabuleiro[1][2]=="X") and (tabuleiro[1][3]=="X")) or 
        ((tabuleiro[1][1]=="X") and (tabuleiro[1][2]=="X") and (tabuleiro[1][3]=="X") and (tabuleiro[1][4]== "X")) or
        # Varredura coluna 1
        ((tabuleiro[2][0]=="X") and (tabuleiro[2][1]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[2][3]=="X")) or 
        ((tabuleiro[2][1]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[2][3]=="X") and (tabuleiro[2][4]== "X")) or
        # Varredura coluna 2
        ((tabuleiro[3][0]=="X") and (tabuleiro[3][1]=="X") and (tabuleiro[3][2]=="X") and (tabuleiro[3][3]=="X")) or 
        ((tabuleiro[3][1]=="X") and (tabuleiro[3][2]=="X") and (tabuleiro[3][3]=="X") and (tabuleiro[3][4]== "X")) or
        # Varredura coluna 3
        ((tabuleiro[4][0]=="X") and (tabuleiro[4][1]=="X") and (tabuleiro[4][2]=="X") and (tabuleiro[4][3]=="X")) or 
        ((tabuleiro[4][1]=="X") and (tabuleiro[4][2]=="X") and (tabuleiro[4][3]=="X") and (tabuleiro[4][4]== "X"))):
        # Varredura coluna 4
        vitoria=1
    
    #Varredura das colunas combinaçao O    
    elif (((tabuleiro[0][0]=="O") and (tabuleiro[0][1]=="O") and (tabuleiro[0][2]=="O") and (tabuleiro[0][3]=="O")) or 
        ((tabuleiro[0][1]=="O") and (tabuleiro[0][2]=="O") and (tabuleiro[0][3]=="O") and (tabuleiro[0][4]== "O")) or
        # Varredura coluna 0
        ((tabuleiro[1][0]=="O") and (tabuleiro[1][1]=="O") and (tabuleiro[1][2]=="O") and (tabuleiro[1][3]=="O")) or 
        ((tabuleiro[1][1]=="O") and (tabuleiro[1][2]=="O") and (tabuleiro[1][3]=="O") and (tabuleiro[1][4]== "O")) or
        # Varredura coluna 1
        ((tabuleiro[2][0]=="O") and (tabuleiro[2][1]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[2][3]=="O")) or 
        ((tabuleiro[2][1]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[2][3]=="O") and (tabuleiro[2][4]== "O")) or
        # Varredura coluna 2
        ((tabuleiro[3][0]=="O") and (tabuleiro[3][1]=="O") and (tabuleiro[3][2]=="O") and (tabuleiro[3][3]=="O")) or 
        ((tabuleiro[3][1]=="O") and (tabuleiro[3][2]=="O") and (tabuleiro[3][3]=="O") and (tabuleiro[3][4]== "O")) or
        # Varredura coluna 3
        ((tabuleiro[4][0]=="O") and (tabuleiro[4][1]=="O") and (tabuleiro[4][2]=="O") and (tabuleiro[4][3]=="O")) or 
        ((tabuleiro[4][1]=="O") and (tabuleiro[4][2]=="O") and (tabuleiro[4][3]=="O") and (tabuleiro[4][4]== "O"))):
        # Varredura coluna 4
        vitoria=1

        
    #Varreduta das diagonais
    
    #Varredura das diagonais combinaçao X
    
    elif (((tabuleiro[0][0]=="X") and (tabuleiro[1][1]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[3][3]=="X")) or 
        ((tabuleiro[1][1]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[3][3]=="X") and (tabuleiro[4][4]== "X")) or
        # Varredura diagonal principal
        ((tabuleiro[1][0]=="X") and (tabuleiro[2][1]=="X") and (tabuleiro[3][2]=="X") and (tabuleiro[4][3]=="X")) or 
        ((tabuleiro[0][1]=="X") and (tabuleiro[1][2]=="X") and (tabuleiro[2][3]=="X") and (tabuleiro[3][4]== "X")) or
        # Varredura diagonais adjascentes
        ((tabuleiro[4][0]=="X") and (tabuleiro[3][1]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[1][3]=="X")) or 
        ((tabuleiro[0][4]=="X") and (tabuleiro[1][3]=="X") and (tabuleiro[2][2]=="X") and (tabuleiro[3][1]== "X")) or
        #Varredura diagonal principal oposta
        ((tabuleiro[3][0]=="X") and (tabuleiro[2][1]=="X") and (tabuleiro[1][2]=="X") and (tabuleiro[0][3]=="X")) or 
        ((tabuleiro[4][1]=="X") and (tabuleiro[3][2]=="X") and (tabuleiro[2][3]=="X") and (tabuleiro[1][4]== "X"))):
        # Varredura diagonais adjascentes
        vitoria=1
        
    #Varredura das diagonais combinaçao O
    
    elif (((tabuleiro[0][0]=="O") and (tabuleiro[1][1]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[3][3]=="O")) or 
        ((tabuleiro[1][1]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[3][3]=="O") and (tabuleiro[4][4]== "O")) or
        # Varredura diagonal principal
        ((tabuleiro[1][0]=="O") and (tabuleiro[2][1]=="O") and (tabuleiro[3][2]=="O") and (tabuleiro[4][3]=="O")) or 
        ((tabuleiro[0][1]=="O") and (tabuleiro[1][2]=="O") and (tabuleiro[2][3]=="O") and (tabuleiro[3][4]== "O")) or
        # Varredura diagonais adjascentes
        ((tabuleiro[4][0]=="O") and (tabuleiro[3][1]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[1][3]=="O")) or 
        ((tabuleiro[0][4]=="O") and (tabuleiro[1][3]=="O") and (tabuleiro[2][2]=="O") and (tabuleiro[3][1]== "O")) or
        #Varredura diagonal principal oposta
        ((tabuleiro[3][0]=="O") and (tabuleiro[2][1]=="O") and (tabuleiro[1][2]=="O") and (tabuleiro[0][3]=="O")) or 
        ((tabuleiro[4][1]=="O") and (tabuleiro[3][2]=="O") and (tabuleiro[2][3]=="O") and (tabuleiro[1][4]== "O"))):
        # Varredura diagonais adjascentes
        vitoria=1

    #Detectar empate

    elif ((tabuleiro[0][0]!=" ") and (tabuleiro[0][1]!=" ") and (tabuleiro[0][2]!=" ") and (tabuleiro[0][3]!=" ") and (tabuleiro[0][4]!=" ") and
          (tabuleiro[1][0]!=" ") and (tabuleiro[1][1]!=" ") and (tabuleiro[1][2]!=" ") and (tabuleiro[1][3]!=" ") and (tabuleiro[1][4]!=" ") and
          (tabuleiro[2][0]!=" ") and (tabuleiro[2][1]!=" ") and (tabuleiro[2][2]!=" ") and (tabuleiro[2][3]!=" ") and (tabuleiro[2][4]!=" ") and
          (tabuleiro[3][0]!=" ") and (tabuleiro[3][1]!=" ") and (tabuleiro[3][2]!=" ") and (tabuleiro[3][3]!=" ") and (tabuleiro[3][4]!=" ") and
          (tabuleiro[4][0]!=" ") and (tabuleiro[4][1]!=" ") and (tabuleiro[4][2]!=" ") and (tabuleiro[4][3]!=" ") and (tabuleiro[4][4]!=" ")) :
        vitoria=2
        
    return(vitoria)
                 
def jogo():
    v=0
    d=0
    pt=0
    vencedor=0
    Player1=0
    Player2=0
    
    os.system("cls")#Apaga o terminal
    #print ("\n" * 120) 
                    
    tabuleiro=criartabuleiro() #Funçao para criar o tabuleiro em branco
    
    while(1):
        jog1=(input("Digite o nome do player 1: ")) #Pede o nome do usuario 1
        if os.path.isfile(f"{jog1}.csv") == True: #Verifica se o jogador existe
            break
        else:
            print("Usuario inexistente,digite um usuario valido\n\n\n")
            continue
    
    while(1):
        jog2=(input("Digite o nome do player 2: ")) #Pede o nome do usuario 1
        if os.path.isfile(f"{jog2}.csv") == True: #Verifica se o jogador existe
            break
        else:
            print("Usuario inexistente,digite um usuario valido\n\n\n")
            continue
    
    os.system("cls")#Apaga o terminal
    tabuleiro=criartabuleiro() #Funçao para criar o tabuleiro em branco    
    
    while(vencedor==0):
        p1=0
        p2=0


################################### Jogador 1 #######################
        while p1==0:
            X1=int(input("\nPlayer 1\nDigite a coluna: ")) #Coordenada da coluna
            X2=int(input("Digite a linha: ")) #Coordenada da linha
           
            if X1<5 and X2<5:#Verifica se a posição é valida
                if tabuleiro[X1][X2]==" ": #Verifica se a posiçao esta livre 
                    tabuleiro[X1][X2]="X" #Colocaçao da peça no tabuleiro na posiçao indicada
                    p1=1 #Flag que identirica a conclussao da jogada
                else:
                    print("\nCoordenada ja oculpada") # Mensagem de posiçao oculpada
            else:
                    print("\nCoordenada invalida, escolha outra") # Mensagem de posiçao invalida
        
       
        vencedor=varredura(tabuleiro) #Verifica se ouve vitoria
        
        if vencedor == 1  : # Sai do loop caso detecte a flag indicando vencedor
            Player1=1
            os.system("cls")#Apaga o terminal
            #print ("\n" * 120)
            break
        elif vencedor==0: #Verifica se ninguem venceu ou empatou
            
################################### Jogador 2 #######################

            while p2==0:
                O1=int(input("\nPlayer 2\nDigite a coluna: ")) #Coordenada da coluna
                O2=int(input("Digite a linha: ")) #Coordenada da linha
                
                if O1<5 and O2<5:#Verifica se a posição é valida
                    if tabuleiro[O1][O2]==" "  and O1<5 and O2<5: #Verifica se a posiçao esta livre
                        tabuleiro[O1][O2]="O" #Colocaçao da peça no tabuleiro na posiçao indicada
                        p2=1 #Flag que identirica a conclussao da jogada
                    else:
                        print("\nCoordenada ja oculpada ou invalida, escolha outra") # Mensagem de posiçao oculpada
        
                else:
                    print("\nCoordenada invalida, escolha outra") # Mensagem de posiçao invalida
        
        vencedor=varredura(tabuleiro) #Verifica se ouve vitoria
        
        if vencedor == 1: # Sai do loop caso detecte a flag indicando vencedor
            Player2=1
            os.system("cls")#Apaga o terminal
            #print ("\n" * 120)
            break
        
        elif vencedor == 2:
            empate=1
            os.system("cls")#Apaga o terminal
            #print ("\n" * 120)
            break
        else:
            os.system("cls")
            #print ("\n" * 120) 
            vencedor=varredura(tabuleiro) #Verifica se ouve vitoria
            atualizatabuleiro(tabuleiro)

################################### Mensagem vitoria/empate #######################    
    atualizatabuleiro(tabuleiro)
    
######################################### Vitoria Player 1 ########################    

    if Player1 ==1:
        print(" ".center(70),"\nParabens, o Player 1 ganhou\n")#Mensagem de vitoria player 1
        
###################################################################################        
        
        data=pd.read_csv(f'{jog1}.csv')#Le arquivo do jogador 1
        
        for i in data["vitorias"]: #Faz a somatoria de vitorias
            if i == 'Vitoria':
                v+=1
            pt+=1
                
        for i in data["derrotas"]: #Faz a somatoria de vitorias
            if i == 'Derrota':
                d+=1
                
        row=[pt+1,"Vitoria","-",v+1,d]#Cria nova linha de historico
        data.loc[len(data)]=row
        data.to_csv(f'{jog1}.csv', index=False)#Registra vitoria do jogador 1
        
        v=0
        d=0
        pt=0
        
 ###################################################################################    
        
        data2=pd.read_csv(f'{jog2}.csv')#Le arquivo do jogador 2
        
        for i in data2["vitorias"]:
            if i == 'Vitoria':
                v+=1
            pt+=1
                
        for i in data2["derrotas"]:
            if i == 'Derrota':
                d+=1
                
        row=[pt+1,"-","Derrota",v,d+1]#Cria nova linha de historico
        data2.loc[len(data2)]=row
        data2.to_csv(f'{jog2}.csv', index=False)#Registra vitoria do jogador 2
        
        v=0
        d=0
        pt=0

######################################### Vitoria Player 2 ########################    
        
    elif Player2 ==1:
        print(" ".center(70),"\nParabens, o Player 2 ganhou\n")
        
###################################################################################        
        
        data=pd.read_csv(f'{jog1}.csv')#Le arquivo do jogador 1
        
        for i in data["vitorias"]: #Faz a somatoria de vitorias
            if i == 'Vitoria':
                v+=1
            pt+=1
                
        for i in data["derrotas"]: #Faz a somatoria de derrotas
            if i == 'Derrota':
                d+=1
                
        row=[pt+1,"-","Derrota",v,d+1]#Cria nova linha de historico
        data.loc[len(data)]=row
        data.to_csv(f'{jog1}.csv', index=False)#Registra vitoria do jogador 1
        
        v=0
        d=0
        pt=0
        
 ###################################################################################    
        
        data2=pd.read_csv(f'{jog2}.csv')#Le arquivo do jogador 2
        
        for i in data2["vitorias"]: #Faz a somatoria de vitorias
            if i == 'Vitoria':
                v+=1
            pt+=1
                
        for i in data2["derrotas"]: #Faz a somatoria de derrotas
            if i == 'Derrota':
                d+=1
                
        row=[pt+1,"Vitoria","-",v+1,d]#Cria nova linha de historico
        data2.loc[len(data2)]=row
        data2.to_csv(f'{jog2}.csv', index=False)#Registra vitoria do jogador 2
        
        v=0
        d=0
        pt=0
 
 ######################################### Empate ################################   
    
       
    elif empate ==1:
        print(" ".center(70),"\nEmpate\n")
        
        ###################################################################################        
        
        data=pd.read_csv(f'{jog1}.csv')#Le arquivo do jogador 1
        
        for i in data["vitorias"]: #Faz a somatoria de vitorias
            if i == 'Vitoria':
                v+=1
            pt+=1
                
        for i in data["derrotas"]: #Faz a somatoria de derrotas
            if i == 'Derrota':
                d+=1
                
        row=[pt+1,"-","-",v,d]#Cria nova linha de historico
        data.loc[len(data)]=row
        data.to_csv(f'{jog1}.csv', index=False)#Registra vitoria do jogador 1
        
        v=0
        d=0
        pt=0
        
 ###################################################################################    
        
        data2=pd.read_csv(f'{jog2}.csv')#Le arquivo do jogador 2
        
        for i in data2["vitorias"]: #Faz a somatoria de vitorias
            if i == 'Vitoria':
                v+=1
            pt+=1
                
        for i in data2["derrotas"]: #Faz a somatoria de derrotas
            if i == 'Derrota':
                d+=1
                
        row=[pt+1,"-","-",v,d]#Cria nova linha de historico
        data2.loc[len(data2)]=row
        data2.to_csv(f'{jog2}.csv', index=False)#Registra vitoria do jogador 2
        
        v=0
        d=0
        pt=0
            
    input(" ".center(70)+"Pressione ENTER para continuar") # Solicita apertar o botao enter para continuar
        
        
    return 
    
    

def main():
 
    while(1):
        os.system("cls")#Apaga o terminal
        #print ("\n" * 120) #Apaga o terminal
        x= int(input(" ".center(70)+"O que deseja fazer \n\n 1 - Criar um novo jogador / usuário \n 2 - Exibir histórico de um jogador \n 3 - Excluir um jogador / usuário \n 4 - Iniciar uma partida\n 5 - Sair do jogo \n\n"))

        if x==1:    #Criar novo jogador
            
            criarusuario()
 
        elif x==2:  #Exibir Historico
            
            historico()
     

        elif x==3:  #Excluir um jogador
            
            excluir()
       

        elif x==4:  #Iniciar Partida
            
            jogo()
            
        elif x==5:  #fechar jogo
            
            fechar()
                
    return
         
      
if __name__=='__main__':
    import sys
    import os
    import pandas as pd
    main()
    

     
    

    