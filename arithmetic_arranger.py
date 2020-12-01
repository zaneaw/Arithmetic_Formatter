def arithmetic_arranger(problems, *secondarg):
    # Variables
    toprow = list()
    operator = list()
    botrow = list()
    botrowprint = list()
    dashes = list()
    problem_answer = list()
    arranged_probs = ""
    count = 0
    # Exit if too many arguments given.
    if len(problems) > 5:
        arranged_probs = "Error: Too many problems."
        return arranged_probs
    # Iterate through each problem
    for problem in problems:
        # Break Problem into seperate components
        problem = problem.rstrip()
        problem = problem.split()
        # Display error if problems are not numbers
        if not problem[0].isdigit() or not problem[2].isdigit():
            arranged_probs = "Error: Numbers must only contain digits."
            return arranged_probs
        # Display error if problems are too long
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            arranged_probs = "Error: Numbers cannot be more than four digits."
            return arranged_probs
        # Math for the sums (optionally displayed)
        if problem[1] == "+":
            problem_answer.append(int(problem[0]) + int(problem[2]))
        elif problem[1] == "-":
            problem_answer.append(int(problem[0]) - int(problem[2]))
        else:  # Display error if operators are not a '+' or a '-'
            arranged_probs = "Error: Operator must be '+' or '-'."
            return arranged_probs
        # Turn the integer from above math into a string
        problem_answer[count] = str(problem_answer[count])
        # Add the items to individual lists
        toprow.append(problem[0])
        operator.append(problem[1])
        botrow.append(problem[2])
        # Add space behind operator (No matter what, there will always be a space)
        operator[count] = operator[count] + " "
        # LOGIC for spacing (formatted for 79 character length)
        if len(toprow[count]) < len(botrow[count]) + len(
            operator[count]
        ) and len(toprow[count]) > len(botrow[count]):
            botrow[count] = " " + botrow[count]
            while len(toprow[count]) < len(botrow[count]) + len(
                operator[count]
            ):
                toprow[count] = " " + toprow[count]
        elif len(toprow[count]) <= len(botrow[count]):
            while len(toprow[count]) < len(botrow[count]) + len(
                operator[count]
            ):
                toprow[count] = " " + toprow[count]
        elif len(toprow[count]) > len(botrow[count]) + len(operator[count]):
            toprow[count] = "  " + toprow[count]
            while len(toprow[count]) > len(botrow[count]) + len(
                operator[count]
            ):
                operator[count] = operator[count] + " "
        if len(problem_answer[count]) != len(toprow[count]):
            while len(problem_answer[count]) < len(toprow[count]):
                problem_answer[count] = " " + problem_answer[count]
        # Create dashes for the 3rd row
        dashes.append("-" * len(toprow[count]))
        # Add the 4 spaces between all problems on each row
        toprow[count] += " " * 4
        botrow[count] += " " * 4
        dashes[count] += " " * 4
        problem_answer[count] += " " * 4
        # Attach the operator to the botrow numbers
        botrowprint.append(operator[count] + botrow[count])
        count += 1
        # Variable for next line
        sep = "\n"
        # .join() method to join the lists to single individual strings
        # .rstrip() method to strip the whitespace on the right
        trp = "".join(toprow)
        trp = trp.rstrip()
        brp = "".join(botrowprint)
        brp = brp.rstrip()
        drp = "".join(dashes)
        drp = drp.rstrip()
        # Combine the strings
        arranged_probs = trp + sep + brp + sep + drp
    # Return the totals of the problems IF there is a second argument
    if secondarg:
        parp = "".join(problem_answer)
        parp = parp.rstrip()
        arranged_probs += sep + parp
    return arranged_probs