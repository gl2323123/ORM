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

for ali in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[ali.get('model')]
    session.add(model(id=ali.get('pk'), **ali.get('fields')))
session.commit()

borz_id = input('ID Автора: ')


borz = session.query(Book.title, Shop.name, Stock.count, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == borz_id).all()




print(borz)

session.close()