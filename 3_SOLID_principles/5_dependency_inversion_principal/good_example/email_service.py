from notification_channel import NotificationChannel

class EmailService(NotificationChannel):
    def notify(self,msg):
        print(f"Sending Email: {msg}")
