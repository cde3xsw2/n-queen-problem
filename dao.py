from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import logging
import sys


db = create_engine('postgresql://postgres:postgres@db:5432/nqueen')#,echo=True)
Base = declarative_base()

class Solution(Base):
    __tablename__ = 'solutions'
    id = Column(Integer, Sequence('solution_id_seq'), primary_key=True)
    n = Column(Integer)
    result = Column(JSON)

    def __repr__(self):
        return "<User(n='%s', result='%s')>" % (
                                self.n, self.result)

Session = sessionmaker(db)
session = Session()
try:
    Base.metadata.create_all(db)
except:
    print(sys.exc_info()[1])

def save_solutions(n,solutions):
    entities =  [Solution(n=n,result=solution)  for solution in solutions]
    session.add_all(entities)
    session.commit()

def delete_solutions(n):
    session.query(Solution).filter(Solution.n == n).delete()
    session.commit()

def list_solutions(n):
    return session.query(Solution).filter(Solution.n == n).all()


#ed_user = Solution(n=8, result=[1,2,3,4,5])
#session.add(ed_user)
#session.commit()
