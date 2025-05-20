class Student:
    def __init__(self, id, grade, courses, schedule=None):
        self.id = id
        self.grade = grade
        self.courses = courses
        self.schedule = schedule
        
    def setSchedule(self, schedule):
        self.schedule = schedule
        
    def getSchedule(self):
        return self.schedule
        
    def __str__(self):
        return self.id
