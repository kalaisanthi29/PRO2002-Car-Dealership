from car_dealership_api.data.user_data_access import UserDataAccess

class UserService:
    """"""
    def __init__(self, user_data_access:UserDataAccess ):
        self._user_data_access = user_data_access

    def create_user(self, name:str, mail:str, password_hash:str,role:str) -> int |None:
        """"""
        return self._user_data_access.create_user(
            name = name,
            mail = mail,
            password_hash= password_hash,
            role = role
        )
