from notifypy import Notify

# Create a notification object
notification = Notify()

# Set the title and message for the notification
notification.title = "YOU HACKED!"
notification.message = "YOUR HACKED BY :D!"
notification.urgency = "critical"
notification.icon = "skull.jpeg"
notification.timeout = 7000  # 7 seconds


# Display the notification
notification.send()