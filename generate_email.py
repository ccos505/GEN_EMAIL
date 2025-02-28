import hashlib
import datetime
import base64


class DeterministicCredentialsGenerator:
    def __init__(self, username: str, domain: str = "example.com", password_length: int = 12):
        self.username = username
        self.domain = domain
        self.password_length = password_length

    def _get_current_month_identifier(self) -> str:
        """Generate a unique identifier based on the current year and month."""
        now = datetime.datetime.now()
        return f"{self.username}-{now.year}-{now.month}"

    def _generate_email(self) -> str:
        """Generate a deterministic email that changes every month."""
        unique_string = self._get_current_month_identifier()
        hashed_value = hashlib.sha256(unique_string.encode()).hexdigest()[
            :8]  # First 8 characters of hash
        return f"{self.username}{hashed_value}@{self.domain}"

    def _generate_password(self) -> str:
        """Generate a deterministic password that changes every month."""
        if self.password_length < 8:
            raise ValueError(
                "Password length should be at least 8 characters for security.")

        unique_string = f"{self._get_current_month_identifier()}-password"
        hashed_value = hashlib.sha256(
            unique_string.encode()).digest()  # Get raw bytes of hash
        password = '@' + \
            base64.urlsafe_b64encode(hashed_value).decode()[
                :self.password_length - 1]

        return password

    def _generate_static_dob(self) -> str:
        """Generate a deterministic date of birth that remains constant across months."""
        unique_string = f"{self.username}-dob"
        hashed_value = hashlib.sha256(unique_string.encode()).hexdigest()

        birth_year = datetime.datetime.now().year - \
            (20 + int(hashed_value[:2], 16) % 21)  # Age: 20-40
        birth_month = 1 + int(hashed_value[2:4], 16) % 12  # Month: 1-12
        # Day: 1-28 (safe for all months)
        birth_day = 1 + int(hashed_value[4:6], 16) % 28

        return f"{birth_year:04d}-{birth_month:02d}-{birth_day:02d}"

    def generate_credentials(self) -> dict:
        """Generate email, password (which change monthly), and a static DOB."""
        return {
            "email": self._generate_email(),
            "password": self._generate_password(),
            "date_of_birth": self._generate_static_dob()
        }


generator = DeterministicCredentialsGenerator("john_doe", "gmail.com", 12)
credentials = generator.generate_credentials()

print(f"Email: {credentials['email']}")
print(f"Password: {credentials['password']}")
print(f"Date of Birth: {credentials['date_of_birth']}")
