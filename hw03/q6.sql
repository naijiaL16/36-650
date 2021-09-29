/* Q6 */

ALTER TABLE player_bios
ADD COLUMN inches NUMERIC;

UPDATE player_bios
SET inches = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

ALTER TABLE player_bios
DROP COLUMN height;

ALTER TABLE player_bios
RENAME COLUMN Inches TO height;

select firstname, lastname, height from player_bios LIMIT 5;