input_number = [int(input('number1: ')), 
                int(input('number2: ')), 
                int(input('number3: '))]
solved = []

for i in range(0, len(input_number)-1):
    if input_number[i] > input_number[i+1]:
        solved.append(input_number[i])
    elif input_number[i] < input_number[i+1]:
        solved.append(input_number[i+1])
        
for ii in range(0, len(solved)-1):
    if solved[ii] > solved[ii+1]:
        solved.pop(i+1)
    elif solved[ii] < solved[ii+1]:
        solved.pop(ii)

print(solved)

