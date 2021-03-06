from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config


# Create our engine based on the db specified in our config.
ENGINE = create_engine(config.DATABASE)

# Create all tables if they don't exist
config.Base.metadata.create_all(ENGINE)

# Define our session object which we'll instantiate in other modules.
Session = sessionmaker(ENGINE)