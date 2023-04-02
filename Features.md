DATABASE DESIGN

With this schema, employers can create accounts and post job openings, while job seekers can register for accounts, browse job postings, and apply for jobs. The database keeps track of user information, job postings, and job applications, and provides a way for employers and job seekers to interact.

### database schema for a job posting website:

**Table: users**
- *id*: unique identifier for each user
- *username*: the username the person uses to log in
- *password*: the password for the account
- *email*: the email address associated with the account
- *name*: the user's full name
- *address*: the user's address
- *phone_number*: the user's phone number
- *is_employer*: a boolean to indicate whether the user is an employer or not
- *created_at*: the date and time the user account was created
- *updated_at*: the date and time the user account was last updated

**Table: job_postings**
- *id*: unique identifier for each job posting
- *user_id*: the ID of the user who posted the job
- *title*: the job title
- *description*: a description of the job duties and requirements
- *location*: the location of the job
- *salary*: the salary or hourly rate of the job
- *company*: the name of the company offering the job
- *created_at*: the date and time the job posting was created
- *updated_at*: the date and time the job posting was last updated

**Table: job_applications**
- *id*: unique identifier for each job application
- *user_id*: the ID of the user applying for the job
- *job_posting_id*: the ID of the job posting the user is applying for
- *resume*: a link to the user's resume or CV
- *cover_letter*: a cover letter or message from the user to the employer
- *status*: the current status of the application (e.g. "pending", "reviewed", "hired", "rejected")
- *created_at*: the date and time the job application was created
- *updated_at*: the date and time