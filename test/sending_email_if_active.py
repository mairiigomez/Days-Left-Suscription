
import csv, smtplib, ssl

def send_email(list_estudents_active):
    from_adress = "gomezpythonista@gmail.com"
    receiver_adress = "mairig25@gmail.com"
    password = input("Enter your password: ")

    for name, end_suscription in list_estudents_active:
        print(name)
        print(end_suscription)

        message = """Subject: Your update

        Hi {name}, thank you for having a suscription with Guajiera here is your weekly quote:
        ' Keep working hard'
        Your suscription ends on {end_suscription}
        """
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(from_adress, password)
            server.sendmail(from_adress, receiver_adress, message.format(name=name,end_suscription=end_suscription))

with open(r'C:\Users\Mayri\Documents\DEVELOPER\codigo_practica\suscription_days_left\students.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    students_active = []
    for row in reader:
        name = row['student_name']
        status = row['status']
        end_suscription = row['day_suscription_ends']

        if status == 'active':
            students_active.append((name, end_suscription))

    send_email(students_active)

