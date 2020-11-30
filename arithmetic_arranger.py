def arithmetic_arranger(problems):
    #problems = input('Please enter your math problems.')
    
    print(problems)
    #return arranged_problems
blankspaces = ''
probspaces = '    '
toprow = list()
operator = list()
botrow = list()
botrowprint = list()
dashes = list()
problem_answer = list()
#problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
count = 0
for problem in problems:
    problem_answer.append(eval(problem))
    problem_answer[count] = str(problem_answer[count])
    problem = problem.rstrip()
    problem = problem.split()
    toprow.append(problem[0])
    operator.append(problem[1])
    botrow.append(problem[2])
    count += 1

count = 0
for number in toprow:
    operator[count] = operator[count] + ' '
    if len(toprow[count]) < len(botrow[count]) + len(operator[count]) and len(toprow[count]) > len(botrow[count]):
        botrow[count] = ' ' + botrow[count]
        while len(toprow[count]) < len(botrow[count]) + len(operator[count]):
            toprow[count] = ' ' + toprow[count]
    elif len(toprow[count]) <= len(botrow[count]):
        while len(toprow[count]) < len(botrow[count]) + len(operator[count]):
            toprow[count] = ' ' + toprow[count]
    elif len(toprow[count]) > len(botrow[count]) + len(operator[count]):
        toprow[count] = '  ' + toprow[count]
        while len(toprow[count]) > len(botrow[count]) + len(operator[count]):
            operator[count] = operator[count] + ' '
    if len(problem_answer[count]) != len(toprow[count]):
        while len(problem_answer[count]) < len(toprow[count]):
            problem_answer[count] = ' ' + problem_answer[count]
    dashes.append('-' * len(toprow[count]))
    toprow[count] += ' ' * 4
    botrow[count] += ' ' * 4
    dashes[count] += ' ' * 4
    problem_answer[count] += ' ' * 4
    count += 1

count = 0
for number in toprow:
    botrowprint.append(operator[count] + botrow[count])
    count += 1

print(f'{toprow}\n{botrowprint}\n{dashes}\n{problem_answer}')



# TO DO
# print in one line
# ======= try, except statements