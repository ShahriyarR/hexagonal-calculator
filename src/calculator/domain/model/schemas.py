import datetime

from marshmallow import EXCLUDE, Schema, fields, validate
from ulid import ULID


class OperandsCreateDTO(Schema):
    left = fields.Decimal(required=True)
    right = fields.Decimal(required=True)

    class Meta:
        unknown = EXCLUDE


class CalculationCreateDTO(Schema):
    uuid = fields.String(load_default=lambda: str(ULID()))
    left = fields.Decimal(required=True)
    right = fields.Decimal(required=True)
    action = fields.String(
        validate=validate.OneOf(["add", "divide", "subtract", "multiply"])
    )
    result = fields.Decimal(required=True)
    created_at = fields.DateTime(
        load_default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    updated_at = fields.DateTime(
        load_default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    class Meta:
        unknown = EXCLUDE
