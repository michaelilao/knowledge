
from abc import ABC, abstractmethod
from typing import List

from User import User


class NotificationChannel(ABC):

    @abstractmethod
    def Notify(self, user: User, message: str):
        pass


class SMSChannel(NotificationChannel):
    def __init__(self):
        pass

    def Notify(self, user: User, message: str):
        print("Sending SMS to " + user.name + " @ " + user.phone)
        print("SMS: " + message)


class EmailChannel(NotificationChannel):
    def __init__(self):
        pass

    def Notify(self, user: User, message: str):
        print("Sending Email to " + user.name + " @ " + user.email)
        print("Email: " + message)


class NotificationService():
    def __init__(self):
        self.channels: List[NotificationChannel] = []

    def AddChannel(self, channel: NotificationChannel):
        self.channels.append(channel)

    def Notify(self, user: User, message: str):
        for channel in self.channels:
            if user is not None:
                channel.Notify(user, message)
