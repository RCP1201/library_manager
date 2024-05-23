#Projeto: Sistema de Biblioteca
#Descrição:
#Vamos criar um sistema simples de gerenciamento de biblioteca que permita ao usuário adicionar livros, visualizar todos os livros, emprestar livros e devolver livros.

#Funcionalidades:
#Adicionar um novo livro.
#Visualizar todos os livros disponíveis.
#Emprestar um livro.
#Devolver um livro.

#Requisitos:
#O programa deve solicitar ao usuário que escolha uma opção do menu principal.
#O programa deve armazenar os livros em uma lista de dicionários ou uma lista de objetos.
#Para emprestar um livro, o usuário deve inserir o título do livro.
#Para devolver um livro, o usuário deve inserir o título do livro.
#Após realizar uma operação, o programa deve exibir novamente o menu principal.
#Sugestões para a implementação:
#Use loops para exibir o menu principal e solicitar a entrada do usuário.
#Use listas para armazenar os livros.
#Utilize funções para organizar o código e realizar operações específicas (adicionar livro, exibir livros, emprestar livro, devolver livro).
#Considere usar um loop infinito para manter o programa em execução até que o usuário opte por sair.

import os

class Livros:
    def __init__(self, ):
        self.lista_de_disponiveis = ['Branca de neve', 'pinóquio', 'Lobo mal']
        self.lista_livros_emprestados = []
        #self.format = "\n".join(self.lista_de_disponiveis)

    def limpar_terminal(self):
        # Comando para limpar o terminal no Windows e Unix (Linux/MacOS)
        os.system('cls' if os.name == 'nt' else 'clear')
                   
    def opcao(self):
        print(
    "Escolha uma das opções de serviço\n\n",
    "1 - Mostra livros\n",
    "2 - Pegar um livro\n",
    "3 - Devolver um livro\n",
    "4 - Fechar biblioteca\n"
            )
        entrada_dados = input("Digite o numero do serviço desejado: ")
        return entrada_dados
    
    def lista_disponiveis(self): 
        self.limpar_terminal() 
        print(f"\nEsses são os livros disponíveis:\n{self.lista_de_disponiveis}\n")                             
        
    def livros_emprestar(self):
        self.limpar_terminal()
        print(f"\nAqui estão os livros disponíveis:\n{self.lista_de_disponiveis}")
        emprestar = input('Qual livro deseja pegar? ')
        if emprestar in self.lista_de_disponiveis:
           self.lista_de_disponiveis.remove(emprestar)
           self.lista_livros_emprestados.append(emprestar)
           print(f"\nEmpréstimo do livro '{emprestar}' realizado, pegue seu livro na recepção!\n")
        else:
            print("\nLivro não disponível, ou não existe!\n")
            
    def livros_devolver(self):
        self.limpar_terminal()
        devolver = input("\nDigite o nome do livro: ")
        if devolver in self.lista_livros_emprestados:
            self.lista_livros_emprestados.remove(devolver)
            self.lista_de_disponiveis.append(devolver)
            print(f"\nLivro '{devolver}' devolvido com sucesso!")
        else:
            print("\nEste livro não está emprestado ou não existe!")
            nova_consulta = input("\nDeseja devolver outro livro?\n 1 - Devolver outro livro\n 2 - Voltar ao menu principal ") 
            if nova_consulta == "1":      
                self.livros_devolver()
            else:
                self.limpar_terminal()
                self.opcao()
                
                
    def fecha(self):
        self.limpar_terminal()
        print("\nAté a próxima aventura!")
        global fecharapp
        fecharapp = "sim"


boas_vindas = print("Bem vindo a Biblioteca Paixão!\n")
fecharapp = "Não"
escolha = Livros()
       
while fecharapp.lower() =="não":
    opcao = escolha.opcao()
    if opcao == "1":
       escolha.lista_disponiveis()
       escolha2 = input("1 - Voltar\n2 - fechar\n\n ")
       if escolha2 == "1":
           fecharapp="Não"
           escolha.limpar_terminal()
       else:
          escolha.fecha()
    elif opcao == "2":
        escolha.livros_emprestar() 
    elif opcao == "3":
        escolha.livros_devolver()
    elif opcao == "4":
        escolha.fecha()
    else:
        print("\nOpção inválida!\n")


    


