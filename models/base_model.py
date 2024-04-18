#!/usr/bin/python3
"""
Module for the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """ Initialize a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Update the 'updated_at' timestamp to the current time."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Convert the instance attributes to a dictionary."""
        inst_dict = self.__dict__.copy()
        inst_dict["_class_"] = type(self).__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """Return string representation of BaseModel instance."""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
