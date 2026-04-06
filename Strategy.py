from abc import ABC, abstractmethod

# Interfaz
class NotificationPolicy(ABC):
    @abstractmethod
    def should_notify(self, event: str) -> bool:
        pass

# Estrategias
class AlwaysNotify(NotificationPolicy):
    def should_notify(self, event: str) -> bool:
        return event in ["TASK_CREATED", "STATUS_CHANGED", "TASK_DONE"]

class NotifyOnDoneOnly(NotificationPolicy):
    def should_notify(self, event: str) -> bool:
        return event == "TASK_DONE"

# Servicio
class NotificationService:
    def __init__(self, policy: NotificationPolicy):
        self.policy = policy

    def process_event(self, event: str, task: Task):
        if self.policy.should_notify(event):
            print(f"Notificación enviada para la tarea {task.id} por el evento: {event}")