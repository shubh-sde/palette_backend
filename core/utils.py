from enum import Enum

class AdminType(Enum):
  CLIENT = 'client'
  PROGRAM = 'program'
  SUPER = 'super'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]