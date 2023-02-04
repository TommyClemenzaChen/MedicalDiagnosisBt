symptoms_diagnosis = {
    "fever": ["Influenza", "Typhoid", "Malaria"],
    "headache": ["Migraine", "Tension headache", "Influenza"],
    "body ache": ["Influenza", "Typhoid", "Malaria"],
    "cough": ["Common Cold", "Asthma", "Bronchitis"],
    "sore throat": ["Common Cold", "Strep throat", "Tonsillitis"],
    "runny nose": ["Common Cold", "Allergic rhinitis"],
    "fatigue": ["Anemia", "Depression", "Chronic Fatigue Syndrome"],
}

def suggest_diagnosis(symptoms):
    suggested_diagnosis = {}
    for symptom in symptoms:
        if symptom in symptoms_diagnosis:
            for diag in symptoms_diagnosis[symptom]:
                if diag in suggested_diagnosis:
                    suggested_diagnosis[diag] += 1
                else:
                    suggested_diagnosis[diag] = 1
    if suggested_diagnosis:
        all_frequent = []
        max_frequency = max(suggested_diagnosis.values())
        for diag, frequency in suggested_diagnosis.items():
            if frequency == max_frequency:
                all_frequent.append(diag)

        print(f"Chatbot: Based on your symptoms, the possible diagnoses are {all_frequent}. Please consult a doctor for a proper diagnosis.")
    else:
        print("Chatbot: Sorry, I couldn't suggest a diagnosis based on your symptoms. Please consult a doctor.")
