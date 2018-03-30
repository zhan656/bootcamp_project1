import random
fake_data = {}
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

total_weeks = (52-40)+1+11
dic_index = 0
for i in range(total_weeks):
    if i <= 12:
        for state in states:
            fake_data[dic_index] = {}
            per_week = fake_data[dic_index]
            per_week['year'] = 2017
            per_week['week'] = i + 40
            per_week['state'] = state
            per_week['cases'] = random.randint(200,1000)
            per_week['tweets'] = random.randint(10,200)
            dic_index += 1
    else:
        for state in states:
            fake_data[dic_index] = {}
            per_week = fake_data[dic_index]
            per_week['year'] = 2018
            per_week['week'] = i - 12
            per_week['state'] = state
            per_week['cases'] = random.randint(200,1000)
            per_week['tweets'] = random.randint(10,200)
            dic_index += 1
print(fake_data)