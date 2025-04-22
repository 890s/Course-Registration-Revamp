class Course:
  def __init__(self, prereq="", gradeReq=[9,10,11,12], credit=[], teacher):
    self.prereqs = prereq
    self.gradeReqs = gradeReq
    self.credits = credit
    self.teacher = teacher
