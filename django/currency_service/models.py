from dataclasses import asdict, dataclass


@dataclass
class BaseModel:

    def as_dict(self):
        return asdict(self)
