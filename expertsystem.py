def ask_question(question : str) -> bool:    #this is function for asking question that returns bool values
    response = input(question + ": ").lower().strip()[0]
    return response == 'y'

def diagnostic_allergies() -> bool :
    return ask_question("Do you have itching or swelling?") or ask_question("Do you have red or watery eyes?")

def diagnostic_fever() -> bool:
    return ask_question("Is your body temperature greater than 37.5 °C?") or ask_question("Do you experience chills?") 

def diagnostic_cold() -> bool:
    return ask_question("Do you have running or stuffy nose?") or ask_question("Are you sneezing frequently?")

def diagnostic_flu() -> bool:
    return(
        ask_question("Do you have body aches?") and 
        ask_question("Do you feel tired?") and
        ask_question("Do you have temperature above 38 °C?")
    )
    
def diagnostic_strep_throat() -> bool:
    return(
        ask_question("Do you have sore throat?") and
        ask_question("Are your tonsils swollen")
    )

def diagnostic_foodPoisoning() -> bool:
    return(
        ask_question("Do you feel nausious?") and
        ask_question("Have you been vomating?") and
        ask_question("Do you have dirrehoea?")
    )

print("\nExpert System for Diagnosis")

if diagnostic_allergies():
    print("You Have Allergy.")
    
if diagnostic_fever():
    print("You Have fever.")
    
if diagnostic_cold():
    print("You Have Cold.")
    
if diagnostic_flu():
    print("You Have Flu.")
    
if diagnostic_foodPoisoning():
    print("You Have Food Poisoning.")
    
if diagnostic_strep_throat():
    print("You Have Strep Throat.")
