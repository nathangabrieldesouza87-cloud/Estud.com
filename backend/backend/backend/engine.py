from classifier import classify
from personality import PERSONALITY

class EstudEngine:

    def build_prompt(self,question):

        subject=classify(question)

        prompt=f"""
{PERSONALITY}

Matéria:

{subject}

Pergunta:

{question}

Explique como um professor excelente.
"""

        return prompt
