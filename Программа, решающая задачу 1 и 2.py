print('\nЗАДАНИЕ 1\n\n')

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(format(i,'07b'))
  return m

variant = int(input('Введите номер варианта по списку: '))

BSN = 2*variant
FSN = 127 - (3*variant)
print(format(FSN,'08b')+' '+format(FSN,'0x')+' '+'FSN='+str(FSN)+' FIB=0')
print(format(BSN,'08b')+' '+format(BSN,'0x')+' '+'BSN='+str(BSN)+' BIB=0')


FIO = input('\nVvedite ASCII soobscheniye translitom: ')
print('\nДлина введенной фразы: ',len(FIO))
FIOR = reversed(FIO)
FIO_array = ''.join(toBinary(FIOR))

next_step = list(FIO_array)

x = len(FIO_array)

n = 8
chunks = [FIO_array[-(i+n):-i] for i in range(0, len(FIO_array), n)]
chunks[0]=FIO_array[-n:]
count=0

for x in chunks:
    p=count
    if count%8==0 and p<len(FIO):
        print(format(int(x,2),'08b') + '        '+ format((int(x,2)),'0x')+'        OF         '+'Char='+FIO[count]+' Char='+FIO[count+1])
        count+=2
    elif count%8!=0 and p<len(FIO):
        print(format(int(x,2),'08b') + '        '+ format((int(x,2)),'0x')+'        OF         '+' Char='+FIO[count])
        count+=1
if len(FIO)%8!=0:
    print(format(int(chunks[-1],2),'08b') + '       '+ format((int(chunks[-1],2)),'0x')+'       OF         '+' Char=')


def convert_to_binary_and_hex(text):
    for char in text:
        char_code = ord(char)
        binary_repr = format(char_code, '016b')
        hex_repr_1 = format(int(binary_repr[:8], 2), 'x')
        hex_repr_2 = format(int(binary_repr[8:], 2), 'x')
        binary_repr_split = f"{binary_repr[:8]}            0{hex_repr_1}\n{binary_repr[8:]}            {hex_repr_2}            Буква= {char}\n"

        print(f"{binary_repr_split}")

phrase = input('Введите фразу на русском языке: ')
print('Длина введенной фразы: ',len(phrase),' символов\n')
print('Число байт, необходимых для передачи указанного сообщения: ',len(phrase)*2,'\n')
convert_to_binary_and_hex(phrase)

print('\n\nЗАДАНИЕ 2\n')

value_b = float(input('Введите значение Рр: '))
value_c = float(input('Введите значение Рз: '))
value_d = float(input('Введите значение Рн/о: '))
value_e = float(input('Введите значение а: '))
value_f = float(input('Введите значение b: '))
value_g = float(input('Введите значение t_раз.: '))

print(f"Значения для варианта {variant}: Pp = {value_b}, Pз = {value_c}, Рн/о = {value_d}, a = {value_e*0.01}, b = {value_f*0.01}, t_ср. = {value_g}\n")

Y_1 = ((((value_b*92+value_c*66+value_d*79)*8)/(64000*3600))*1000000)
print('Рассчитаем нагрузку на звено ОКС от 1 сигнального соединения: \nY1 = ', round(Y_1, 3),' мкЭрл\n')

Np = (0.7*3600)//value_g

print('Учитывая, что нагрузка на один информационный канал равна 0,7 Эрланга,\nнаходим количество разговоров, которые может обслужить один информационный канал: \nNp = ',Np,' разговор(ов)\n')

Np_1ОКС = 0.2/(Y_1*0.000001)

print('рассчитаем, сколько разговоров может обслужить 1 канал ОКС,\nесли нагрузка от одного соединения на этот канал составляет',round(Y_1,3),'мкЭрл: \nNp.окс = ',int(Np_1ОКС))

Vразг = Np_1ОКС//Np

print('Определим число информационных каналов, которые может обслужить 1 канал ОКС, который обслуживает',Np,'разговорных каналов при среднем длительности разговора',value_g,'секунд: \nVразг = ',Vразг)

Y1_1 = ((((value_b*209+value_c*154+value_d*183)*8)/(64000*3600))*1000000)
print('Рассчитаем увеличение сигнальной нагрузки при переадресации: \nY1 = ', round(Y1_1, 3),' мкЭрл\n')

Y_sms_ascii = round((((len(FIO)+95)*8)/(64000*3600))*1000000, 3)
Y_sms_unicod = round((((len(phrase)+95)*8)/(64000*3600))*1000000, 3)

print(f"Y_SMS(ASCII) = ({len(FIO)+95}*8)/(64000*3600) = {Y_sms_ascii}мкЭрл\nY_SMS(Unicod) = ({len(phrase)+99}*8)/(64000*3600) = {Y_sms_unicod}мкЭрл\n")
print('\nПо итогу расчетов получаются следующие нагрузки: ')

Y_1_ascii = 0.2+value_f*Np_1ОКС*(Y1_1-Y_1)*0.000001+value_e*Np_1ОКС*Y_sms_ascii*0.000001
Y_1_unicod = 0.2+value_f*Np_1ОКС*(Y1_1-Y_1)*0.000001+value_e*Np_1ОКС*Y_sms_unicod*0.000001

print(f"Y 1 сигн.(ASCII) = {round(Y_1_ascii,3)} Эрл\nY 1 сигн.(Unicod) = {round(Y_1_unicod,3)} Эрл")
