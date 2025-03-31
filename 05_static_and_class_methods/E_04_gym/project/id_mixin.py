class IDMixin:
    _id: int = 1

    @classmethod
    def get_next_id(cls) -> int:
        return cls._id

    @classmethod
    def increment_id(cls) -> None:
        cls._id += 1
