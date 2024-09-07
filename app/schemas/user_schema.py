from marshmallow import Schema, fields, validate, ValidationError

# Definimos el esquema para validar los datos del usuario
class UserSchema(Schema):
    username = fields.String(required=True, validate=[
        validate.Length(min=4, max=80, error="Username must be between 4 and 80 characters."),
        validate.Regexp(r"^\w+$", error="Username must contain only letters, numbers, or underscores.")
    ])
    password = fields.String(required=True, validate=[
        validate.Length(min=6, error="Password must be at least 6 characters long.")
    ])
