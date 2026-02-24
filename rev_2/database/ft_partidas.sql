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


INSERT INTO ft_partidas (id_partida, status_partida)
SELECT id_partida, 'Não iniciado'
FROM dim_partidas;




CREATE VIEW vw_classificacao AS WITH
jogos_expandido as (
    -- mandante
    SELECT
        dp.grupo,
        dp.id_mandante AS id_nation,
        fp.gols_mandante AS gols_pro,
        fp.gols_visitante AS gols_contra,
        CASE
            WHEN fp.gols_mandante > fp.gols_visitante THEN 3
            WHEN fp.gols_mandante = fp.gols_visitante THEN 1
            ELSE 0
        END AS pontos
    from ft_partidas fp
    JOIN dim_partidas dp
        ON fp.id_partida = dp.id_partida

    UNION ALL
    -- visitante
    SELECT
        dp.grupo,
        dp.id_visitante AS id_nation,
        fp.gols_visitante AS gols_pro,
        fp.gols_mandante AS gols_contra,
        CASE
            WHEN fp.gols_visitante > fp.gols_mandante THEN 3
            WHEN fp.gols_visitante = fp.gols_mandante THEN 1
            ELSE 0
        END AS pontos
    FROM ft_partidas fp
    JOIN dim_partidas dp
        ON fp.id_partida = dp.id_partida
),
classificacao as (
    SELECT
        grupo,
        id_nation,
        SUM(pontos) AS pontos,
        SUM(gols_pro) AS gols_pro,
        SUM(gols_contra) AS gols_contra,
        SUM(gols_pro) - SUM(gols_contra) AS saldo_gols
    FROM jogos_expandido
    GROUP BY grupo, id_nation
) 
SELECT
    c.grupo,
    dn.nome_pais,
    c.pontos,
    c.gols_pro,
    c.gols_contra,
    c.saldo_gols,
    RANK() OVER (
        PARTITION BY c.grupo
        ORDER BY
            c.pontos DESC,
            c.saldo_gols DESC,
            c.gols_pro DESC
    ) AS posicao
FROM classificacao c
JOIN dim_nations dn
    ON dn.id = c.id_nation;