from ITExam import ITExam

class TechnicalWritingExam(ITExam):
    # class attributes
    MAX_SCORE = 100
    GRAMMAR_PERCENT = 0.3
    SENTENCE_PERCENT = 0.3
    CONTENT_PERCENT = 0.4
    
    # Initiating constructor for the child class
    def __init__(self):
        ITExam.__init__(self) # Superclass constructor called by the child
        # initiating the instance attributes
        self.__grammar_score = 0
        self.__sentence_struct_score = 0
        self.__content_score = 0

    # Setting the instance variable grammar score as a boolean
    def setGrammarScore(self, grammar_score):
        if 0 < grammar_score <= 100:
            self.__grammar_score = grammar_score
            return True
        else:
            return False

    # Get the instance vaiable grammar score    
    def getGrammarScore(self):
        return self.__grammar_score
    
    # Setting the instance sentence structure score as a boolean
    def setSentenceStructureScore(self, sentence_struct_score):
        if 0 < sentence_struct_score <= 100:
            self.__sentence_struct_score = sentence_struct_score
            return True
        else:
            return False
    
    # Get the instance variable
    def getSentenceStructureScore(self):
        return self.__sentence_struct_score
    
    # Setting the instance variable content score as a boolean
    def setContentScore(self, content_score):
        if 0 < content_score <= 100:
            self.__content_score = content_score
            return True
        else:
            return False

    # get the instance variable
    def getContentScore(self):
        return self.__content_score
    
    # check condition from exam score to return the examgrade
    def getExamGrade(self):
        exam_score = (TechnicalWritingExam.GRAMMAR_PERCENT * self.getGrammarScore())\
             + (TechnicalWritingExam.SENTENCE_PERCENT * self.getSentenceStructureScore()) \
                  + (self.getContentScore() * TechnicalWritingExam.CONTENT_PERCENT)
        
        exam_grade = super().getExamGrade()
    
    # return the instance variables in string format
    def toString(self):
        s = ITExam.toString(self)
        s += "\nScore of Grammer Portion:: " + str(self.getGrammarScore())
        s += "\nScore of Sentence Structure Portion: " + str(self.getSentenceStructureScore())
        s += "\nScore of Content Portion: " + str(self.getContentScore())
        
        return s