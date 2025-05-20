class Course:
    def __init__(self, name, internal, id, subject, prereqs=[], gradereq=[9,10,11,12]):
        self.name = name
        self.internal = internal
        self.id = id
        self.subject = subject
        self.prereqs = prereqs
        self.gradereq = gradereq
    
    def __str__(self):
        return self.name
