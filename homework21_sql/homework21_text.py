# 1. Create/Drop table:
# CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
# INTEGER);
# DROP TABLE shopping

# the create table functions here used to create a new table with a name shopping while the keys of this table are id,name and amount
# drop table function is used to delete a table in this instance the table that been deleted is shopping

# 2. Rename table:
# ALTER table shopping RENAME to shopp
# ALTER table shopp RENAME to shopping

# this function used to rename table in first alter option table named "shopping" is renamed to "shopp"
# while in second alter table is renamed back to "shopping"

# 3. Insert rows into table:
# INSERT INTO shopping VALUES (1, 'Avokado', 5);
# INSERT INTO shopping VALUES (2, 'Milk', 2);
# INSERT INTO shopping VALUES (3, 'Bread', 3);
# INSERT INTO shopping VALUES (4, 'Chocolate', 8);
# INSERT INTO shopping VALUES (5, 'Bamba', 5);
# INSERT INTO shopping VALUES (6, 'Orange', 10);

# the function insert is used to insert values into given keys of the table
# as we can see in this instance each insert gives the table named "shopping" values: (id,name, amount)

# 4. Display table:
# select * from shopping

# select function allows us to display selected information from the table or as it used here to display the whole table at once

# 5. ?
# SELECT id, name FROM shopping

# on contrary to the last function this select is used to show only id and name from each row in the table

# 6. ?
# SELECT * FROM shopping WHERE amount > 5
# SELECT * FROM shopping WHERE amount = 2
# SELECT * FROM shopping WHERE name LIKE 'Bamba'

# this time each select only shows rows where given conditions are met
# for example in first one only data where amount bigger than 5 fill be shown, second one only data where amount is equal to 2 will be shown
# and finally in the third one only data where key name is "Bamba" will be shown
