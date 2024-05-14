#AirBnB clone - The console

# Project description
1. This project aims to build the foundational elements for an AirBnB clone.
2. It focuses on creating a parent class called BaseModel responsible for instance initialization, serialization, and deserialization. 
3. The project will establish a simple flow for data management, moving between instances, dictionaries, JSON strings, and files. 
4. It involves creating various classes essential for AirBnB functionality, such as User, State, City, and Place, all inheriting from BaseModel.
5. Furthermore, a storage engine will be developed to manage data persistence, starting with a File storage implementation.
6. The project will include comprehensive unittests to ensure the correctness of all classes and the storage engine.

# How to Start the Command Interpreter
To start the command interpreter, follow these steps:
1. Clone the project repository to your local machine.
2. Navigate to the project directory.
3. Run the command "./console.py" to start the command interpreter.

# How to Use the Command Interpreter
Once the command interpreter is running, you can enter commands to interact with the AirBnB clone. Here are some example commands:
- 'create User' : Create a new user.
- 'show State' : Show details about a state. 
- 'update Place' : Update information about a place.
- 'destroy City' : Delete a city from the database.
- 'all' : Show all instances of a specific class.
- 'quit' : Exit the command interpreter.

# Examples
To create a new user account, use the create command followed by the entity type and the attributes in key-value format. For example:
1. (hbnb) create User email="example@example.com" password="password123" first-name="Firstname" last-name="Lastname"

