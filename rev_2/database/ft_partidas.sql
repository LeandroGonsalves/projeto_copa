DROP TABLE IF EXISTS ft_partidas;

CREATE TABLE ft_partidas (
    id_partida INTEGER PRIMARY KEY,

    gols_mandante INTEGER DEFAULT 0,
    gols_visitante INTEGER DEFAULT 0,

    ca_mandante INTEGER DEFAULT 0,
    cv_mandante INTEGER DEFAULT 0,
    ca_visitante INTEGER DEFAULT 0,
    cv_visitante INTEGER DEFAULT 0,

    status_partida TEXT DEFAULT 'Não iniciado',

    FOREIGN KEY (id_partida) REFERENCES dim_partidas(id_partida)
);