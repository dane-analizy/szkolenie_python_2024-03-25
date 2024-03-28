from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///lokalna_baza.sqlite")

db_conn = engine.connect()

sql_queries = [
    """
create table players (
	player_id serial primary key,
	first_name text not null,
	last_name text not null,
	height numeric not null,
	weight numeric not null
);
""",
    """
insert into players (first_name,last_name,height,weight)  
values ('Jan', 'Kowalski', 1.84, 85);  
""",
    """  
insert into players (first_name,last_name,height,weight)  
values ('Marian', 'Nowak', 1.90, 50);  
""",
    """
insert into players (first_name,last_name,height,weight)  
values ('Zdzisław', 'Dyrman', 1.73 ,74);  
""",
    """
insert into players (first_name,last_name,height,weight)  
values ('Zenon', 'Brzęczyk', 1.64, 95);  
""",
    """
insert into players (first_name,last_name,height,weight)  
values ('Chuck','Norris', 1.82, 78);  
""",
    """
insert into players (first_name,last_name,height,weight)  
values ('Krzysztof','Jarzyna', 1.68, 70);
""",
]

for sql_query in sql_queries:
    db_conn.execute(text(sql_query))
    res = db_conn.commit()
    print(res)
