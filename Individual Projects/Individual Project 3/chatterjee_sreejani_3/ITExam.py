class ITExam:
    MAX_SCORE = 100
    # Creating the Constructor for the Parent Class
    def __init__(self):        
        self.__exam_title = None
        self.__exam_score = 0
    
    # Setting the examtitle to return a boolean 
    def setExamTitle(self, exam_title):
        if len(exam_title) == 0:
            return False
        else:
            self.__exam_title = exam_title
            return True

    # get the exam title
    def getExamTitle(self):
        return self.__exam_title
    
    # Setting the exam score to return a boolean
    def setExamScore(self, exam_score):
        if 0 <= exam_score <= ITExam.MAX_SCORE:
            self.__exam_score = exam_score
            return True
        else:            
            return False

    # get the exam score
    def getExamScore(self):
        return self.__exam_score
    
    # check condition from exam score to return the examgrade
    def getExamGrade(self):
        if self.getExamScore() >= 90:
            exam_grade = 'A'
        elif self.getExamScore() >= 80:
            exam_grade = 'B'
        elif self.getExamScore() >= 70:
            exam_grade = 'C'
        elif self.getExamScore() >= 60:
            exam_grade = 'D'
        else:
            exam_grade = 'F'
        
        return exam_grade
    
    # returns the instance variables in string format
    def toString(self):
        s = ""
        s += "\nExam Title: " + self.getExamTitle()
        s += "\nExam Score: " + str(self.getExamScore())
        
        return s


