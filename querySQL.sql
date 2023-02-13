SELECT
	*,
    CASE 
		WHEN glic_valor >= 150 THEN 'Hiperglicemia'
        WHEN glic_valor >= 70 THEN 'Normal'
        ELSE 'Hipoglicemia'
		END AS glic_resultado,
	CASE
		WHEN EXTRACT(HOUR FROM glic_data) >= 19 THEN 'Noite'
        WHEN EXTRACT(HOUR FROM glic_data) >= 13 THEN 'Tarde'
        WHEN EXTRACT(HOUR FROM glic_data) >= 5 THEN 'Manhã'
        ELSE 'Noite'
        END AS hora_dia
FROM Glicemia.glic_medicoes