def arithmetic_arranger(problems):
    #problems = input('Please enter your math problems.')
    
    print(problems)
    #return arranged_problems
blankspaces = ''
probspaces = '    '
toprow = list()
operator = list()
botrow = list()
probanswers = list()
count = 0
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
#problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
for problem in problems:
    problem = problem.rstrip()
    problem = problem.split()
    toprow.append(problem[0])
    operator.append(problem[1])
    botrow.append(problem[2])
    if len(toprow[count]) < len(botrow[count]):
        operator[count] = operator[count] + ' '
        while len(toprow[count]) < len(botrow[count]) + len(operator[count]):
            toprow[count] = ' ' + toprow[count]
        print(f"{toprow[count]}\n{operator[count]}{botrow[count]}")
    elif len(toprow[count]) > len(botrow[count]):
        operator[count] = operator[count] + (' ' * len(toprow[count]))
        while len(toprow[count]) < len(botrow[count]) + len(operator[count]):
            toprow[count] = ' ' + toprow[count]
        print(f"{toprow[count]}\n{operator[count]}{botrow[count]}")
    elif len(toprow[count]) == len(botrow[count]):
        operator[count] = operator[count] + ' '
        while len(toprow[count]) < len(botrow[count]) + len(operator[count]):
            toprow[count] = ' ' + toprow[count]
        print(f"{toprow[count]}\n{operator[count]}{botrow[count]}")
    count += 1


#print(toprow[0], probspaces, toprow[1], probspaces, toprow[2], probspaces, toprow[3])

# ======= -------- length alg
# ======= sum alg
# ======= try, except statements
print(toprow)





# while len(toprow[0]) < 5:
#     toprow[0] = ' ' + toprow[0]
# print(toprow[0])


# if len(toprow[0]) < len(botrow[0]):
#     operator[0] = operator[0] + ' '
#     while len(toprow[0]) < len(botrow[0]) + len(operator[0]):
#         toprow[0] = ' ' + toprow[0]
#     print(f"{toprow[0]}\n{operator[0]}{botrow[0]}")
# elif len(toprow[0]) > len(botrow[0]):
#     operator[0] = operator[0] + (' ' * len(toprow[0]))
#     while len(toprow[0]) < len(botrow[0]) + len(operator[0]):
#         toprow[0] = ' ' + toprow[0]
#     print(f"{toprow[0]}\n{operator[0]}{botrow[0]}")
# elif len(toprow[0]) == len(botrow[0]):
#     operator[0] = operator[0] + ' '
#     while len(toprow[0]) < len(botrow[0]) + len(operator[0]):
#         toprow[0] = ' ' + toprow[0]
#     print(f"{toprow[0]}\n{operator[0]}{botrow[0]}")