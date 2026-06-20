from email_service import EmailService
from sms_service import SMSService
from notification_service import NotificationService

smsService = SMSService()
service = NotificationService(smsService)
service.notify("Your order has been placed")
