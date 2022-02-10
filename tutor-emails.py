import smtplib

def student_email_v1(subject, student, student_grade, tutor_name, time, day, start_date, parent_name, parent_email):
  email_string = f'''Hi {tutor_name},
 
You are scheduled to tutor {student} ({student_grade} grader) in {subject} on {day}s from {time}, beginning {start_date}, and ending the week of January 9. I have emailed {student}'s parent/guardian, and have given them your email address. If this is your first time working with {student} please contact their parent/guardian with a short introduction of yourself, and ask about {student}'s needs. Otherwise, please still reach out to the parent/guardian to notify them of the starting date. I have created a template for an email that you can send to their parent/guardian. Feel free to add any personal touches, or you can create one yourself. If you have worked with {student} previously please still make sure to reach out to their parent/guardian in advance of your first meeting. 
 
Please send the Zoom tutoring links to {parent_name}. The parent's email address is {parent_email}.
 
If {student} does not have any homework please send them material to work on in between your tutoring sessions, so you can go over any issues they had with it during your meeting. Make sure to keep track of your service hours, so I can submit them for our supervising teacher's signature.
 
Your scheduled time is used as a guideline. If you find that another time is more convenient for you and your student's family you are welcome to change to that time by contacting your student's parent/guardian. Please reach out to me ASAP if your scheduled tutoring time changes, so I can adjust your hours on our main schedule. Please contact me at chicagoteenmentors@gmail.com if you have questions or need additional information.
 
Sincerely,
Harbin Li (Chicago Teen Mentors Vice President) &
Sophie Xie (Chicago Teen Mentors Treasurer)
chicagoteenmentors.org
 
Template: 
 
Dear {parent_name},
 
My name is {tutor_name}, and I am a (grade) at (your school). I will be tutoring {student} in {subject} on {day} at {time}, beginning {start_date}. Are there any particular topics that {student} struggles with?
 
Please contact me at (your email) if you have any questions or if you need additional information. I look forward to your reply.
 
Sincerely,
{tutor_name}'''
  return email_string

def student_email_v2(subject, student, student_grade, tutor_name, time, day, start_date, parent_name, parent_email, student_email):
  email_string = f'''Hi {tutor_name},
 
You are scheduled to tutor {student} ({student_grade} grader) in {subject} on {day}s from {time}, beginning {start_date}, and ending the week of January 9. I have emailed {student}'s parent/guardian and {student}, and have given them your email address. If this is your first time working with {student} please contact their parent/guardian with a short introduction of yourself, and ask about {student}'s needs. Otherwise, please still reach out to the parent/guardian to notify them of the starting date. I have created a template for an email that you can send to their parent/guardian. Feel free to add any personal touches, or you can create one yourself. If you have worked with {student} previously please still make sure to reach out to their parent/guardian in advance of your first meeting. 
 
Please send the Zoom tutoring links to {student} and {parent_name}. The student's email address is {student_email}, and their parent/guardian's email address is {parent_email}.
 
If {student} does not have any homework please send them material to work on in between your tutoring sessions, so you can go over any issues they had with it during your meeting. Make sure to keep track of your service hours, so I can submit them for our supervising teacher's signature.
 
Your scheduled time is used as a guideline. If you find that another time is more convenient for you and your student's family you are welcome to change to that time by contacting your student's parent/guardian. Please reach out to me ASAP if your scheduled tutoring time changes, so I can adjust your hours on our main schedule. Please contact me at chicagoteenmentors@gmail.com if you have questions or need additional information.
 
Sincerely,
Harbin Li (Chicago Teen Mentors Vice President) &
Sophie Xie (Chicago Teen Mentors Treasurer)
chicagoteenmentors.org
 
Template: 
 
Dear {parent_name},
 
My name is {tutor_name}, and I am a (grade) at (your school). I will be tutoring {student} in {subject} on {day} at {time}, beginning {start_date}. Are there any particular topics that {student} struggles with?
 
Please contact me at (your email) if you have any questions or if you need additional information. I look forward to your reply.
 
Sincerely,
{tutor_name}'''
  return email_string

def send_emails(emails, subjects, students, student_grades, tutor_names, t, day, start_date, parent_names, parent_emails, send_student, student_emails):
  gmail_user = 'chicagoteenmentors@gmail.com'
  gmail_password = 'fortunatel8Y-'

  sent_from = gmail_user
  for i in range(len(emails)):
    subject = "Tutoring Schedule ({} - {})".format(students[i], subjects[i])
    to = [emails[i]]
    if send_student[i] == "yes":
      body = student_email_v2(subjects[i], students[i], student_grades[i], tutor_names[i], t[i], day[i], start_date[i], parent_names[i], parent_emails[i], student_emails[i])
    else:
      body = student_email_v1(subjects[i], students[i], student_grades[i], tutor_names[i], t[i], day[i], start_date[i], parent_names[i], parent_emails[i])

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
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

file = open('tutor-data.txt', 'r') 
lines = file.readlines() 

emails = []
subjects = []
students = []
student_grades = []
tutor_names = []
t = []
days = []
start_date = []
parent_names = []
parent_emails_lst = []
send_student = []
student_emails = []

num = 1
for line in lines:
  if line[:-1] in ["2", "3", "4", "5", "6", "7", "8", "9", "10","11","12"]:
    num+=1
  elif num == 1:
    emails.append(line[:-1])
  elif num == 2:
    subjects.append(line[:-1])
  elif num == 3:
    students.append(line[:-1])
  elif num == 4:
    student_grades.append(line[:-1])
  elif num == 5:
    tutor_names.append(line[:-1])
  elif num == 6:
    t.append(line[:-1])
  elif num == 7:
    days.append(line[:-1])
  elif num == 8:
    start_date.append(line[:-1])
  elif num == 9:
    parent_names.append(line[:-1])
  elif num == 10:
    parent_emails_lst.append(line[:-1])
  elif num == 11:
    send_student.append(line[:-1])
  elif num == 12:
    student_emails.append(line[:-1])

emails = emails[1:]
parent_emails = {}
for i in range(len(parent_emails_lst)):
  if parent_emails_lst[i] in parent_emails:
    if students[i] in parent_emails[parent_emails_lst[i]]["children"]:
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["subject(s)"].append(subjects[i])
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["tutor_emails"].append(emails[i])
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["tutor_names"].append(tutor_names[i])
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["days"].append(days[i])
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["time"].append(t[i])
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["start_dates"].append(start_date[i])
    else:
      parent_emails[parent_emails_lst[i]]["children"][students[i]] = {}
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["subject(s)"] = [subjects[i]]
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["tutor_emails"] = [emails[i]]
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["tutor_names"]= [tutor_names[i]]
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["days"] = [days[i]]
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["time"] = [t[i]]
      parent_emails[parent_emails_lst[i]]["children"][students[i]]["start_dates"] = [start_date[i]]
  else:
    parent_emails[parent_emails_lst[i]] = {}
    parent_emails[parent_emails_lst[i]]["parent_name"] = parent_names[i]
    parent_emails[parent_emails_lst[i]]["children"] = {}
    parent_emails[parent_emails_lst[i]]["children"][students[i]] = {}
    parent_emails[parent_emails_lst[i]]["children"][students[i]]["subject(s)"] = [subjects[i]]
    parent_emails[parent_emails_lst[i]]["children"][students[i]]["tutor_emails"] = [emails[i]]
    parent_emails[parent_emails_lst[i]]["children"][students[i]]["tutor_names"]= [tutor_names[i]]
    parent_emails[parent_emails_lst[i]]["children"][students[i]]["days"] = [days[i]]
    parent_emails[parent_emails_lst[i]]["children"][students[i]]["time"] = [t[i]]
    parent_emails[parent_emails_lst[i]]["children"][students[i]]["start_dates"] = [start_date[i]]

# -- PARENT EMAILS --
def parent_email_either(student, parent_name, subject, tutor, tutor_email, day, time, start_date):
  email_string = f'''Dear {parent_name},
 
Thank you for signing up for Chicago Teen Mentors' tutoring service! Please see your child's tutoring schedule below.
 
{student} will be working on {subject} with {tutor} ({tutor_email}) on {day}s from {time}. This tutor will contact you via email, prior to their first meeting with {student}. {student}'s first tutoring session will be on {day}, {start_date}. Our fall tutoring session will end the week of January 9. 
 
Please download and make a Zoom account before the first session. Our high school tutors will send you a link 5-10 minutes before your scheduled time. If {student} needs to miss any sessions, please contact your tutor in advance of your meeting to reschedule. We look forward to working with you and your child.
 
If your child does not show up to their first tutoring session, they will be removed from the program and your tutor(s) will be paired with another student. Additionally, if your child misses two meetings in a row with no prior notice, they will be removed from our tutoring program and your tutor(s) will be paired with another student. Meetings will not be recorded, but parent(s)/guardian(s) are welcome to sit in on tutoring sessions.
 
If you have any questions, or you feel that your tutor is not a good match for {student} please reach out to chicagoteenmentors@gmail.com.
 
Sincerely,
Ava Penn (Chicago Teen Mentors President)
chicagoteenmentors.org'''
  return email_string

def parent_email_both(student, parent_name, subjects, tutors, tutor_emails, days, times, start_dates):

  email_string = f'''Dear {parent_name},
 
Thank you for signing up for Chicago Teen Mentors' tutoring service! Please see your child's tutoring schedule below.
 
{student} will be working on {subjects[0]} with {tutors[0]} ({tutor_emails[0]}) on {days[0]}s from {times[0]}. {student} will be working on {subjects[1]} with {tutors[1]} ({tutor_emails[1]}) on {days[1]}s from {times[1]}. These tutors will contact you via email, prior to their first meeting with {student}.
 
{student}'s first tutoring session in {subjects[0]} will be on {days[0]}, {start_dates[0]}. {student}'s first tutoring session in {subjects[1]} will be on {days[1]}, {start_dates[1]}. Our fall session will end the week of January 9. Please download and make a Zoom account before the first session. 
 
Our high school tutors will send you a link 5-10 minutes before your scheduled time. If {student} needs to miss any sessions, please contact your tutor in advance of your meeting to reschedule. We look forward to working with you and your child.
 
If your child does not show up to their first tutoring session, they will be removed from the program and your tutor(s) will be paired with another student. Additionally, if your child misses two meetings in a row with no prior notice, they will be removed from our tutoring program and your tutor(s) will be paired with another student. Meetings will not be recorded, but parent(s)/guardian(s) are welcome to sit in on tutoring sessions.
 
If you have any questions, or you feel that your tutors are not a good match for {student} please reach out to chicagoteenmentors@gmail.com.
 
Sincerely,
Ava Penn 
Chicago Teen Mentors President
chicagoteenmentors.org'''
  return email_string

def parent_send_emails(parents):
  gmail_user = 'chicagoteenmentors@gmail.com'
  gmail_password = 'fortunatel8Y-'
  subject = 'Tutoring Schedule'
  sent_from = gmail_user
  for parent in parents:
    to = [parent]
    parent_name = parents[parent]["parent_name"]
    for children in parents[parent]["children"]:
      student = children
      child = parents[parent]["children"][children]
      if len(child["subject(s)"]) == 2:
        body = parent_email_both(student, parent_name, child["subject(s)"], child["tutor_names"], child["tutor_emails"], child["days"], child["time"], child["start_dates"])
      else:
        body = parent_email_either(student, parent_name, child["subject(s)"][0], child["tutor_names"][0], child["tutor_emails"][0], child["days"][0], child["time"][0], child["start_dates"][0])
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
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

#send_emails(emails, subjects, students, student_grades, tutor_names, t, days, start_date, parent_names, parent_emails_lst, send_student, student_emails)
#parent_send_emails(parent_emails)