import time
import httpx

from src.schemas import GigaTokenManangerSchema
from src.config import settings
from src.sys import Singleton


class GigaTokenManager(metaclass=Singleton):
    def __init__(
        self,
        auth_key=settings.api_key,
        url=settings.giga_auth_url,
        ruid=settings.giga_ruid,
    ):
        self.auth_key = auth_key
        self.url = url
        self.ruid = ruid

        # if not settings.ssl_verify:
        #     warnings.filterwarnings("ignore", message="Unverified HTTPS request")


        self.http_client = httpx.Client(
            verify=False,
            timeout=httpx.Timeout(30.0, connect=10.0),  # Добавляем таймауты
        )

        self.access_secret = None

    def _will_expire_in(self, seconds: int = 120) -> bool:
        if not self.access_secret:
            return True
        now_ms = int(time.time() * 1000)
        return (self.access_secret.expires_at - now_ms) <= seconds * 1000

    def get_access_token(self):
        if self.access_secret is None or self._will_expire_in():
            resp = self.http_client.post(
                self.url,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "RqUID": f"{self.ruid}",
                    "Authorization": f"Basic {self.auth_key}",
                },
                data={"scope": "GIGACHAT_API_PERS"},
            )

            resp.raise_for_status()
            self.access_secret = GigaTokenManangerSchema(**resp.json())
            return self.access_secret.access_token
        else:
            return self.access_secret.access_token
