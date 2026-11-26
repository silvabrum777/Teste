class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if not self.disponivel:
            raise Exception(f"O livro '{self.titulo}' já está emprestado.")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            raise Exception(f"O livro '{self.titulo}' já está na biblioteca.")
        self.disponivel = True

    def descricao(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [{status}]"


class Usuario:
    limite_livros = 5
    prazo_emprestimo = 14

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []

    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= self.limite_livros:
            raise Exception(f"{self.nome} atingiu o limite de {self.limite_livros} livros.")

        livro.emprestar()
        self.livros_emprestados.append(livro)
        print(f"{self.nome} pegou '{livro.titulo}' (prazo: {self.prazo_emprestimo} dias).")

    def devolver_livro(self, livro):
        if livro not in self.livros_emprestados:
            raise Exception(f"{self.nome} não está com o livro '{livro.titulo}'.")

        livro.devolver()
        self.livros_emprestados.remove(livro)
        print(f"{self.nome} devolveu '{livro.titulo}'.")


class Aluno(Usuario):
    limite_livros = 3
    prazo_emprestimo = 7

    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso


class Professor(Usuario):
    limite_livros = 10
    prazo_emprestimo = 30

    def __init__(self, nome, matricula, departamento):
        super().__init__(nome, matricula)
        self.departamento = departamento


# --- Dados iniciais com livros reais ---
livros = [
    Livro("Dom Casmurro", "Machado de Assis", "978-8535914849"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "978-8595081512"),
    Livro("1984", "George Orwell", "978-8535914840"),
    Livro("A Hora da Estrela", "Clarice Lispector", "978-8532530837"),
    Livro("Capitães da Areia", "Jorge Amado", "978-8535914061")
]

usuarios = [
    Aluno("Maria", "2026001", "Letras"),
    Professor("Carlos", "PROF01", "História")
]


# --- Menu simples no terminal ---
while True:
    print("\n--- MENU BIBLIOTECA ---")
    print("1 - Ver livros")
    print("2 - Pegar livro emprestado")
    print("3 - Devolver livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            print("\nAcervo:")
            for i, livro in enumerate(livros):
                print(f"{i} - {livro.descricao()}")

        elif opcao == "2":
            print("\nUsuários:")
            for i, u in enumerate(usuarios):
                print(f"{i} - {u.nome} ({type(u).__name__})")
            idx_usuario = int(input("Número do usuário: "))

            print("\nLivros:")
            for i, livro in enumerate(livros):
                print(f"{i} - {livro.descricao()}")
            idx_livro = int(input("Número do livro: "))

            usuarios[idx_usuario].pegar_livro(livros[idx_livro])

        elif opcao == "3":
            print("\nUsuários:")
            for i, u in enumerate(usuarios):
                print(f"{i} - {u.nome} ({type(u).__name__})")
            idx_usuario = int(input("Número do usuário: "))

            print("\nLivros:")
            for i, livro in enumerate(livros):
                print(f"{i} - {livro.descricao()}")
            idx_livro = int(input("Número do livro: "))

            usuarios[idx_usuario].devolver_livro(livros[idx_livro])

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: digite apenas números para escolher.")
    except IndexError:
        print("Erro: número de usuário ou livro não existe na lista.")
    except Exception as erro:
        print(f"Erro na operação: {erro}")