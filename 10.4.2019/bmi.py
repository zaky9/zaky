# BMI calculator

beratBadan= int(input('Masukan berat badan (kg): '))
tinggiBadan= float(input('Masukan tinggi badan (cm): ')) 
x= tinggiBadan * 0.01

bmi = round(beratBadan / (x**2),1)

if bmi >=30:
    print('BMI anda: ', bmi, 'Anda sangat overweight')
elif bmi <=29.9 and bmi >=25:
    print('BMI anda: ', bmi, 'Anda overweight')
elif bmi <=24.9 and bmi >=18.5:
    print('BMI anda: ', bmi, 'Anda normal')
else:
    print('BMI anda: ', bmi, 'Anda underweight')
