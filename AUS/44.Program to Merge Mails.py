# Mail template
template = """\nDear {name},

We are pleased to inform you that your application for the position of {position} has been accepted.

Best regards,
{sender}
"""

# Ask how many recipients
num = int(input("How many recipients do you want to send the mail to? "))

# List to store recipient info
recipients = []

# Get input for each recipient
for i in range(num):
    print(f"\nEnter details for Recipient {i + 1}:")
    name = input("Name: ")
    position = input("Position: ")
    sender = input("Sender: ")
    
    recipients.append({
        "name": name,
        "position": position,
        "sender": sender
    })

# Generate and print personalized mails
print("\n" + "=" * 50)
print("Generated Mails:")
for person in recipients:
    message = template.format(name=person["name"], position=person["position"], sender=person["sender"])
    print("-" * 50)
    print(message)
