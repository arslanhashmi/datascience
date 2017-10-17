
from cassandra.cluster import Cluster


cluster = Cluster()
session = cluster.connect('demo')
session.execute("""

insert into users (lastname, age, city, email, firstname) values ('Jones', 35, 'Austin', 'bob@example.com', 'Bob')

""")