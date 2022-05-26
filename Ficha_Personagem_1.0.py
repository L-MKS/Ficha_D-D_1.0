class npc:
    def __init__(self, classe, raca, nivel, genero, name):
        self.classe = classe
        self.raca = raca
        self.nivel = nivel
        self.genero = genero
        self.nome = name

    def imprime(self):
        if self.genero == "m":
            print("O {classe} é um {raça} nível {nivel}!".format(classe=self.classe,raça=self.raca,nivel=self.nivel))
        else:
            print("A {classe} é uma {raça} nível {nivel}!".format(classe=self.classe,raça=self.raca,nivel=self.nivel))

    def cria(self):
        c = False
        while c == False:
            self.classe = input("Digite a classe do personagem: ")
            if self.classe in classes:
                c = True
            else:
                print("Classe inválida. Escolha uma entre: {}".format(classes))
                continue
        r = False
        while r == False:
            self.raca = input("Digite a raca do personagem: ")
            if self.raca in racas:
                r = True
            else:
                print("Raca inválida. Escolha uma entre: {}".format(racas))
                continue
        n = False
        while n == False:
            self.nivel = input("Digite o nível do personagem: ")
            if int(self.nivel) >= 1 and int(self.nivel) <= 20:
                n = True
            else:
                print("Nível inválido. Escolha um valor entre 1 e 20.")
                continue
        g = False
        while g == False:
            self.genero = input("Digite o gênero do personagem: ")
            if self.genero in generos:
                g = True
            else:
                print("Gênero inválido. Escolha um entre {}".format(generos))
                continue
        a = False
        while a == False:
            self.nome = input("Digite o nome do seu personagem: ")
            if len(self.nome) >= 4 and len(self.nome) <= 15:
                a = True
            else:
                self.nome = input("O nome do seu personagem deve ter entre 4 e 15 caracteres.")
                continue
        print("Personagem adicionado!")

    def newGame(self):
        game = " "
        x = 0
        while x in range(1):
            game = input("Você deseja iniciar o jogo agora?: ")
            if game == "Começar":
                print("\n")
                print("Continuação em breve!")
                print("\n")
                x += 1
            else:
                print("\n")
                print("Por enquanto, somente existe a opção: Começar")
                print("\n")
                continue

classes = ["Bárbaro", "Guerreiro", "Mago", "Feiticeiro", "Ladino", "Monge", "Ranger"]
racas = ["Humano","Elfo","Anão","Halfling","Gnomo","Tiefling","Dragonborn"]
generos = ["Masculino", "Feminino"]

principal = npc("c","r",0,"n","n")
secundario = npc("c","r",0,"n","n")
print("\n")
print("Vamos criar os dois personagens que você utilizará no jogo. Por favor insira os dados abaixo:")
principal.cria()
print("\n")
print("O primeiro personagem foi criado! Agora insira os dados para criação do segundo personagem:")
secundario.cria()
print("\n")
print ("Parabéns, você criou seus dois personagens!")
print("{nome} é um {classe} {raca} nível {nivel}".format(nome=principal.nome,classe=principal.classe,raca=principal.raca,nivel=principal.nivel))
print("{nome} é um {classe} {raca} nível {nivel}".format(nome=secundario.nome,classe=secundario.classe,raca=secundario.raca,nivel=secundario.nivel))
print("\n")
principal.newGame()