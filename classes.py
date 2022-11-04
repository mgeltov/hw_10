class Candidate:

    def __init__(self, pk, name, picture, position, gender, age, skills):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

    def get_pk(self):
        return self.pk

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_skills(self):
        return self.skills

    def get_all(self):
        return self.pk, self.name, self.picture, self.position, self.gender, self.age, self.skills

    def get_by_pk(self, pk):
        return self.pk, self.name, self.picture, self.position, self.gender, self.age, self.skills