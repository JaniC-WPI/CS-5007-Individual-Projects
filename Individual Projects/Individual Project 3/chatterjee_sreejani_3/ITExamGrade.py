from ITExam import ITExam
from MultipleChoiceExam import MultipleChoiceExam
from AnalyticalProgrammingExam import AnalyticalProgrammingExam
from TechnicalWritingExam import TechnicalWritingExam

obj_list = []

def fillITExam(oneExamObject):
    global obj_list
    # check if object belongs to class, validate the instance variables and assign computed score as an instance attribute
    if isinstance(oneExamObject, MultipleChoiceExam):
        mcq_loop = True
        cq_loop = True
        while mcq_loop:
            total_mcq = int(input("Total Number of Multiple Choice's Questions: "))
            if not oneExamObject.setTotalNumOfMCQuestion(total_mcq):
               print("Sorry! The number is not valid. Please enter it again.")
            else:
                mcq_loop = False
        while cq_loop:
            total_cq = int(input("Total Number of Correct Multiple Choice's Questions: "))
            if not oneExamObject.setCorrectNumOfMCQuestion(total_cq):
               print("Sorry! The number is not valid. Please enter it again.")
            else:
                cq_loop = False
                oneExamObject.setExamScore(((oneExamObject.getCorrectNumOfMCQuestion() * \
                     MultipleChoiceExam.POINTS_PER_QUESTION) \
            / (oneExamObject.getTotalNumOfMCQuestion() * MultipleChoiceExam.POINTS_PER_QUESTION)) * 100)

    # check if object belongs to class, validate the instance variables and assign computed score as an instance attribute
    elif isinstance(oneExamObject, AnalyticalProgrammingExam):
        short_ans_loop = True
        prog_loop = True
        while short_ans_loop:
            short_ans_score = float(input("Score of Short Answer Section: "))
            if not oneExamObject.setShortAnswerScore(short_ans_score):
               print("Sorry! The number is not valid. Please enter it again.")
            else:
                short_ans_loop = False
        while prog_loop:
            prog_score = float(input("Score of Programming Section: "))
            if not oneExamObject.setProgrammingScore(prog_score):
               print("Sorry! The number is not valid. Please enter it again.")
            else:
                prog_loop = False
                oneExamObject.setExamScore(((AnalyticalProgrammingExam.SHORT_ANSWER_PERCENT * oneExamObject.getShortAnswerScore()) \
                        + (AnalyticalProgrammingExam.PROGRAMMING_PERCENT * oneExamObject.getProgrammingScore())))

    # check if object belongs to class, validate the instance variables and assign computed score as an instance attribute    
    elif isinstance(oneExamObject, TechnicalWritingExam):
            grammar_loop = True
            sentence_loop = True
            content_loop = True
            while grammar_loop:
                grammar_score = float(input("Score of Grammar Portion: "))
                if not oneExamObject.setGrammarScore(grammar_score):
                    print("Sorry! The number is not valid. Please enter it again.")
                else:
                    grammar_loop = False
            while sentence_loop:
                sentence_score = float(input("Score of Sentence Structure Portion: "))
                if not oneExamObject.setSentenceStructureScore(sentence_score):
                    print("Sorry! The number is not valid. Please enter it again.")
                else:
                    sentence_loop = False
            
            while content_loop:
                content_score = float(input("Score of Content Portion: "))
                if not oneExamObject.setContentScore(content_score):
                    print("Sorry! The number is not valid. Please enter it again.")
                else:
                    content_loop = False
                    oneExamObject.setExamScore((((TechnicalWritingExam.GRAMMAR_PERCENT * oneExamObject.getGrammarScore())\
             + (TechnicalWritingExam.SENTENCE_PERCENT * oneExamObject.getSentenceStructureScore()) \
                  + (oneExamObject.getContentScore() * TechnicalWritingExam.CONTENT_PERCENT))))

    obj_list.append(oneExamObject) # save the objects in a list to be used for display results


def displayResults(allExamsList):
    total_score = 0
    for obj in allExamsList: # loop through the list of objects
        print(obj.toString()) # display the final outputs
        total_score += obj.getExamScore() # total score
    avg_score = total_score/len(allExamsList) # average score
    print("Total Score of All Exams: ", total_score)
    print("Average Score of All Exams: ", avg_score)


def main():

    bool_main = True
    bool_obj = True
    bool_obj1 = True
    bool_obj2 = True
    bool_obj3 = True
    more_choice = "Always Running"

    while bool_main:
        # run the loop until condition is met
        if more_choice != 'no':
            print("\nIT Exam Type Menu: \n")
            print("1) Multiple Choice \n")
            print("2) Technical Writing \n")
            print("3) Analytical Programming")
            input_choice = int(input("Enter your choice: "))
            bool_obj = True
            bool_obj1 = True
            bool_obj2 = True
            bool_obj3 = True
            while bool_obj:
                # run the loop to check the input choice and exit if condition not met
                if input_choice == 1:
                    while bool_obj1:
                        # run the loop to check the Exam title and exit if condition not met
                        input_title = input("Enter the Exam Title: ")
                        obj = MultipleChoiceExam() # initiate the object
                        if obj.setExamTitle(input_title): # set the examtitle for this instance
                            fillITExam(obj) # set instance variable to get the final grade
                            bool_obj1 = False
                            more_choice = str(input("More IT Exams (Yes/No)? ")).casefold()
                            bool_obj = False
                        else:
                            print("Sorry! The exam title is not valid. Please enter it again.")

                    
                elif input_choice == 3:
                    # run the loop to check the input choice and exit if condition not met
                    while bool_obj3:
                        # run the loop to check the exam title and exit if condition not met
                        input_title = input("Enter the Exam Title: ")
                        obj = AnalyticalProgrammingExam() # initiate the object
                        if obj.setExamTitle(input_title): # set the examtitle for this instance
                            fillITExam(obj) # set instance variable to get the final grade
                            bool_obj3 = False
                            more_choice = str(input("More IT Exams (Yes/No)? ")).casefold()
                            bool_obj = False
                        else:
                            print("Sorry! The exam title is not valid. Please enter it again.")

                elif input_choice == 2:
                    # run the loop to check the input choice and exit if condition not met
                    while bool_obj2:
                        # run the loop to check the exam title and exit if condition not met
                        input_title = input("Enter the Exam Title: ")
                        obj = TechnicalWritingExam() # initiate the object
                        if obj.setExamTitle(input_title): # set the examtitle for this instance
                            fillITExam(obj) # set instance variable to get the final grade
                            bool_obj2 = False
                            more_choice = str(input("More IT Exams (Yes/No)? ")).casefold()
                            bool_obj = False
                        else:
                            print("Sorry! The exam title is not valid. Please enter it again.")
                else:
                    print("Sorry! No such choice. Please enter it again")
                    print("\nIT Exam Type Menu: \n")
                    print("1) Multiple Choice \n")
                    print("2) Technical Writing \n")
                    print("3) Analytical Programming \n")
                    input_choice = int(input("Enter your choice: "))
        
        else:
            # Exit the main loop
            bool_main = False        

    # call function to display results
    displayResults(obj_list)

        
    

if __name__ == "__main__":
    main()