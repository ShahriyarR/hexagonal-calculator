from marshmallow import EXCLUDE, Schema, fields


class OperandsCreateDTO(Schema):
    left = fields.Decimal(required=True)
    right = fields.Decimal(required=True)

    class Meta:
        unknown = EXCLUDE
