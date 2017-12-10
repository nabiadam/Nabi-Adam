# CTI 110
# M6HW1: Test Average and Grades
# Nabi Adam
# 10/07/2017

def calc_Average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4+ score)/5
    return average
def determine_Grade(userScore):
    if(userScore < 60):
        return 'F'
    elif(userScore < 70):
        return 'D'
    elif(userScore < 80):
        return 'C'
    elif(userScore < 90):
        return 'D'
    elif(userScore < 101):
        return 'A'

def ask_For_Score():
    score1 = float (input('Enter score 1:'))
    score2 = float (input('Enter score 2:'))
    score3 = float (input('Enter score 3:'))
    score4 = float (input('Enter score 4:'))
    score5 = float (input('Enter score 5:'))
    return score1, score2, score3, score4, score5
def print_Table_Of_Results (score1, score2, score3, score4, score5):
    print ('Score\tLetter Grade')
    print(int(score1), '\t\t' + determine_Grade(score1))
    print(int(score2), '\t\t' + determine_Grade(score2))
    print(int(score3), '\t\t' + determine_Grade(score3))
    print(int(score4), '\t\t' + determine_Grade(score4))
    print(int(score5), '\t\t' + determine_Grade(score5))
    
def main ():
    score1, score2, score3, score4, score5 = ask_For_Score()
    print_Table_Of_Results (score1, score2, score3, score4, score5)
    
main()
    
