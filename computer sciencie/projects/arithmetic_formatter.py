def arithmetic_arranger(problems, show_answers=True):
    width = 6
    dash = ''
    row1=''
    row2=''
    problems_copy = problems[:]
    
    for problem in problems_copy:
        num1, operation, num2 = problem.split(' ')
        space = 0
        try:
            if len(problems) > 5:
                    return 'Error: Too many problems.'
            elif len(num1) > 4 or len(num2) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
            elif not num1.isdigit() or not num2.isdigit():
                    return 'Error: Numbers must only contain digits.'
            elif operation == '+':
                space = width - len(num1)
                result = int(num1) + int(num2)
                row1 += " "*space+str(num1)+ ' '*width
                space = width - len(num2)
                row2 += operation+ ' '*(space-1) +str(num2)+' '*width
                dash += '-'*width + ' '*width
                problems.append(f"\n     {num1}\n{operation}    {num2}\n{dash}")
                problems.pop(0)
            
            elif operation == '-':
                space = width - len(num1)
                row1 += ' '*space+str(num1) + ' '*width
                space = width - len(num2)
                row2 += operation + ' '*(space-1) +str(num2)+' '*width  
                dash += '-'*width + ' '*width 
                result = int(num1) - int(num2)
                problems.append(f"\n   {num1}\n{operation}     {num2}\n{dash}")
                problems.pop(0)
                
            elif operation == '/' or operation == '*':
                    return "Error: Operator must be '+' or '-'."
            
            
            
        except:
             pass
    print(row1 + "\n" + row2 + "\n" + dash)
    return problems

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
#lista=arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

print('  3801      123\n-    2    +  49\n------    -----')