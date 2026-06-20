from abc import ABC, abstractmethod
class NotificationChannel(ABC):
    @abstractmethod
    def notify(self,msg):
        pass