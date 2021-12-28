import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, select,DATETIME,desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert, delete, update
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
Base = declarative_base()

engine = create_engine("postgresql+psycopg2://postgres:13241340@localhost/medical_institution")
conn = engine.connect()



#######################СТАТУС_ПРИЁМА#############################

class reception_status(Base):
    __tablename__ = 'reception_status'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __repr__(self):
        return f'{self.id} {self.name}'

#######################СПЕЦИАЛИЗАЦИЯ#############################

class specialization(Base):
    __tablename__ = 'specialization'
    id = Column(Integer, primary_key=True)
    name_spec = Column(String(100))

    def __repr__(self):
        return f'{self.id} {self.name_spec}'

#######################ДЕНЬ#############################

class day(Base):
    __tablename__ = 'day'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __repr__(self):
        return f'{self.id} {self.name}'

#######################ПАЦИЕНТ#############################

class patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __repr__(self):
        return f'{self.id} {self.name}'


#######################КАБИНЕТЫ#############################

class offices(Base):
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    cab_num = Column(Integer)

    def __repr__(self):
        return f'{self.id} {self.cab_num}'

#######################ПЕРСОНАЛ#############################

class personnel(Base):
    __tablename__ = 'personnel'
    id = Column(Integer, primary_key=True)
    id_spec = Column(Integer, ForeignKey('specialization.id'))
    id_office = Column(Integer, ForeignKey('offices.id'))
    name = Column(String(100))

    def __repr__(self):
        return f'{self.id} {self.id_spec} {self.id_office} {self.name}'

    #######################Время_работы#############################

class working_hours(Base):
    __tablename__ = 'working_hours'
    id = Column(Integer, primary_key=True)
    id_day = Column(Integer, ForeignKey('day.id'))
    id_personnel = Column(Integer, ForeignKey('personnel.id'))
    work_hours = Column(String)
    free_time = Column(String)
    break_time = Column(String)

    def __repr__(self):
        return f'{self.id} {self.id_day} {self.id_personnel} {self.work_hours} {self.free_time} {self.break_time}'

#######################Приём#############################id, id_patient, id_office, id_reception_status, id_personnel,id_spec, date_insurance_cost

class reception(Base):
    __tablename__ = 'reception'
    id = Column(Integer, primary_key=True)
    id_patient = Column(Integer, ForeignKey('patient.id'))
    id_office = Column(Integer, ForeignKey('offices.id'))
    id_reception_status = Column(Integer, ForeignKey('reception_status.id'))
    id_personnel = Column(Integer, ForeignKey('personnel.id'))
    id_spec = Column(Integer, ForeignKey('specialization.id'))
    date = Column(DATETIME)

    def __repr__(self):
        return f'{self.id} {self.id_patient} {self.id_office} {self.id_reception_status} {self.id_personnel} {self.id_spec} {self.date}'

#######################Мед_книга#############################

class med_knigа(Base):
    __tablename__ = 'med_knigа'
    id = Column(Integer, primary_key=True)
    id_patient = Column(Integer, ForeignKey('patient.id'))
    diagnoz = Column(String(100))

    def __repr__(self):
        return f'{self.id} {self.id_patient} {self.diagnoz}'



Session = sessionmaker(bind=engine)
session = Session()
