#Taks 1
print("Task 1: ")
def calculateGPA(grades, credits):


  total_points = 0
  total_credits = 0
  for grade, credit in zip(grades, credits):
    grade_points = translateLetter(grade)
    total_points += grade_points * credit
    total_credits += credit
  return total_points / total_credits


def translateLetter(letter):

  translation_table = {
      'A+': 4.3,
      'A': 4.0,
      'A-': 3.7,
      'B+': 3.3,
      'B': 3.0,
      'B-': 2.7,
      'C+': 2.3,
      'C': 2.0,
      'C-': 1.7,
      'D+': 1.3,
      'D': 1.0,
      'D-': 0.7
  }

  return translation_table.get(letter, 0.0)


def translatePercentage(percentage):

  if percentage >= 95:
    return 'A+'
  elif percentage >= 90:
    return 'A'
  elif percentage >= 85:
    return 'A-'
  elif percentage >= 80:
    return 'B+'
  elif percentage >= 75:
    return 'B'
  elif percentage >= 70:
    return 'B-'
  elif percentage >= 65:
    return 'C+'
  elif percentage >= 60:
    return 'C'
  elif percentage >= 55:
    return 'C-'
  elif percentage >= 50:
    return 'D+'
  elif percentage >= 45:
    return 'D'
  elif percentage >= 40:
    return 'D-'
  else:
    return 'F'



grades = ['A+', 'B-', 'C+', 'D+', 'B']
credits = [4, 3, 4, 5, 3]

gpa = calculateGPA(grades, credits)
print(f'GPA: {gpa}')
print("task 2")
import os
def readCredits():
    credits = []
    with open('grades/credits.txt', 'r') as f:
        for line in f:
            credits.append(int(line.strip()))
    return credits
def readAndTranslateScores(filename, translateFunc):
    scores = []
    with open('grades/' + filename, 'r') as f:
        for line in f:
            score = line.strip()
            points = translateFunc(score)
            scores.append(points)
    return scores
def calculateStudentGPA(credits, *scores):
    total_points = 0
    total_credits = sum(credits)
    for i in range(len(scores)):
        total_points += scores[i] * credits[i]
    gpa = total_points / total_credits
    return round(gpa, 2)
credits = readCredits()
math_scores = readAndTranslateScores('math.txt', translateLetter)
chemistry_scores = readAndTranslateScores('chemistry.txt', translatePercentage)
english_scores = readAndTranslateScores('english.txt', translatePercentage)
gpas = []
for i in range(len(math_scores)):
    math_score = math_scores[i]
    chemistry_score = chemistry_scores[i]
    english_score = english_scores[i]
    gpa = calculateStudentGPA(credits, math_score, chemistry_score, english_score)
    gpas.append(gpa)
with open('grades/overallGPAs.txt', 'w') as f:
    for gpa in gpas:
        f.write(str(gpa) + '')
overall_gpa = calculateGPA(*gpas, *credits)
print('Overall GPA:', overall_gpa)
# 4.What is API? What are the use cases of API? Give an example with code snippets of using API with Python. What are the limitations of API?
# Application Programming Interface (API) is a software interface that allows two applications to interact with each other without any user intervention.
# API is a collection of software functions and procedures. In simple terms, API means a software code that can be accessed or executed.
# API is defined as a code that helps two different software’s to communicate and exchange data with each other.
# 5.What is socket? What are the use cases of sockets? Give an example with code snippets of using sockets with Python.
# A Python socket is a module in Python that provides a way for two computers to communicate.
# It’s like a virtual postman, delivering messages between two nodes on a network.
# Here’s a simple example of a Python socket: import socket s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) s.connect('localhost', 12345)
# Output: # Establishes a connection to the server at localhost on port 12345.
