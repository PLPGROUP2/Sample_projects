from random import randint
#career options list
career_option_list = ["software engineering",
                      "aeronautical engineeering"]
#career advices list                
career_advices_list = ["advice: collaborate with other software engineers",
                        "advice: be ready to travel the world"]
#questions regarding software
software_questions = ["outline the process of software developments",
             "What is software re-engineering?",
             "What are the characteristics of Software?",
             "What is Cohesion?"]
#this function shuffles the list of answers to make the randomly displayed each time
def list_shuffler():
    shuffle_list_of_answers = []
    while len(shuffle_list_of_answers)<4:
        num = randint(0,3)
        if num in shuffle_list_of_answers:
            continue
        else:
            shuffle_list_of_answers.append(num)
    return shuffle_list_of_answers
#the main function that asks for user inputs and validates them awarding points for correct answers
def user_fun(questions, answers):
    points = 0
    count = 1
    for question in questions:
        shuffled_list = list_shuffler()         #calling the shuffler
        j=0
        i = shuffled_list[j]                    
        print("question ",count,":",question,"\n")
        for answer in answers:
            i = shuffled_list[j]       
            print(answers[i]) 
            j+=1
        bl = True
        while bl:
            try:
                choice=int(input("\nchoose the suitable answer from choices above:\nanswer with the number at the start of the answers: "))
                bl = False
            except ValueError:
                print("\nplease answer with a number between 1 and 4!!")
        if choice == count:
            print("correct")
            points +=1
        else:
            print("wrong")
        count +=1
    return points



             
aeronautical_questions= ["what are the differences btn incompressible and compressible flows?",
             "what are the major sectors involved in aircraft maintainance?",
             "what is the main source of power in an aircraft?",
             "what are the different stress types in aircraft operations?"]

software_answers = ["1.Requirement gathering & analysis,Design,Implementation & coding, Testing, Deployment, Maintenance",
           "2.the process of scanning, modifying, and reconfiguring a system in a new way.",
           "3.Software is developed or engineered; it is not manufactured in the classical sense",
           "4.It indicates the relative functional capacity of the module. "]

aeronautical_answers =["1.incompressible flows are flows that have a constant density, whereas compressible flows are those that consists of variable densities",
           "2.mechanical and avionic",
           "3.hydraulic motor",
           "4.tensile, compressive, shear"]    


software_points = user_fun(software_questions,software_answers)
aero_points = user_fun(aeronautical_questions,aeronautical_answers)
if software_points>aero_points:
    print("you should pursue software engineering\n")
    print(career_advices_list[0])
else:
    print("you should pursue aeronautical engineering\n")
    print(career_advices_list[1])