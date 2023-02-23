class User:
    """simple User class"""
    
    def __init__(self, first_name, last_name, *user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile=user_profile
        self.login_attempts=0

    def describe_user(self):
        return f"My name is {self.first_name} {self.last_name}\nOther informations:{[i for i in self.user_profile]} ."
    
    def greet_user(self):
        return f"Hi {self.last_name.upper()}!"

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


