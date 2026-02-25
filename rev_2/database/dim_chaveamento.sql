DROP TABLE IF EXISTS dim_chaveamento;


CREATE TABLE dim_chaveamento (
    id_jogo INTEGER,
    fase TEXT,
    grupo_mandante TEXT,
    posicao_mandante INTEGER,
    grupo_visitante TEXT,
    posicao_visitante INTEGER,
    horario TEXT,
    data_partida TEXT
);

INSERT INTO dim_chaveamento VALUES
(73,'SEGUNDA_FASE','A',1,'B',2,'16:00','2026-06-28'),
(74,'SEGUNDA_FASE','B',1,'A',2,'22:00','2026-06-29'),

(75,'SEGUNDA_FASE','C',1,'D',2,'17:30','2026-06-29'),
(76,'SEGUNDA_FASE','D',1,'C',2,'18:00','2026-06-29'),

(77,'SEGUNDA_FASE','E',1,'F',2,'16:00','2026-06-28'),
(78,'SEGUNDA_FASE','F',1,'E',2,'22:00','2026-06-29'),

(79,'SEGUNDA_FASE','G',1,'H',2,'17:30','2026-06-29'),
(80,'SEGUNDA_FASE','H',1,'G',2,'18:00','2026-06-29'),

(81,'SEGUNDA_FASE','I',1,'J',2,'16:00','2026-06-28'),
(82,'SEGUNDA_FASE','J',1,'I',2,'22:00','2026-06-29'),

(83,'SEGUNDA_FASE','K',1,'L',2,'17:30','2026-06-29'),
(84,'SEGUNDA_FASE','L',1,'K',2,'18:00','2026-06-29'),

(85,'SEGUNDA_FASE','a definir',1,'a definir',2,'16:00','2026-06-28'),
(86,'SEGUNDA_FASE','a definir',1,'a definir',2,'22:00','2026-06-29'),

(87,'SEGUNDA_FASE','a definir',1,'a definir',2,'17:30','2026-06-29'),
(88,'SEGUNDA_FASE','a definir',1,'a definir',2,'18:00','2026-06-29'),






INSERT INTO dim_partidas (id_partida, id_mandante, id_visitante, grupo, rodada, horario, data_partida)
SELECT
    dc.id_jogo,
    mandante.id,
    visitante.id,
    NULL,
    dc.fase,
    dc.horario,
    dc.data_partida
FROM dim_chaveamento dc
JOIN vw_classificacao vc_m
    ON vc_m.grupo = dc.grupo_mandante AND vc_m.posicao = dc.posicao_mandante
JOIN dim_nations mandante
    ON mandante.nome_pais = vc_m.nome_pais
JOIN vw_classificacao vc_v
    ON vc_v.grupo = dc.grupo_visitante AND vc_v.posicao = dc.posicao_visitante
JOIN dim_nations visitante
    ON visitante.nome_pais = vc_v.nome_pais
WHERE dc.fase = 'SEGUNDA_FASE';