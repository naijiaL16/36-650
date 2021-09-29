/* Q4 */

CREATE TABLE new_table(
	player integer references more_player_stats,
	prl NUMERIC,
	position TEXT
);

insert into new_table (player,prl) (select id,round(per - 67*va/(gp*minutes),1) 
									from more_player_stats);

UPDATE new_table
	SET position='PF' 
	where prl>=11.3;
	
UPDATE new_table
	SET position='PG' 
	where prl>=10.8 and prl<11.3;
	
UPDATE new_table
	SET position='C' 
	where prl>=10.6 and prl<10.8;

UPDATE new_table
	SET position='SG/SF'
	where prl>=0 and prl<10.6;
	
SELECT * FROM new_table LIMIT 10;