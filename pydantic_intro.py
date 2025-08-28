## Why do we use Pydantic?


# Pydantic is a data validation and settings management library for Python,
# built on top of type hints. It is used to ensure that the data being processed
# in an application adheres to a specified schema, providing both validation
# and serialization/deserialization capabilities.


def insert_patient_data(name :str,age:int):
    return {"name":name,"age":age}

### this wont genertae any error as it is not validating the data type

def insert_patient_data2(name :str,age:int):
    if type(name)==str and type(age)==int:
        return {"name":name,"age":age}
    else:
        raise TypeError("incorrect data typee")
    
    
    #### This in nottt good practice as it isnt scalable
    ## but this still can take neagtive values for age
    
    
    ### this is where pydantic comes into play
    
    
    
    
    
    
    
    
