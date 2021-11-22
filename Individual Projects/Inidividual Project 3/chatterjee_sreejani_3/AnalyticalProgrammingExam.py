from ITExam import ITExam

class AnalyticalProgrammingExam(ITExam):
    # class attributes
    MAX_SCORE = 100
    SHORT_ANSWER_PERCENT = 0.3
    PROGRAMMING_PERCENT = 0.7
    
    # Initiating constructor for the child class
    def __init__(self):        
        ITExam.__init__(self) # super class constructor

        # instance variables
        self.__short_ans_score = 0
        self.__prog_score = 0
    
    # setter method for instance variable
    def setShortAnswerScore(self, short_ans_score):
        if 0 < short_ans_score <= 100:
            self.__short_ans_score = short_ans_score
            return True
        else:
            return False

    # getter method for instance variable
    def getShortAnswerScore(self):
        return self.__short_ans_score
    
    # setter method for instance variable
    def setProgrammingScore(self, prog_score):
        if 0 < prog_score <= 100:
            self.__prog_score = prog_score
            return True
        else:
            False
    
    # getter method for instance variable
    def getProgrammingScore(self):
        return self.__prog_score
    
    # check condition from exam score to return the examgrade
    def getExamGrade(self):
        exam_score = (self.SHORT_ANSWER_PERCENT * self.getShortAnswerScore()) \
                        + (self.PROGRAMMING_PERCENT * self.getProgrammingScore())
        
        exam_grade = super().getExamGrade()
        return exam_grade

    # return the instance variables in string format        
    def toString(self):
        s = ITExam.toString(self)
        s += "\nShort Answer Score Is: " + str(self.getShortAnswerScore())
        s += "\nProgramming score is: " + str(self.getProgrammingScore())
        s += "\nFinal Grade: " + str(self.getExamGrade())
        
        return s



