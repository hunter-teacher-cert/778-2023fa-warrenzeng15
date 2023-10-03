# additional api.py
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: n/a
# consulted: n/a



import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", app_token='geA6qNwvpHVBEDAVXq33qNDOb')
print("")


#part a

# target_county = input("Please enter a county: ")
# target_county = target_county.upper()

# results = client.get("55zc-sp6m", county_of_indictment = target_county, snapshot_year = '2023', select = 'most_serious_crime, current_age', limit = 50000)

# print(results)



# for inmate in results:
#     print("Most serious crime:", inmate['most_serious_crime'], ".   And their age is: ", inmate['current_age'])

# print(len(results))

# counter = 0
# for inmate in results:
#     counter += 1

# print("There are", counter, "inmates in this county.")  

# print("")




#part b

# max_counter = 0
# med_counter = 0
# min_counter = 0
# total = 0


# target_age = input("Please enter an age: ")

# results = client.get("55zc-sp6m", snapshot_year = '2023', select = 'current_age, facility_security_level', limit = 50000)


# for inmate in results:
#     if inmate['current_age'] >= target_age:
#         if inmate['facility_security_level'] == "MAXIMUM SECURITY":
#             max_counter += 1
#         elif inmate['facility_security_level'] == "MEDIUM SECURITY":
#             med_counter += 1
#         else:
#             min_counter += 1
        
# total = max_counter + med_counter + min_counter

# print("Total number of inmates age", target_age, " or older: ", total)
# print("Number of inmates age", target_age, " or older in maximum security: ", max_counter, "(", round((max_counter/total)*100,2),"%)")
# print("Number of inmates age" , target_age,   "or older in medium security: ", med_counter, "(", round((med_counter/total)*100,2),"%)")
# print("Number of inmates age" , target_age, "or older in minimum security: ", min_counter, "(", round((min_counter/total)*100,2),"%)")

#print("")



#part c

# counter = 0
# not_returned = 0

# target_county = input("Please enter a county: ")
# target_county = target_county.upper()
# results = client.get("y7pw-wrny", county_of_indictment = target_county, select = 'return_status', limit = 50000)

# for inmate in results:
#     if inmate['return_status'] != 'Not Returned':
#         not_returned += 1
#         counter += 1
#     else:
#         counter +=1

# print("There are", counter, "inmates from this county.")
# print("The number that did not return to incarceration are: ", not_returned, "(", round((not_returned/counter)*100,2), ")")

#print("")


#part d


total = 0
new_felony_count = 0
parole_vio_count = 0

target_age = input("Please enter an age: ")

results = client.get("y7pw-wrny", select = 'age_at_release, return_status', limit = 50000)

for parolees in results:
    if parolees['age_at_release'] <= target_age:
        if parolees['return_status'] == 'New Felony Offense':
            total += 1
            new_felony_count += 1
        elif parolees['return_status'] == 'Returned Parole Violation':
            total += 1
            parole_vio_count += 1


print("Number of parolees at or under age", target_age, "that returned to prison: ", total)
print("Number of parolees that came back for a 'New Felony Offense': ", new_felony_count, "(", round((new_felony_count/total)*100,2), ")")
print("Number of parolees that came back for a 'Returned Parole Violation': ", parole_vio_count, "(", round((parole_vio_count/total)*100,2), ")")

print("")