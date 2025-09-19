from datetime import datetime

hora_actual = datetime.now().hour

if hora_actual < 12:
    print("Buenos días, FRAN")
elif hora_actual >= 12 and hora_actual <= 20:
    print("Buenos tardes, FRAN")
elif hora_actual >= 21 and hora_actual <= 23:
    print("Buenos noches, FRAN")
