# %% 
 
from sqlalchemy import create_engine

# Replace with your database connection string
db_url = "postgresql://username:password@localhost/mydatabase"
engine = create_engine(db_url)
