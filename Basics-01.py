# --------------------------------------------------------------------------------------------
# How to handle exception. Except helps to pass to the next iteration
# --------------------------------------------------------------------------------------------
test = [2,4,5, 'DHK', 6]

for el in test:
    try:
        print(el/2)
    except:
        print(f'Invalid element {el}. It must be a number.')

# --------------------------------------------------------------------------------------------
# How to generate csv using pandas data frame
# --------------------------------------------------------------------------------------------
# import pandas as pd

# states = ['Dhaka', 'Mymensingh', 'Chittagong', 'Rajshahi']
# population = [100000, 20000, 40000, 60000]

# dict_states = {'states': states, 'population': population }

# df_states = pd.DataFrame.from_dict(dict_states)

# df_states.to_csv("states.csv", index=False)

# print(df_states)

# --------------------------------------------------------------------------------------------
# How to write in a file
# --------------------------------------------------------------------------------------------
# with open('test.txt', 'w') as file:
#     file.write('Paper successfully scraped')


