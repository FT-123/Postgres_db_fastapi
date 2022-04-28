from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:2277@db:5432/postgres'.format('service_name_of_postgres'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Model = declarative_base()