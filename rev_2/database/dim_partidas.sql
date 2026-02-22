drop table if exists dim_partidas;

CREATE TABLE IF NOT EXISTS dim_partidas (
    id_partida INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mandante INTEGER NOT NULL,
    id_visitante INTEGER NOT NULL,

    grupo TEXT NOT NULL,
    rodada INTEGER NOT NULL,
    horario TEXT NOT NULL,
    data_partida TEXT NOT NULL,
    FOREIGN KEY (id_mandante) REFERENCES dim_nations(id),
    FOREIGN KEY (id_visitante) REFERENCES dim_nations(id)
);

INSERT INTO dim_partidas (id_mandante, id_visitante, grupo, rodada, horario, data_partida) VALUES
-----------
--RODADA 1
-----------
--GRUPO A
(
    (SELECT id FROM dim_nations WHERE nome_pais='Mexico'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Africa do Sul'), 
    'A', 1, '16:00', '2026-06-11'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Coreia do Sul'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 1'),                                                        
    'A', 1, '23:00', '2026-06-11'
),
-- GRUPO B
(
    (SELECT id FROM dim_nations WHERE nome_pais='Canada'),         
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 2'),                                                       
    'B', 1, '16:00', '2026-06-12'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Catar'),             
    (SELECT id FROM dim_nations WHERE nome_pais='Suica'),               
    'B', 1, '16:00', '2026-06-13'
),
-- GRUPO C
(
    (SELECT id FROM dim_nations WHERE nome_pais='Brasil'),               
    (SELECT id FROM dim_nations WHERE nome_pais='Marrocos'),               
    'C', 1, '19:00', '2026-06-13'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Haiti'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Escocia'), 
    'C', 1, '22:00', '2026-06-13'
),
-- GRUPO D
(
    (SELECT id FROM dim_nations WHERE nome_pais='Estados Unidos'),              
    (SELECT id FROM dim_nations WHERE nome_pais='Paraguai'),      
    'D', 1, '22:00', '2026-06-12'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Australia'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 3'), 
    'D', 1, '01:00', '2026-06-20'
),
-- GRUPO E
(
    (SELECT id FROM dim_nations WHERE nome_pais='Alemanha'),             
    (SELECT id FROM dim_nations WHERE nome_pais='Curacao'),               
    'E', 1, '14:00', '2026-06-14'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Costa do Marfim'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Equador'), 
    'E', 1, '20:00', '2026-06-14'
),
-- GRUPO F
(
    (SELECT id FROM dim_nations WHERE nome_pais='Holanda'),              
    (SELECT id FROM dim_nations WHERE nome_pais='Japao'),              
    'F', 1, '17:00', '2026-06-14'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 4'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Tunisia'), 
    'F', 1, '23:00', '2026-06-14'
),
-- GRUPO G
(
    (SELECT id FROM dim_nations WHERE nome_pais='Belgica'),                
    (SELECT id FROM dim_nations WHERE nome_pais='Egito'),            
    'G', 1, '16:00', '2026-06-15'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Ira'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Nova Zelandia'), 
    'G', 1, '22:00', '2026-06-15'
),
-- GRUPO H
(
    (SELECT id FROM dim_nations WHERE nome_pais='Espanha'),                  
    (SELECT id FROM dim_nations WHERE nome_pais='Cabo Verde'),          
    'H', 1, '13:00', '2026-06-15'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Arabia Saudita'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Uruguai'),
    'H', 1, '19:00', '2026-06-15'
),
-- GRUPO I
(
    (SELECT id FROM dim_nations WHERE nome_pais='Franca'),                
    (SELECT id FROM dim_nations WHERE nome_pais='Senegal'),       
    'I', 1, '16:00', '2026-06-16'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 5'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Noruega'),
    'I', 1, '19:00', '2026-06-16'
),
-- GRUPO J
(
    (SELECT id FROM dim_nations WHERE nome_pais='Argentina'),                 
    (SELECT id FROM dim_nations WHERE nome_pais='Argelia'),    
    'J', 1, '22:00', '2026-06-16'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Austria'),
    (SELECT id FROM dim_nations WHERE nome_pais='Jordania'),
    'J', 1, '01:00', '2026-06-17'
),
-- GRUPO K
(
    (SELECT id FROM dim_nations WHERE nome_pais='Portugal'),               
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 6'),    
    'K', 1, '14:00', '2026-06-17'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Uzbequistao'),
    (SELECT id FROM dim_nations WHERE nome_pais='Colombia'),
    'K', 1, '17:00', '2026-06-17'
),
-- GRUPO L
(
    (SELECT id FROM dim_nations WHERE nome_pais='Inglaterra'),                
    (SELECT id FROM dim_nations WHERE nome_pais='Croacia'),    
    'L', 1, '17:00', '2026-06-17'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Gana'),
    (SELECT id FROM dim_nations WHERE nome_pais='Panama'),
    'L', 1, '20:00', '2026-06-17'
),
------------
--RODADA 2
-----------
--GRUPO A
(
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 1'),
    (SELECT id FROM dim_nations WHERE nome_pais='Africa do Sul'),
    'A', 2, '13:00', '2026-06-18'
),
(    
	(SELECT id FROM dim_nations WHERE nome_pais='Mexico'),
    (SELECT id FROM dim_nations WHERE nome_pais='Coreia do Sul'),
    'A', 2, '22:00', '2026-06-18'
),
-- GRUPO B
(              
    (SELECT id FROM dim_nations WHERE nome_pais='Suica'),
	(SELECT id FROM dim_nations WHERE nome_pais='Generico 2'),
    'B', 2, '16:00', '2026-06-18'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Canada'),
    (SELECT id FROM dim_nations WHERE nome_pais='Catar'),
    'B', 2, '19:00', '2026-06-18'
),
-- GRUPO C
(
    (SELECT id FROM dim_nations WHERE nome_pais='Escocia'),	
    (SELECT id FROM dim_nations WHERE nome_pais='Marrocos'),        
    'C', 2, '19:00', '2026-06-19'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Brasil'),
    (SELECT id FROM dim_nations WHERE nome_pais='Haiti'),
    'C', 2, '22:00', '2026-06-19'
),
-- GRUPO D
(
    (SELECT id FROM dim_nations WHERE nome_pais='Estados Unidos'),
    (SELECT id FROM dim_nations WHERE nome_pais='Australia'),	       
    'D', 2, '16:00', '2026-06-19'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 3'),
	(SELECT id FROM dim_nations WHERE nome_pais='Paraguai'),
	'D', 2, '01:00', '2026-06-20'
),
-- GRUPO E
(
    (SELECT id FROM dim_nations WHERE nome_pais='Alemanha'), 
    (SELECT id FROM dim_nations WHERE nome_pais='Costa do Marfim'),      
    'E', 2, '17:00', '2026-06-20'
),
(

    (SELECT id FROM dim_nations WHERE nome_pais='Equador'),
	(SELECT id FROM dim_nations WHERE nome_pais='Curacao'),
    'E', 2, '21:00', '2026-06-20'
),
-- GRUPO F
(
    (SELECT id FROM dim_nations WHERE nome_pais='Holanda'),
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 4'),
    'F', 2, '14:00', '2026-06-20'
),
(

    (SELECT id FROM dim_nations WHERE nome_pais='Tunisia'),
	(SELECT id FROM dim_nations WHERE nome_pais='Japao'),
    'F', 2, '01:00', '2026-06-21'
),
-- GRUPO G
(
    (SELECT id FROM dim_nations WHERE nome_pais='Belgica'),
    (SELECT id FROM dim_nations WHERE nome_pais='Ira'),    
    'G', 2, '16:00', '2026-06-21'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Nova Zelandia'),
    (SELECT id FROM dim_nations WHERE nome_pais='Egito'),
    'G', 2, '22:00', '2026-06-21'
),
-- GRUPO H
(
    (SELECT id FROM dim_nations WHERE nome_pais='Espanha'),
    (SELECT id FROM dim_nations WHERE nome_pais='Arabia Saudita'),	     
    'H', 2, '13:00', '2026-06-21'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Uruguai'),  
	(SELECT id FROM dim_nations WHERE nome_pais='Cabo Verde'),  	
    'H', 2, '19:00', '2026-06-21'
),
-- GRUPO I
(
    (SELECT id FROM dim_nations WHERE nome_pais='Franca'),   
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 5'),
    'I', 2, '18:00', '2026-06-22'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Noruega'),
	(SELECT id FROM dim_nations WHERE nome_pais='Senegal'), 
    'I', 2, '21:00', '2026-06-22'
),
-- GRUPO J
(
    (SELECT id FROM dim_nations WHERE nome_pais='Argentina'),
    (SELECT id FROM dim_nations WHERE nome_pais='Austria'),     
    'J', 2, '14:00', '2026-06-22'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Jordania'),
    (SELECT id FROM dim_nations WHERE nome_pais='Argelia'),
    'J', 2, '00:00', '2026-06-23'
),
-- GRUPO K
(
    (SELECT id FROM dim_nations WHERE nome_pais='Portugal'),    
    (SELECT id FROM dim_nations WHERE nome_pais='Uzbequistao'),      
    'K', 2, '14:00', '2026-06-23'
),
(

    (SELECT id FROM dim_nations WHERE nome_pais='Colombia'),
	(SELECT id FROM dim_nations WHERE nome_pais='Generico 6'),
    'K', 2, '23:00', '2026-06-23'
),
-- GRUPO L
(
    (SELECT id FROM dim_nations WHERE nome_pais='Inglaterra'),
    (SELECT id FROM dim_nations WHERE nome_pais='Gana'),     
    'L', 2, '17:00', '2026-06-23'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Panama'),
	(SELECT id FROM dim_nations WHERE nome_pais='Croacia'),
    'L', 2, '20:00', '2026-06-23'
),
------------
--RODADA 3
-----------
--GRUPO A
(
    (SELECT id FROM dim_nations WHERE nome_pais='Africa do Sul'),
	(SELECT id FROM dim_nations WHERE nome_pais='Coreia do Sul'),
    'A', 3, '22:00', '2026-06-24'
),
(        
	(SELECT id FROM dim_nations WHERE nome_pais='Generico 1'),
	(SELECT id FROM dim_nations WHERE nome_pais='Mexico'),
    'A', 3, '22:00', '2026-06-24'
),
-- GRUPO B
(              
    (SELECT id FROM dim_nations WHERE nome_pais='Suica'),
	(SELECT id FROM dim_nations WHERE nome_pais='Canada'),
    'B', 3, '16:00', '2026-06-24'
),
(
	(SELECT id FROM dim_nations WHERE nome_pais='Generico 2'),
    (SELECT id FROM dim_nations WHERE nome_pais='Catar'),
    'B', 3, '16:00', '2026-06-24'
),
-- GRUPO C
(
    (SELECT id FROM dim_nations WHERE nome_pais='Marrocos'),
    (SELECT id FROM dim_nations WHERE nome_pais='Haiti'),
    'C', 3, '19:00', '2026-06-24'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Escocia'),
    (SELECT id FROM dim_nations WHERE nome_pais='Brasil'),
    'C', 3, '22:00', '2026-06-24'
),
-- GRUPO D
(
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 3'),
    (SELECT id FROM dim_nations WHERE nome_pais='Estados Unidos'),       
    'D', 3, '23:00', '2026-06-25'
),
(
	(SELECT id FROM dim_nations WHERE nome_pais='Paraguai'),         
	(SELECT id FROM dim_nations WHERE nome_pais='Australia'),	
	'D', 3, '23:00', '2026-06-25'
),
-- GRUPO E
(
	(SELECT id FROM dim_nations WHERE nome_pais='Curacao'),
    (SELECT id FROM dim_nations WHERE nome_pais='Costa do Marfim'), 	       
    'E', 3, '17:00', '2026-06-25'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Equador'),
    (SELECT id FROM dim_nations WHERE nome_pais='Alemanha'),
    'E', 3, '17:00', '2026-06-25'
),
-- GRUPO F
(
    (SELECT id FROM dim_nations WHERE nome_pais='Tunisia'),
    (SELECT id FROM dim_nations WHERE nome_pais='Holanda'),  
    'F', 3, '20:00', '2026-06-25'
),
(
	(SELECT id FROM dim_nations WHERE nome_pais='Japao'),
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 4'),
    'F', 3, '20:00', '2026-06-25'
),
-- GRUPO G
(
    (SELECT id FROM dim_nations WHERE nome_pais='Nova Zelandia'),
    (SELECT id FROM dim_nations WHERE nome_pais='Belgica'),   
    'G', 3, '00:00', '2026-06-27'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Egito'),
    (SELECT id FROM dim_nations WHERE nome_pais='Ira'),
    'G', 3, '00:00', '2026-06-27'
),
-- GRUPO H
(
	(SELECT id FROM dim_nations WHERE nome_pais='Cabo Verde'),
    (SELECT id FROM dim_nations WHERE nome_pais='Arabia Saudita'),     
    'H', 3, '21:00', '2026-06-26'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Uruguai'),
    (SELECT id FROM dim_nations WHERE nome_pais='Espanha'), 	
    'H', 3, '21:00', '2026-06-26'
),
-- GRUPO I
(
    (SELECT id FROM dim_nations WHERE nome_pais='Noruega'),
    (SELECT id FROM dim_nations WHERE nome_pais='Franca'),      
    'I', 3, '16:00', '2026-06-26'
),
(
	(SELECT id FROM dim_nations WHERE nome_pais='Senegal'),
    (SELECT id FROM dim_nations WHERE nome_pais='Generico 5'), 
    'I', 3, '16:00', '2026-06-26'
),
-- GRUPO J
(
    (SELECT id FROM dim_nations WHERE nome_pais='Argelia'),
    (SELECT id FROM dim_nations WHERE nome_pais='Austria'),	      
    'J', 3, '23:00', '2026-06-27'
),
(
    (SELECT id FROM dim_nations WHERE nome_pais='Jordania'),
    (SELECT id FROM dim_nations WHERE nome_pais='Argentina'),	
    'J', 3, '23:00', '2026-06-27'
),
-- GRUPO K
(
    (SELECT id FROM dim_nations WHERE nome_pais='Colombia'),
    (SELECT id FROM dim_nations WHERE nome_pais='Portugal'),        
    'K', 3, '20:30', '2026-06-27'
),
(
	(SELECT id FROM dim_nations WHERE nome_pais='Generico 6'),
    (SELECT id FROM dim_nations WHERE nome_pais='Uzbequistao'),
    'K', 3, '20:30', '2026-06-27'
),
-- GRUPO L
(
    (SELECT id FROM dim_nations WHERE nome_pais='Panama'),
    (SELECT id FROM dim_nations WHERE nome_pais='Inglaterra'),	      
    'L', 3, '18:00', '2026-06-27'
),
(
	(SELECT id FROM dim_nations WHERE nome_pais='Croacia'),
	(SELECT id FROM dim_nations WHERE nome_pais='Gana'),
    'L', 3, '18:00', '2026-06-27'
)