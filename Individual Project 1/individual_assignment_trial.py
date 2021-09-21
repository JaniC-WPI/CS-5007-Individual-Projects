def main():    
    cont = True
    num_list =  []
    while cont:        
        num_ele = int(input("Enter number"))
        
        if  num_ele != -1:
            num_list.append(num_ele)

        else:
            cont = False

    print(num_list)





        
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