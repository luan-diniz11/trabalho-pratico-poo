from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def __str__(self):
        pass

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"'{self.titulo}' por {self.autor} ({self.ano}) - {status}"

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"{self.nome} emprestou o livro '{livro.titulo}'.")
        elif not livro.disponivel:
            print(f"O livro '{livro.titulo}' não está disponível.")
        else:
            print("Limite de empréstimos atingido (máximo 3).")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
        else:
            print(f"O livro '{livro.titulo}' não está emprestado por {self.nome}.")

    def __str__(self):
        return f"Usuário: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}"

class Administrador(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def cadastrar_livro(self, titulo, autor, ano):
        return Livro(titulo, autor, ano)

    def __str__(self):
        return f"Administrador: {self.nome}, Idade: {self.idade}"

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)

def exibir_livros_disponiveis(livros):
    print("\nLivros Disponíveis:")
    for livro in livros:
        if livro.disponivel:
            print(livro)

def exibir_usuarios_com_livros(usuarios):
    print("\nUsuários com livros emprestados:")
    for usuario in usuarios:
        if usuario.livros_emprestados:
            print(f"{usuario.nome} possui:")
            for livro in usuario.livros_emprestados:
                print(f"  - {livro.titulo}")

def sistema_biblioteca():
    admin = Administrador("Carlos", 40)
    livros = []
    usuarios = []

    while True:
        print("\nSistema de Biblioteca Virtual")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Exibir livros disponíveis")
        print("6. Exibir usuários com livros emprestados")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            livros.append(admin.cadastrar_livro(titulo, autor, ano))
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        
        elif opcao == "2":
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            matricula = input("Digite o número de matrícula: ")
            usuarios.append(UsuarioComum(nome, idade, matricula))
            print(f"Usuário '{nome}' cadastrado com sucesso!")
        
        elif opcao == "3":
            nome_usuario = input("Digite o nome do usuário: ")
            titulo_livro = input("Digite o título do livro: ")
            usuario = next((u for u in usuarios if u.nome == nome_usuario), None)
            livro = next((l for l in livros if l.titulo == titulo_livro), None)
            if usuario and livro:
                usuario.emprestar_livro(livro)
            else:
                print("Usuário ou livro não encontrado.")
        
        elif opcao == "4":
            nome_usuario = input("Digite o nome do usuário: ")
            titulo_livro = input("Digite o título do livro: ")
            usuario = next((u for u in usuarios if u.nome == nome_usuario), None)
            livro = next((l for l in livros if l.titulo == titulo_livro), None)
            if usuario and livro:
                usuario.devolver_livro(livro)
            else:
                print("Usuário ou livro não encontrado.")
        
        elif opcao == "5":
            exibir_livros_disponiveis(livros)
        
        elif opcao == "6":
            exibir_usuarios_com_livros(usuarios)
        
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

sistema_biblioteca()
