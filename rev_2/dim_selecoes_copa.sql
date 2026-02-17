CREATE TABLE IF NOT EXISTS dim_selecoes_copa (
    id INTEGER PRIMARY KEY,
    nome_pais TEXT NOT NULL,
    grupo TEXT,
    num_jogos INTEGER DEFAULT 0,
    vitorias INTEGER DEFAULT 0,
    empates INTEGER DEFAULT 0,
    derrotas INTEGER DEFAULT 0,
    pontos INTEGER DEFAULT 0,
    gols_marcados INTEGER DEFAULT 0,
    gols_sofridos INTEGER DEFAULT 0,
    saldo_gols INTEGER DEFAULT 0,
    cartao_amarelo INTEGER DEFAULT 0,
    cartao_vermelho INTEGER DEFAULT 0
);


INSERT INTO dim_selecoes_copa (id, nome_pais, grupo) VALUES
-- GRUPO A
((SELECT id FROM dim_nations WHERE nome_pais='México'), 'México', 'A'),
((SELECT id FROM dim_nations WHERE nome_pais='África do Sul'), 'África do Sul', 'A'),
((SELECT id FROM dim_nations WHERE nome_pais='Coreia do Sul'), 'Coreia do Sul', 'A'),

-- GRUPO B
((SELECT id FROM dim_nations WHERE nome_pais='Canadá'), 'Canadá', 'B'),
((SELECT id FROM dim_nations WHERE nome_pais='Catar'), 'Catar', 'B'),
((SELECT id FROM dim_nations WHERE nome_pais='Suíça'), 'Suíça', 'B'),

-- GRUPO C
((SELECT id FROM dim_nations WHERE nome_pais='Brasil'), 'Brasil', 'C'),
((SELECT id FROM dim_nations WHERE nome_pais='Marrocos'), 'Marrocos', 'C'),
((SELECT id FROM dim_nations WHERE nome_pais='Haiti'), 'Haiti', 'C'),
((SELECT id FROM dim_nations WHERE nome_pais='Escócia'), 'Escócia', 'C'),

-- GRUPO D
((SELECT id FROM dim_nations WHERE nome_pais='Estados Unidos'), 'Estados Unidos', 'D'),
((SELECT id FROM dim_nations WHERE nome_pais='Paraguai'), 'Paraguai', 'D'),
((SELECT id FROM dim_nations WHERE nome_pais='Austrália'), 'Austrália', 'D'),

-- GRUPO E
((SELECT id FROM dim_nations WHERE nome_pais='Alemanha'), 'Alemanha', 'E'),
((SELECT id FROM dim_nations WHERE nome_pais='Curaçao'), 'Curaçao', 'E'),
((SELECT id FROM dim_nations WHERE nome_pais='Costa do Marfim'), 'Costa do Marfim', 'E'),
((SELECT id FROM dim_nations WHERE nome_pais='Equador'), 'Equador', 'E'),

-- GRUPO F
((SELECT id FROM dim_nations WHERE nome_pais='Países Baixos'), 'Países Baixos', 'F'),
((SELECT id FROM dim_nations WHERE nome_pais='Japão'), 'Japão', 'F'),
((SELECT id FROM dim_nations WHERE nome_pais='Tunísia'), 'Tunísia', 'F'),

-- GRUPO G
((SELECT id FROM dim_nations WHERE nome_pais='Bélgica'), 'Bélgica', 'G'),
((SELECT id FROM dim_nations WHERE nome_pais='Egito'), 'Egito', 'G'),
((SELECT id FROM dim_nations WHERE nome_pais='Irã'), 'Irã', 'G'),
((SELECT id FROM dim_nations WHERE nome_pais='Nova Zelândia'), 'Nova Zelândia', 'G'),

-- GRUPO H
((SELECT id FROM dim_nations WHERE nome_pais='Espanha'), 'Espanha', 'H'),
((SELECT id FROM dim_nations WHERE nome_pais='Cabo Verde'), 'Cabo Verde', 'H'),
((SELECT id FROM dim_nations WHERE nome_pais='Arábia Saudita'), 'Arábia Saudita', 'H'),
((SELECT id FROM dim_nations WHERE nome_pais='Uruguai'), 'Uruguai', 'H'),

-- GRUPO I
((SELECT id FROM dim_nations WHERE nome_pais='França'), 'França', 'I'),
((SELECT id FROM dim_nations WHERE nome_pais='Senegal'), 'Senegal', 'I'),
((SELECT id FROM dim_nations WHERE nome_pais='Noruega'), 'Noruega', 'I'),

-- GRUPO J
((SELECT id FROM dim_nations WHERE nome_pais='Argentina'), 'Argentina', 'J'),
((SELECT id FROM dim_nations WHERE nome_pais='Argélia'), 'Argélia', 'J'),
((SELECT id FROM dim_nations WHERE nome_pais='Áustria'), 'Áustria', 'J'),
((SELECT id FROM dim_nations WHERE nome_pais='Jordânia'), 'Jordânia', 'J'),

-- GRUPO K
((SELECT id FROM dim_nations WHERE nome_pais='Portugal'), 'Portugal', 'K'),
((SELECT id FROM dim_nations WHERE nome_pais='Uzbequistão'), 'Uzbequistão', 'K'),
((SELECT id FROM dim_nations WHERE nome_pais='Colômbia'), 'Colômbia', 'K'),

-- GRUPO L
((SELECT id FROM dim_nations WHERE nome_pais='Inglaterra'), 'Inglaterra', 'L'),
((SELECT id FROM dim_nations WHERE nome_pais='Croácia'), 'Croácia', 'L'),
((SELECT id FROM dim_nations WHERE nome_pais='Gana'), 'Gana', 'L'),
((SELECT id FROM dim_nations WHERE nome_pais='Panamá'), 'Panamá', 'L');
