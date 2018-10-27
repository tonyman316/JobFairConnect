CMPS 183 Project Proposal
Tung Hoi Man
tuman@ucsc.edu

Project Title: Job-Fair-Connect

Project Abstraction:
A website for college students to make appointments for on-campus job fair interview.

Problems:
Students need to line up at each company's booth to submit their resume and have an interview. Sometimes, some companies may only interview students at specific status (eg. will graduate by the end of this quarter). It’s tiring and time-consuming.

Project Description:
A website to connect companies and students. Companies allocate interview time slot while students sign up for interviews. Interviewers and interviewees can meet up at the event at the appointed time slot.

A company can:
Make a profile
Sign up for an event
Allocate the number of interview slot
Set the time for each slot, accept resume online
Set requirements. (eg. major, year, graduate date)
Offer positions. (summer/quarter internship, full-time, part-time)
Visa sponsorship (H1B, CPT, OPT)

A student can:
Make a profile (Major, year)
Sign up for an event
Pick the available time slot for an interview
Upload resume.
Set availability (eg. graduate date)
Look for positions. (summer/quarter internship, full-time, part-time)

Data stored:
User: email, pw, role, event_id
School accounts:
	School name, location, website, email, phone
Company accounts:
	Name, field, location, interviewers, email, phone, event_id
Student accounts:
	Name, school email, phone, major, resume, link, event_id

Event:
	Date, time, location, capacity, organizer(user_id)

Compbooth:
	Has many user_id, has an event_id,  time_slot, resume

Technologies:
Front-end: Html, CSS, Vue.js
Backend: SQLite
Web framework: web2py
Hosting: Pythonanywhere or Heroku
Version control: Github

Not related to other projects. I’m working on a ruby on rails project in CS115.

Division of work:
Team member:  
Tung Hoi Man: Set up website skeleton and database. Connect view and model to show information on view.

Git URL:
https://github.com/tonyman316/JobFairConnect.git
