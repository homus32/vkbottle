from abc import ABC, abstractmethod
import typing


class ABCResponseValidator(ABC):
    """ Abstract Response Validator class
    Documentation: https://github.com/timoniq/vkbottle/tree/v3.0/docs/api/response-validator.md
    """

    @abstractmethod
    async def validate(self, response: dict) -> typing.Union[typing.Any, typing.NoReturn]:
        pass