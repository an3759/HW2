from dataclasses import dataclass

@dataclass
class Greeting:
    """純粹的資料儲存類別"""
    message: str
    generatedAt: str