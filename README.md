# sqlmapTamperScripts
Custom SQLMap Tamper Scripts to bypass html encoding.

quote2dollar.py — replaces single quote (') to PostgreSQL Tag notation \$\$. 
Example: 
```
insert into test (name) values ('kek');
```
Becomes:
```
insert into test (name) values ($$kek$$);
```
nodoublequotes.py — deletes double quotes (") to avoid errors with htmlencode while sqlmap uses field names with ".
Example: 
```
select "name", "value" from tblname;
```
Becomes:
```
select name, value from tblname;
```
