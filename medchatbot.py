symptoms_diagnosis = {
    "Headache": ["Migraine", "Tension headache", "Influenza", "Typhoid"],
    "Fever": ["Influenza", "Typhoid", "Malaria"],
    "Body ache": ["Influenza", "Typhoid", "Malaria"],
    "Fatigue": ["Influenza", "Typhoid", "Malaria", "Chronic Fatigue Syndrome"],
    "Sore throat": ["Influenza", "Strep throat", "Tonsillitis"],
    "Cough": ["Common Cold", "Bronchitis", "Asthma"],
    "Runny nose": ["Common Cold", "Allergic rhinitis"],
    "Shortness of breath": ["Asthma", "Bronchitis"],
    "Chest pain": ["Asthma", "Bronchitis"],
    "Loss of appetite": ["Typhoid", "Malaria"],
    "Nausea": ["Typhoid", "Malaria", "Migraine"],
    "Diarrhea": ["Typhoid", "Malaria"],
    "Depressed mood": ["Depression"],
    "Irritability": ["Depression"],
    "Low energy": ["Depression", "Chronic Fatigue Syndrome"],
    "Difficulty sleeping": ["Depression", "Chronic Fatigue Syndrome"],
    "Loss of interest in activities": ["Depression"],
}

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
}

def suggest_treatments(diagnosis):
    if diagnosis in treatments:
        print(f"Chatbot: Based on your diagnosis, possible treatments include {treatments[diagnosis]}.")
    else:
        print("Chatbot: Sorry, I don't have information on treatments for the given diagnosis.")

def suggest_diagnosis_and_treatments(symptoms):
    suggested_diagnosis = []
    for symptom in symptoms:
        if symptom in symptoms_diagnosis:
            suggested_diagnosis += symptoms_diagnosis[symptom]

    suggested_diagnosis = list(set(suggested_diagnosis))

    if not suggested_diagnosis:
        print("Chatbot: Sorry, I couldn't find any diagnosis based on the given symptoms.")
        return

    if len(suggested_diagnosis) == 1:
        print(f"Chatbot: Based on your symptoms, the most likely diagnosis is {suggested_diagnosis[0]}.")
        suggest_treatments(suggested_diagnosis[0])
    else:
        print(f"Chatbot: Based on your symptoms, possible diagnoses include {suggested_diagnosis}.")
        print("Chatbot: Can you guess which diagnosis may be correct?")
        user_guess = input("You: ")

        if user_guess in suggested_diagnosis:
            print(f"Chatbot: Great! You guessed correctly. The suggested diagnosis is {user_guess}.")
            suggest_treatments(user_guess)
        else:
            print(f"Chatbot: Sorry, {user_guess} is not a possible diagnosis based on your symptoms. Possible diagnoses include {suggested_diagnosis}.")

while True:
    print("Chatbot: Please enter your symptoms separated by commas: ")
    symptoms = input("You: ").strip().split(",")
    symptoms = [symptom.strip() for symptom in symptoms]
    suggest_diagnosis_and_treatments(symptoms)
    print("Chatbot: Do you have any other symptoms to add? (yes/no)")
    user_response = input("You: ").strip().lower()
    if user_response != "yes":
        break

