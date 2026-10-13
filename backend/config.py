from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    SQLITE_DB_FILE: str

    SECRET_KEY: str
    ALGORITHM: str
    ADMIN_NAME: str
    ADMIN_SURNAME: str
    ADMIN_PHONENUM: PhoneNumber
    ADMIN_EMAIL: EmailStr
    ADMIN_PASS: str


    @property
    def db_url_sqlite(self):
        return f"sqlite+aiosqlite:///{self.SQLITE_DB_FILE}.db"

    @property
    def secret_key(self):
        return f"{self.SECRET_KEY}"
    
    @property
    def algorithm(self):
        return f"{self.ALGORITHM}"

    @property
    def admin_name(self):
        return f"{self.ADMIN_NAME}"

    @property
    def admin_surname(self):
        return f"{self.ADMIN_SURNAME}"
    @property
    def admin_phonenum(self):
        return f"{self.ADMIN_PHONENUM}"

    @property
    def admin_email(self):
        return f"{self.ADMIN_EMAIL}"

    @property
    def admin_pass(self):
        return f"{self.ADMIN_PASS}"


    model_config = SettingsConfigDict(env_file=".env")
settings = Settings()