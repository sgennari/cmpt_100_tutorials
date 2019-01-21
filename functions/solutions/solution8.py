def calculate_grade(is_elective, grade):
  """ (bool, int) -> object

  Precondition: 0 <= grade <= 100
  is_elective refers to True iff this course is being taken as an elective. Return the grade if the course is not   being taken as an elective, and either 'Pass' or 'Fail' (depending on whether grade is at least 50) if the   course is an elective.
 """
  if is_elective:
    if grade > 50:
      return 'pass'
    else:
      return 'fail'
  else:
    return grade