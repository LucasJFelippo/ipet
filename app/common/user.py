
class User():
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.access_token = None

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def is_active(self) -> bool:
        return True

    @property
    def is_anonymous(self) -> bool:
        if self.id:
            return False
        return True

    def get_id(self) -> str | None:
        if self.is_anonymous:
            return None
        return self.id