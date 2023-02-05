# map a symptom to possible associated diagnoses
symptoms_diagnosis = {
    "Headache": ["Migraine", "Tension headache", "Influenza", "Typhoid", "Covid"],
    "Fever": ["Influenza", "Typhoid", "Malaria", "Covid"],
    "Body ache": ["Influenza", "Typhoid", "Malaria", "Covid"],
    "Fatigue": ["Influenza", "Typhoid", "Malaria", "Chronic Fatigue Syndrome", "Covid"],
    "Sore throat": ["Influenza", "Strep throat", "Tonsillitis", "Covid"],
    "Cough": ["Common Cold", "Bronchitis", "Asthma", "Covid"],
    "Runny nose": ["Common Cold", "Allergic rhinitis", "Covid"],
    "Shortness of breath": ["Asthma", "Bronchitis", "Covid"],
    "Chest pain": ["Asthma", "Bronchitis"],
    "Loss of appetite": ["Typhoid", "Malaria"],
    "Nausea": ["Typhoid", "Malaria", "Migraine", "Covid"],
    "Diarrhea": ["Typhoid", "Malaria", "Covid"],
    "Depressed mood": ["Depression"],
    "Irritability": ["Depression"],
    "Low energy": ["Depression", "Chronic Fatigue Syndrome"],
    "Difficulty sleeping": ["Depression", "Chronic Fatigue Syndrome"],
    "Loss of interest in activities": ["Depression"],
}

# map a diagnosis to suggested treatments
treatments = {
    "Influenza": ["Rest", "Over-the-counter pain relievers", "Stay hydrated"],
    "Typhoid": ["Antibiotics", "Pain relievers", "Fluids and rest"],
    "Malaria": ["Antimalarial medications", "Pain relievers", "Fluids and rest"],
    "Migraine": ["Pain relievers", "Avoid triggers", "Relaxation techniques"],
    "Tension headache": ["Pain relievers", "Stress management", "Physical therapy"],
    "Common Cold": ["Rest", "Over-the-counter cold and cough medications", "Stay hydrated"],
    "Asthma": ["Inhalers", "Avoid triggers", "Avoid respiratory infections"],
    "Bronchitis": ["Antibiotics", "Avoid irritants", "Fluids and rest"],
    "Strep throat": ["Antibiotics", "Pain relievers", "Gargle salt water"],
    "Tonsillitis": ["Antibiotics", "Pain relievers", "Gargle salt water"],
    "Allergic rhinitis": ["Avoid allergens", "Over-the-counter allergy medications", "Nasal sprays"],
    "Anemia": ["Iron supplements", "Vitamin-rich foods", "Fluids and rest"],
    "Depression": ["Talk therapy", "Antidepressant medication", "Stress management"],
    "Chronic Fatigue Syndrome": ["Stress management", "Physical therapy", "Energy conservation techniques"],
    "Covid": ["Antivirals"], 
}

# print out the suggested treatments for a diagnosis
def suggest_treatments(diagnosis):
    if diagnosis.lower() not in [treatment.lower() for treatment in treatments]:
        print("Chatbot: Sorry, I don't have information on treatments for the given diagnosis.")
    else:
        for treatment in treatments:
            if (treatment.lower() == diagnosis.lower()):
                print(f"Chatbot: Based on this diagnosis, possible treatments include {treatments[treatment]}.")

# find the most likely diagnoses based off symptoms
# symptoms: list of symtpoms
def calculate_diagnosis(symtpoms): 
    diagnoses = {}
    for symptom in symptoms:
        for diagnosis in symptoms_diagnosis[symptom.capitalize()]:
            if diagnosis in diagnoses:
                diagnoses[diagnosis] += 1
            else:
                diagnoses[diagnosis] = 1
    max_frequency = max(diagnoses.values())
    return [diagnosis for diagnosis in diagnoses if diagnoses[diagnosis] == max_frequency]

# symptoms: list of strings
# suggest the highest counted diagnosis or diagnoses based off of symptoms
# provide the user with possible treatments for the diagnosis that they believe may be the most accurate
def suggest_diagnosis_and_treatments(symptoms):
    suggested_diagnosis = calculate_diagnosis(symptoms)

    if not suggested_diagnosis:
        print("Chatbot: Sorry, I couldn't find any diagnosis based on the given symptoms.")
        return

    if len(suggested_diagnosis) == 1:
        print(f"Chatbot: Based on your symptoms, the most likely diagnosis is {suggested_diagnosis[0]}.")
        suggest_treatments(suggested_diagnosis[0])
    else:
        print(f"Chatbot: Based on your symptoms, possible diagnoses include {suggested_diagnosis}.")
        print("Chatbot: Which diagnosis would you like to hear about?")
        user_guess = input("You: ")

        if user_guess.lower() in [diagnosis.lower() for diagnosis in suggested_diagnosis]:
            suggest_treatments(user_guess)
        else:
            print(f"Chatbot: Sorry, {user_guess} is not a possible diagnosis based on your symptoms. Possible diagnoses include {suggested_diagnosis}.")

# return true if all inputs are valid or false otherwise
def validate_input(inputs):
    invalids = []
    for symptom in inputs:
        if symptom.lower() not in [symptoms_diagnosis_lowered.lower() for symptoms_diagnosis_lowered in symptoms_diagnosis]:
            invalids.append(symptom)
    if len(invalids) > 0:
        print(f"Chatbot: I did not recognize these symptoms {invalids}. Please try again using the symptoms list below.")
    return len(invalids) == 0

# prompt the user to list comma separated values consisting of their symptoms
symptoms = []
while True:
    print("Symptoms List: ")
    for symptom in symptoms_diagnosis.keys():
        print(symptom, end = ', ')
    print('\n')
    print("Chatbot: Please enter your symptoms separated by commas: ")
    line = input("You: ").strip().split(", ")
    if not validate_input(line):
        continue
    symptoms += line
    symptoms = [symptom.strip().lower() for symptom in symptoms]
    suggest_diagnosis_and_treatments(symptoms)
    print("Chatbot: Do you have any other symptoms to add? (yes/no)")
    user_response = input("You: ").strip().lower()
    if user_response != "yes":
        print("Goodbye!")
        break

