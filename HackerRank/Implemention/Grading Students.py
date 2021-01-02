def gradingStudents(grades):
    answer = []

    for grade in grades:
    	if grade < 38 or (grade % 5 < 3):
    		 score = grade
    	else:
    		mod_num = grade % 5
    		round_num = 5 - mod_num
    		score = grade + round_num
    	answer.append(score)
    print(answer)

dene = [73, 67, 38, 33]
gradingStudents(dene)