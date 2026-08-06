import os

from google import genai
from rich import prompt

emails = [
    {
        "sender": "alex.smith@example.com",
        "subject": "Project Status Update",
        "timestamp": "2026-08-01 09:15:00",
        "body": "Hi team, just wanted to let you know that phase one is complete ahead of schedule."
    },
    {
        "sender": "alex.smith@example.com",
        "subject": "Quick question regarding tomorrow's meeting",
        "timestamp": "2026-08-02 14:30:00",
        "body": "Hey, do we have a set agenda for tomorrow morning, or should I bring my draft slides?"
    },
    {
        "sender": "alex.smith@example.com",
        "subject": "Revised Q3 Budget Spreadsheet",
        "timestamp": "2026-08-03 11:05:00",
        "body": "Please find attached the updated numbers for Q3 based on yesterday's discussion."
    },
    {
        "sender": "alex.smith@example.com",
        "subject": "Out of office next Monday",
        "timestamp": "2026-08-04 16:45:00",
        "body": "Hi everyone, I will be out of the office on Monday. Please reach out to Sarah for urgent matters."
    },
    {
        "sender": "alex.smith@example.com",
        "subject": "Follow-up on design reviews",
        "timestamp": "2026-08-05 10:00:00",
        "body": "Thanks for the feedback yesterday! I have updated the mockups and they are ready for final sign-off."
    }
]

def summarize_emails(list_of_emails):
    # mails = []
    os.environ["GEMINI_API_KEY"] = str(os.getenv("GEMINI_API_KEY"))
    client = genai.Client()

    summary_list = []
    for i, message in enumerate(list_of_emails):
        body = message["body"]
        sender = message["sender"]

        email = f"Sender: {sender} \nMessage: {body}\n"
        prompt = "I want you to summarize in a few words what the following e-mail want to say: \n " + email
        response = client.models.generate_content(model="gemini-3.5-flash", contents= prompt)

        print(f"{i + 1}º Email: {response.text}")
        summary_list.append(f"{i + 1}º Email: {response.text}")
        print("-" * 50)

        return summary_list

    # mails.append(f"Sender: {sender} \nMessage: {body}\n")
    # prompt = "I want you to summarize in a few words what the following e-mails want to say: \n ".join(mails)



summarize_emails(emails)

