from tortoise.models import Model
from tortoise.fields import IntField, CharField, TextField


class Account(Model):
    id = IntField(pk=True)
    phone = CharField(max_length=20, unique=True, index=True)
    api_id = IntField()
    api_hash = CharField(max_length=100)
    session_string = TextField()

    class Meta:
        table = "accounts"

    def __str__(self):
        return f"Account(phone={self.phone})"