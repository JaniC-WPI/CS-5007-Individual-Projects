from ITExam import ITExam

class MultipleChoiceExam(ITExam):
    # class attribute
    POINTS_PER_QUESTION = 2

    # Initiating constructor for the child class
    def __init__(self):
        ITExam.__init__(self) # super class constructor
        self.__total_num_of_mc_ques = 0
        self.__correct_num_of_mc_ques = 0    
    
    # Setter method for instance variable
    def setTotalNumOfMCQuestion(self, total_num_of_mc_ques):        
        if total_num_of_mc_ques > 0:
            self.__total_num_of_mc_ques = total_num_of_mc_ques
            return True
            # print("Sorry! The number is not valid. Please enter it again.")
        else:
            
            return False
    
    # getter method for instance variable
    def getTotalNumOfMCQuestion(self):
        return self.__total_num_of_mc_ques
    
    # setter method for instance variable
    def setCorrectNumOfMCQuestion(self, correct_num_of_mc_ques):
        if 0 <= correct_num_of_mc_ques <= self.getTotalNumOfMCQuestion():
            self.__correct_num_of_mc_ques = correct_num_of_mc_ques
            return True
        else:
            return False
        
    # getter method for instance variable
    def getCorrectNumOfMCQuestion(self):
        return self.__correct_num_of_mc_ques
    
    # check condition from exam score to return the examgrade    
    def getExamGrade(self):
        exam_score = ((self.getCorrectNumOfMCQuestion() * MultipleChoiceExam.POINTS_PER_QUESTION) \
            / (self.getTotalNumOfMCQuestion() * MultipleChoiceExam.POINTS_PER_QUESTION)) * 100
        
        exam_grade = super().getExamGrade()
        return exam_grade
    
    # return the instance variables in string format    
    def toString(self):
        s = ITExam.toString(self)
        s += "\nTotal Number of MC Questions: " + str(self.getTotalNumOfMCQuestion())
        s += "\nTotal Number of Correct MC Questions: " + str(self.getCorrectNumOfMCQuestion())
        s += "\nFinal Grade: " + str(self.getExamGrade())
        
        return s

