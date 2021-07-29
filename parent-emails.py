import smtplib

def parent_email_either(student, last_name, pronoun,subject, tutor, tutor_email, day, time, start_date):
  email_string = f'''Dear {pronoun}{last_name},
 
Thank you for signing up for Chicago Teen Mentors' tutoring service! Please see your child's tutoring schedule below.
 
{student} will be working on {subject} with {tutor} ({tutor_email}) on {day}s from {time}. This tutor will contact you via email, prior to their first meeting with {student}. {student}'s first tutoring session will be on {day}, {start_date}. Our summer tutoring session will end the week of August 22. 
 
Please download and make a Zoom account before the first session. Our high school tutors will send you a link 5-10 minutes before your scheduled time. If {student} needs to miss any sessions, please contact your tutor in advance of your meeting to reschedule. We look forward to working with you and your child.
 
If your child does not show up to their first tutoring session, they will be removed from the program and your tutor(s) will be paired with another student. Additionally, if your child misses two meetings in a row with no prior notice, they will be removed from our tutoring program and your tutor(s) will be paired with another student. Meetings will not be recorded, but parent(s)/guardian(s) are welcome to sit in on tutoring sessions.
 
If you have any questions, or you feel that your tutor is not a good match for {student} please reach out to chicagoteenmentors@gmail.com.
 
Sincerely,
Ava Penn (Chicago Teen Mentors President)
chicagoteenmentors.org'''
  return email_string

def send_parent_emails_either(parents, last_names, pronoun, students, subjects, tutor, tutor_email, day, t, start_time):
  gmail_user = 'chicagoteenmentors@gmail.com'
  gmail_password = 'fortunatel8Y-'

  sent_from = gmail_user
  subject = 'Tutoring Schedule'
  for i in range(len(parents)):
    to = [parents[i]]
    body = parent_email_either(students[i], last_names[i], pronoun[i], subjects[i], tutor[i], tutor_email[i], day[i], t[i], start_time[i])
    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        #print(email_text)
        #server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

file = open('either-data.txt', 'r') 
lines = file.readlines() 

parents = []
last_names = []
pronoun = []
students = []
subjects = []
tutors = []
tutor_emails = []
days = []
t = []
start_time = []

num = 1
for line in lines:
  if line[:-1] in ["2", "3", "4", "5", "6", "7", "8","9","10"]:
    num+=1
  elif num == 1:
    parents.append(line[:-1])
  elif num == 2:
    last_names.append(line[:-1])
  elif num == 3:
    pronoun.append(line[:-1])
  elif num == 4:
    students.append(line[:-1])
  elif num == 5:
    subjects.append(line[:-1])
  elif num == 6:
    tutors.append(line[:-1])
  elif num == 7:
    tutor_emails.append(line[:-1])
  elif num == 8:
    days.append(line[:-1])
  elif num == 9:
    t.append(line[:-1])
  elif num == 10:
    start_time.append(line[:-1])


#send_parent_emails_either(parents[1:], last_names, pronoun, students, subjects, tutors, tutor_emails, days, t, start_time)

def parent_email_both(student, last_name, pronoun, reading_tutor, reading_email, reading_day, reading_time, reading_start, math_tutor, math_email, math_day, math_time, math_start):
  email_string = f'''Dear {pronoun}{last_name},
 
Thank you for signing up for Chicago Teen Mentors' tutoring service! Please see your child's tutoring schedule below.
 
{student} will be working on math with {math_tutor} ({math_email}) on {math_day}s from {math_time}. {student} will be working on reading with {reading_tutor} ({reading_email}) on {reading_day}s from {reading_time}. These tutors will contact you via email, prior to their first meeting with {student}.
 
{student}'s first tutoring session in math will be on {math_day}, {math_start}. {student}'s first tutoring session in reading will be on {reading_day}, {reading_start}. Our summer session will end the week of August 22. Please download and make a Zoom account before the first session. 
 
Our high school tutors will send you a link 5-10 minutes before your scheduled time. If {student} needs to miss any sessions, please contact your tutor in advance of your meeting to reschedule. We look forward to working with you and your child.
 
If your child does not show up to their first tutoring session, they will be removed from the program and your tutor(s) will be paired with another student. Additionally, if your child misses two meetings in a row with no prior notice, they will be removed from our tutoring program and your tutor(s) will be paired with another student. Meetings will not be recorded, but parent(s)/guardian(s) are welcome to sit in on tutoring sessions.
 
If you have any questions, or you feel that your tutors are not a good match for {student} please reach out to chicagoteenmentors@gmail.com.
 
Sincerely,
Ava Penn 
Chicago Teen Mentors President
chicagoteenmentors.org'''
  return email_string

def send_parent_emails_both(parents, students, last_names, pronoun, r_tutor, r_tutor_email, r_day, r_t, r_start_date, m_tutor, m_tutor_email, m_day, m_t, m_start_date):
  gmail_user = 'chicagoteenmentors@gmail.com'
  gmail_password = 'fortunatel8Y-'

  sent_from = gmail_user
  subject = 'Tutoring Schedule'
  for i in range(len(parents)):
    to = [parents[i]]
    body = parent_email_both(students[i], last_names[i], pronoun[i], r_tutor[i], r_tutor_email[i], r_day[i], r_t[i], r_start_date[i], m_tutor[i], m_tutor_email[i], m_day[i], m_t[i], m_start_date[i])
    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        #print(email_text)
        #server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

file = open('both-data.txt', 'r') 
lines = file.readlines() 

parents = []
last_names = []
pronoun = []
students = []
subjects = []
r_tutors = []
r_tutor_emails = []
r_days = []
r_t = []
r_start_date = []
m_tutors = []
m_tutor_emails = []
m_days = []
m_t = []
m_start_date = []

num = 1

for line in lines:
  if line[:-1] in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]:
    num+=1
  elif num == 1:
    parents.append(line[:-1])
  elif num == 2:
    last_names.append(line[:-1])
  elif num == 3:
    pronoun.append(line[:-1])
  elif num == 4:
    students.append(line[:-1])
  elif num == 5:
    r_tutors.append(line[:-1])
  elif num == 6:
    r_tutor_emails.append(line[:-1])
  elif num == 7:
    r_days.append(line[:-1])
  elif num == 8:
    r_t.append(line[:-1])
  elif num == 9:
    r_start_date.append(line[:-1])
  elif num == 10:
    m_tutors.append(line[:-1])
  elif num == 11:
    m_tutor_emails.append(line[:-1])
  elif num == 12:
    m_days.append(line[:-1])
  elif num == 13:
    m_t.append(line[:-1])
  elif num == 14:
    m_start_date.append(line[:-1])

#send_parent_emails_both(parents[1:], students, last_names, pronoun, r_tutors, r_tutor_emails, r_days, r_t, r_start_date, m_tutors, m_tutor_emails, m_days, m_t, m_start_date)
