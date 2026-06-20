from notification_channel import NotificationChannel


class SMSService(NotificationChannel):
    def notify(self, msg):
        print(f"Sending SMS: {msg}")
