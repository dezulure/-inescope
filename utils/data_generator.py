from faker import Faker

fake = Faker("en_US")


class DataGenerator:
    @staticmethod
    def generate_random_password(length: int = 12):
        return fake.password(
            length=length,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )

    @staticmethod
    def generate_random_email():
        return fake.email()

    @staticmethod
    def generate_random_name():
        return fake.first_name()

    @staticmethod
    def generate_random_verified_status():
        return fake.random_element([True,False])

    @staticmethod
    def generate_random_banned_status():
        return fake.random_element([True,False])
