from marshmallow import Schema, fields, validate


class PartidaSchema(Schema):
    id_partida = fields.Int(required=True)

    gols_mandante = fields.Int(required=True)
    gols_visitante = fields.Int(required=True)

    ca_mandante = fields.Int(required=True)
    cv_mandante = fields.Int(required=True)

    ca_visitante = fields.Int(required=True)
    cv_visitante = fields.Int(required=True)

    status_partida = fields.Str(
        required=True,
        validate=validate.OneOf([
            "Não iniciado",
            "Em andamento",
            "Finalizado"
        ])
    )