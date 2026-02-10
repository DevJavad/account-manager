from tortoise.models import Model
from tortoise.fields import IntField, CharField, TextField, BooleanField


class Account(Model):
    id = IntField(pk=True)
    phone = CharField(max_length=20, unique=True, index=True)
    api_id = IntField()
    api_hash = CharField(max_length=100)
    device_model = CharField(max_length=100)
    system_version = CharField(max_length=100)
    session_string = TextField()

    chat_id = IntField(max_length=15)
    is_premium = BooleanField(default=False)
    first_name = TextField()
    last_name = TextField(null=True, default=None)
    full_name = TextField()
    username = CharField(max_length=20, null=True, default=None)
    bio = TextField(null=True, default=None)

    class Meta:
        table = "accounts"

    def __str__(self):
        return f"Account(phone={self.phone})"