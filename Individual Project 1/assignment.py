def main():    
    cont1 = True
    cont2 = True
    cont3 = True
    score_list_student_1 = [] #empty list to store the scores of student 1
    score_list_student_2 = [] #empty list to store the scores of student 2
    score_list_student_3 = [] #empty list to store the scores of student 3
    while cont1:
        #Enter individual score for student 1
        score_student_1 = int(input("Please enter Student 1's score (-1: Exit): "))
        #store them one by one in a list
        if score_student_1 == -1:
            more_student_confirmation = input("Any more student? (Yes or No): ")   

            if more_student_confirmation == "yes":
            #Enter individual score for student 2
                while cont2:
                    score_student_2 = int(input("Please enter Student 2's score (-1: Exit): "))
            #store them one by one in a list
                    if score_student_2 == -1:
                        more_student_confirmation = input("Any more student? (Yes or No): ")

                        if more_student_confirmation == "yes":
                            while cont3:
                                score_student_3 = int(input("Please enter Student 3's score (-1: Exit): "))
            #store them one by one in a list
                                if score_student_3 == -1:
                                    more_student_confirmation = input("Any more student? (Yes or No): ")

                                    if more_student_confirmation == "no":
                                        print(score_list_student_1)
                                        print(score_list_student_2)
                                        print(score_list_student_3)

                                        print("Student 1 has appeared for", len(score_list_student_1), "exams")
                                        cont1 = False
                                        cont2 = False
                                        cont3 = False
                                    
                                else:
                                    score_list_student_3.append(score_student_3)
                    
                #if score_student_2 == -1:
                    else:
                        score_list_student_2.append(score_student_2)
            else:
                cont1 = False
        else:
            score_list_student_1.append(score_student_1)
         

        #if score_student_1 == -1:
       
        

          

        





        
        # cnt1 = cnt1 + 1
        # if (score_student_1 == -1):
        #     confirm_student_entry_1 = (input("Any more student? (Yes or No):") 
        
        # if (confirm_student_entry == "No"):
        #     score_student_2 = int(input("Please enter Student 2's score (-1: Exit):"))
        #     cnt2 = cn2+1
        
        # if (score_student_2 == -1):
        #     confirm_student_entry_2 = (input("Any more student? (Yes or No):")
        
        # # score_student_2 = int(input("Please enter Student 1's score (-1: Exit):"))
        # # cnt2 = cnt2+1
        
        # avg_score_student_1 = 

          
if __name__ == "__main__":
    main()