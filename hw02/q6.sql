\* Q6 *\

UPDATE rdata
set moment = '2020-03-27'::DATE
where a='bagel' or a='scone';

select * from rdata;