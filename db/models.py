from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    """The model for the user table.ArithmeticError
    
    Attributes:
        email: The user's email address. It is the primary key of the table
            and will be used for logging in to the application.ArithmeticError
        first_name: The first name of the user.
        last_name: The last name of the user.
        username: The username the user can use to refer to themself. This can
            also be used for logging in.
        password: The password the user uses to authenticate.
        is_admin: A boolean value that used to identify whether the user is an
            admin within the app.
    
    """
    __tablename__ = 'user'
    
    email = Column(String(255), primary_key = True)
    first_name = Column(String(255) )
    last_name = Column(String(255) )
    username = Column(String(255) )
    password = Column(String(255) )
    is_admin = Column(Integer )
    
    def __init__(self, email: str, first_name: str, last_name: str, 
            username: str , password: str, is_admin: bool = False):
                        
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.is_admin = is_admin
        
        
    def __repr__(self):
        str_format = '<User(email: %s, first_name: %s, last_name: %s)>'
        values = (self.email, self.first_name, self.last_name)
        return str_format % values


class Employee(Base):
    """The model for the employee table.
    
    Attributes:
        email (str): The employee's email. It is used as the primary key for
            the table, and it will be used for adding employees to groups for
            the corresponding apps.
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
    
    """
    __tablename__ = 'employee'
    
    email = Column(String(255), primary_key = True)
    first_name = Column(String(255) )
    last_name = Column(String(255) )
    
    
    def __init__(self, email: str, first_name: str, last_name: str):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        
        
    def __repr__(self):
        str_format = '<Employee(email: %s, first_name: %s, last_name: %s)>' 
        values = (self.email, self.first_name, self.last_name)
        return str_format % values
        

class App(Base):
    """The model for the app table.
    
    Attributes:
        app_id (int): The primary key of the app table.
        name (str): The name of the app. It is used to distinguish which 
            application groups belong to, since group names may be repeated.
    
    """
    __tablename__ = 'app'
    
    app_id = Column(Integer, primary_key = True)
    name = Column(String(255) )
    
    
    def __init__(self, app_id: int, name: str, token: str = ""):
        self.app_id = app_id
        self.name = name
        self.token = token
    
    def __repr__(self):
        str_format = '<App(app_id: %s, name: %s)>'
        values = (self.app_id, self.name)
        return str_format % values
        
        
class Role(Base):
    """The model for the role table.
    
    Attributes:
        role_id (int): The primary key of the role table.
        name (str): The name of the role. Roles must have unique names to
            make them easy to tell them apart.
        description (str): A description of the role.
    
    """
    __tablename__ = 'role'
    
    role_id = Column(Integer, primary_key = True)
    name = Column(String(255), unique = True )
    description = Column(String(1000) )
    
    
    def __init__(self, role_id, name, description):
        self.role_id = role_id
        self.name = name
        self.description = description
        
    
    def __repr__(self):
        str_format = '<Role(role_id: %s, name: %s, description: %s)>'
        values = (self.role_id, self.name, self.description)
        return str_format % values


class Group(Base):
    """The model for the employee table.
    
    Attributes:
        group_id: (int): The primary key of the group table.
        name (str): The name of a group from one of the supported applications.
            Group names may be repeated in different applications.
        app_id (int): The id of the app that this group belongs to.
    
    """
    __tablename__ = 'group'

    group_id = Column(Integer, primary_key = True)
    name = Column(String(255) )
    app_id = Column(Integer)
    
    
    def __init__(self, group_id, name, app_id):
        self.group_id = group_id
        self.name = name
        self.app_id = app_id
    
    
    def __repr___(self):
        str_format = '<Group(group_id: %s, name: %s, app_id: %s)>'
        values = (self.group_id, self.name, self.app_id)
        return str_format % values