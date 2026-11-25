class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

    def descricao(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) | {status}"


class Usuario:
    limite_livros = 5
    prazo_emprestimo = 7

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []

    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= self.limite_livros:
            print(f"{self.nome} já atingiu o limite de {self.limite_livros} livros.")
            return False

        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print(
                f"{self.nome} pegou '{livro.titulo}' "
                f"(prazo: {self.prazo_emprestimo} dias)."
            )
            return True

        print(f"O livro '{livro.titulo}' está indisponível.")
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu '{livro.titulo}'.")
            return True

        print(f"{self.nome} não possui o livro '{livro.titulo}'.")
        return False


class Aluno(Usuario):
    prazo_emprestimo = 7


class Professor(Usuario):
    prazo_emprestimo = 30


# Exemplo de uso
livro = Livro("A garota do calendário fevereiro", "Audrey Carlan", "123456789")
aluno = Aluno("Maria", "2026001")

print(livro.descricao())
aluno.pegar_livro(livro)
print(livro.descricao())
aluno.devolver_livro(livro)
print(livro.descricao())
