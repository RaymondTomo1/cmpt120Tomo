#- This program will allow quizzes to get graded based on what score the user inputs
def main():
    score= eval(input("Input a score between 0 and 5 in quotes:"))
    print (score)
    score= score.replace ("5", "A")
    score= score.replace ("4", "B")
    score= score.replace ("3", "C")
    score= score.replace ("2", "D")
    score= score.replace ("1", "F")
    score= score.replace ("0", "F")
    print (score)
main()
