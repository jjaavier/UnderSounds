from abc import ABC, abstractmethod
from typing import List, Optional

class InterfaceDAOGenero(ABC):

    @abstractmethod
    def get_genre(self):
        pass