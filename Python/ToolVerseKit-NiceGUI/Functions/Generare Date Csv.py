import random , csv , os
sezon = ['Primavara', 'Vara', 'Toamna', 'Iarna']
total_csv_files = 10
for file_number in range(1, total_csv_files + 1):
    n = 1
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CSV De Antrenare')
    filename = rf'{folder}\Date_{file_number}.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Sezon', 'Ora', 'Temperatura', 'Umbra' ,'Radiatia Solara', 'Kw']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        while n <= 10000:
            sezon1 = random.choice(sezon)
            ora = random.randint(8, 16)
            radiatiaSolara = random.randint(2,10)
            if sezon1 == 'Primavara':
                temperatura = random.randint(15, 30)
                umbra = random.randint(0, 100)
                if umbra <= 50:
                    kw = random.randint(500, 1000)
                else:
                    kw = random.randint(1000, 2500)
            elif sezon1 == 'Vara':
                temperatura = random.randint(25, 40)
                umbra = random.randint(0, 100)
                if umbra <= 50:
                    kw = random.randint(500, 2500)
                else:
                    kw = random.randint(2500, 5000)
            elif sezon1 == 'Toamna':
                temperatura = random.randint(10, 25)
                umbra = random.randint(0, 100)
                if umbra <= 50:
                    kw = random.randint(100, 500)
                else:
                    kw = random.randint(500, 1000)
            elif sezon1 == 'Iarna':
                temperatura = random.randint(-20, 5)
                umbra = random.randint(0, 100)
                if umbra <= 50:
                    kw = random.randint(5, 250)
                else:
                    kw = random.randint(250, 500)
            writer.writerow({'Sezon': sezon1, 'Ora': ora, 'Temperatura': temperatura, 'Umbra': umbra, 'Radiatia Solara' : radiatiaSolara , 'Kw': kw})
            n += 1
