input_data = open('input.txt', 'r') 

 
S = input_data.read() 
S= int(S)
out=S*S

output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(str(out))

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()