from sqlalchemy import create_engine
DATABASE_URL="sqlite:///company.db"
engine = create_engine(DATABASE_URL)