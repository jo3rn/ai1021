# factor 10: Dev/prod parity (keeping environments as similar as possible)
import os
from sqlalchemy import create_engine, MetaData, Table

# Load environment-specific configuration
if os.getenv('ENV') == 'production':
    from prod_config import DATABASE_URL # 'postgresql://user:password@localhost/prod_db'
else:
    from dev_config import DATABASE_URL # 'sqlite:///dev.db'

engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# Access table with case-sensitive name
users_table = Table('Users', metadata, autoload_with=engine)

# Query the table
with engine.connect() as connection:
    result = connection.execute(users_table.select())
    for row in result:
        print(row)
