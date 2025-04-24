class Teacher:
  def __init(self, first, last, subject, students)__:
    self.nameFirst = first #string
    self.nameLast = last #string
    self.subject = subject # string
    self.students = students #double array: index 1 is period, index 2 is student in period

  def addStudent(self, student, period):
    self.students[period-1].append(student)
