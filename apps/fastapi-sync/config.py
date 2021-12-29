from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_USERNAME: Optional[str]
    MONGODB_PASSWORD: Optional[str]
    MONGODB_HOST: str
    MONGODB_PORT: str
    MONGODB_DATABASE: str
    MONGODB_TLS_CA_FILE: Optional[str]

    # Database collection name
    MONGODB_COLLECTION_MESSAGES_NAME: str = 'messages'

    def _get_mongodb_dsn(self) -> str:
        if self.MONGODB_USERNAME is None or self.MONGODB_PASSWORD is None:
            return f'mongodb://{self.MONGODB_HOST}:{self.MONGODB_PORT}/{self.MONGODB_DATABASE}'

        return f'mongodb://{self.MONGODB_USERNAME}:{self.MONGODB_PASSWORD}@{self.MONGODB_HOST}:{self.MONGODB_PORT}/{self.MONGODB_DATABASE}' # noqa

    def _get_tls_config(self) -> dict:
        if not self.MONGODB_TLS_CA_FILE:
            return {}

        return {
            'tls': True,
            'tlsCAFile': self.MONGODB_TLS_CA_FILE
        }

    def get_mongodb_config(self) -> dict:
        dsn_config = {'host': self._get_mongodb_dsn()}
        tls_config = self._get_tls_config()

        return {**dsn_config, **tls_config}


settings = Settings()
