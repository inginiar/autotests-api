from typing import TypedDict
from clients.api_clients import APIClient
from httpx import Response


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на регистрацию нового пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет регистрацию пользователя.

        :param request: Словарь с регистрационными данными пользователями.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

