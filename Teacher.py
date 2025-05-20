class Teacher:
    def __init__(self, name, subject, periods, classes=[]):
        self.name = name
        self.subject = subject
        self.classes = classes
        self.periods = periods
        
    def getClass(self, period):
        return self.periods[period-1]
        
    def addStudent(self, student, period):
        self.periods[period-1].append(student)
        
    def __str__(self):
        return self.name
