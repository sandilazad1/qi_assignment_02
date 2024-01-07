def calculate_grade_base_on_percentage(num):
       if (num>=80):
          print("A+")
       elif num <= 79 and num >= 70:
          print("A")
       elif num <= 69 and num >= 60:
          print("A-")
       elif num <= 59 and num >= 50:
          print("B")
       elif num <= 49 and num >= 40:
          print("C")
       elif num <= 39 and num >= 33:
          print("D")
       else:
          print("Failed")

calculate_grade_base_on_percentage(12)