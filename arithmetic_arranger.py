def arithmetic_arranger(problems):
    #problems = input('Please enter your math problems.')
    
    print(problems)
    #return arranged_problems
blankspaces = ''
probspaces = '    '
toprow = list()
operand = list()
botrow = list()
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
for problem in problems:
    problem = problem.rstrip()
    problem = problem.split()
    toprow.append(problem[0])
    operand.append(problem[1])
    botrow.append(problem[2])

print(toprow)
print(operand)
print(botrow)
print(toprow[0], probspaces, toprow[1], probspaces, toprow[2], probspaces, toprow[3])

if len(toprow[0]) > len(botrow[0]):
    operand[0] = operand[0] + (' ' * len(toprow[0]))
    print(f"  {toprow[0]}\n{operand[0]}{botrow[0]}")
elif len(toprow[0]) < len(botrow[0]):
    operand[0] = operand[0] + ' '
    print(f"   {toprow[0]}\n{operand[0]}{botrow[0]}")
else:
    operand[0] = operand[0] + (' ' * len(toprow[0]))
    print(f"    {toprow[0]}\n{operand[0]}{botrow[0]}")
# ======= toprow space length - algorithm?
# ======= -------- length algorithm
# ======= sum algorithm
# ======= try, except statements