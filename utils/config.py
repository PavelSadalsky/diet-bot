import os
from dataclasses import dataclass
from typing import ClassVar, Optional


@dataclass
class Config:
    bot_token: str
    _config: ClassVar[Optional["Config"]] = None

    @classmethod
    def load(cls):
        if cls._config:
            return cls._config
        if os.path.exists(".env"):
            from dotenv import load_dotenv

            load_dotenv()
        try:
            cls._config = cls(bot_token=os.environ["BOT_TOKEN"])
        except KeyError:
            raise Exception("Environment variables does not exists.")
        return cls._config
