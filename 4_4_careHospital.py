"""Problem Statement
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
} 

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.

Note: 

Assume that there is always only one medical speciality which is visited by maximum number of patients.

Perform case sensitive string comparison wherever necessary.

Sample Input                                            Expected Output

[101,P,102,O,302,P,305,P]                               Pediatrics

[101,O,102,O,302,P,305,E,401,O,656,O]                   Orthopedics

[101,O,102,E,302,P,305,P,401,E,656,O,987,E]             ENT

"""

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
   
    result = [0,0,0]
    i = 1 
    while(i< len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[i] == 'P': result[0] = result[0] + 1
        elif patient_medical_speciality_list[i] == 'O' : result[1] = result[1] + 1
        else : result[2] = result[2] + 1
        i = i + 2
    a = max(result)
    a = result.index(a)
    if a == 0: speciality = 'Pediatrics'
    elif a == 1: speciality ='Orthopedics'
    else : speciality = 'ENT'

    return speciality


speciality_list_visited_by_patients=[301,'O',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E' ,306, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(speciality_list_visited_by_patients,medical_speciality)
print("The most visited speciality by patients is :",speciality)

# end