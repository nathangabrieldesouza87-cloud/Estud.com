class StudentMemory:

    def __init__(self):

        self.history=[]

        self.subjects={}

    def save(self,question):

        self.history.append(question)

    def register_subject(self,subject):

        if subject not in self.subjects:

            self.subjects[subject]=0

        self.subjects[subject]+=1
