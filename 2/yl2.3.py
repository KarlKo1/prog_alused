age = int(input("Sisestage enda vanus: "))
pulse_max_male = 220 - age
pulse_max_female = 206 - (0.88*age)
gender = input("Sisestage enda sugu: ").upper()

if gender == "M":
	gender_max_pulse = pulse_max_male
else:
	gender_max_pulse = pulse_max_female

training_id = int(input("Sisestage treeningu tüüp (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening): "))

if training_id == 1:
	min_pulserate = 0.50
	max_pulserate = 0.70
elif training_id == 2:
	min_pulserate = 0.70
	max_pulserate = 0.80
elif training_id == 3:
	min_pulserate = 0.80
	max_pulserate = 0.87

print("Pulsisagedus peaks olema vahemikus " + str(round((gender_max_pulse * min_pulserate))) + " kuni " + str(round((gender_max_pulse * max_pulserate))) + ".")

