student_scores = [85, 92, 78, 96, 88, 79, 95, 91, 87, 84]

# Using sum() function to calculate total scores
total_exam_scores = sum(student_scores)

# Using max() function to find the highest score
total_exam_scores = max(student_scores)

# Calculating total score using a for loop
sum = 0
for score in student_scores:
  
  sum += score
  
print(f"Highest score in the class: {total_exam_scores}")
  
print(f"Total score calculated using for loop: {sum}")

max_score = 0
for score2 in student_scores:
  if score2 > max_score:
    max_score = score2
print(f"New highest score found: {max_score}")