def arithmetic_arranger(problems, show_answers=False):
    dash = ''
    row1=''
    row2=''
    problems_copy = problems[:]
    results = ''
    string=''
    space = ' '*4
    for problem in problems_copy:
        num1, operation, num2 = problem.split(' ')
        if len(num1) > len(num2):
            longer_value = len(num1)
        else:
            longer_value = len(num2)
        try:
            if len(problems) > 5:
                    return 'Error: Too many problems.'
            elif len(num1) > 4 or len(num2) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
            elif not num1.isdigit() or not num2.isdigit():
                    return 'Error: Numbers must only contain digits.'
            
            elif operation == '+':
                max_char = longer_value + 2
                if show_answers:
                    results += ' '*(max_char-longer_value)+str(int(num1) + int(num2)) + space
                row1 += " "*(max_char-len(num1))+str(num1) + space 
                row2 += operation+ ' '*(max_char-len(num2)-1) +str(num2) + space
                dash += '-'*(max_char) + space
                
            
            elif operation == '-':
                max_char = longer_value + 2
                if show_answers:
                    results += ' '*(max_char-longer_value)+str(int(num1) - int(num2)) + space
                row1 += ' '*(max_char-len(num1))+str(num1) + space
                row2 += operation + ' '*(max_char-len(num2)-1) +str(num2) + space
                dash += '-'*(max_char) + space
                
            elif operation == '/' or operation == '*':
                    return "Error: Operator must be '+' or '-'."
            
            
            problems.pop(0)
        
        except Exception as e:
             print(e)
    #string += row1 + row2 + dash
    if show_answers:
        string += row1 + row2 + dash + results
    else:
        string += row1 + row2 + dash
    problems.append(string)
    print(row1 + "\n" + row2 + "\n" + dash + '\n' + results)
    return problems

print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
