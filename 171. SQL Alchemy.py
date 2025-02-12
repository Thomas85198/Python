from sqlalchemy import create_engine, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# 建立 Base class (類似於 JPA 的 @Entity)
Base = declarative_base()

# 定義 Entity (類似於 Spring 的 @Entity class)


class Person(Base):
    __tablename__ = 'people'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    count: Mapped[int] = mapped_column(Integer)


# 建立連線
dbpath = 'datafile.db'
engine = create_engine(f'sqlite:///{dbpath}')
Base.metadata.create_all(engine)

# 建立 session (類似於 Spring 的 EntityManager)
Session = sessionmaker(bind=engine)
session = Session()

# 插入資料
person = Person(name='Spencer', count=66)
session.add(person)
session.commit()

# 查詢資料
result = session.execute(select(Person))
for row in result.scalars():
    print(row.name, row.count)
