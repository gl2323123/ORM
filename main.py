import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker

from models import create_tables,Publisher,Shop,Book,Stock,Sale

DSN = "postgresql://postgres:postgres@localhost:5432/ORM"

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

json_data = open('tests_data.json').read()

Session = sessionmaker(bind=engine)
session = Session()

data = json.loads(json_data)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()