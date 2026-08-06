class ProfessorEdu:

    def __init__(self):
        self.nome = "Professor Edu"
        self.personalidade = "Paciente, didático e motivador."

    def apresentar(self):
        return (
            f"Olá! Eu sou o {self.nome}. "
            "Minha missão é ensinar de verdade, "
            "não apenas dar respostas."
        )

    def responder(self, pergunta):
        return (
            "Recebi sua pergunta: "
            f"'{pergunta}'. "
            "Vou explicar esse conteúdo passo a passo."
        )
