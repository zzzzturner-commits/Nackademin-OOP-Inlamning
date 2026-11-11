from models.preconditions import Preconditions 
from models.test_data import TestData
from models.steps import Steps
from uuid import UUID

class TestCase:
    def __init__(self):
        self.id: UUID
        self.title: str
        self.purpose: str
        self.acceptance_criteria: str
        self.preconditions: list[Preconditions] =[]
        self.test_data: list[TestData] = []
        self.steps: list[Steps] = []
        self.expected_result: str