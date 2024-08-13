from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, String, Integer, Numeric


Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicle_fipe'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Numeric(10, 2), nullable=False)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano_modelo = Column(String, nullable=False)
    combustivel = Column(String, nullable=False)
    codigo_fipe = Column(String, nullable=False)
    mes_referencia = Column(String, nullable=False)
    autenticacao = Column(String, nullable=False)
    tipo_veiculo = Column(String, nullable=False)
    sigla_combustivel = Column(String, nullable=False)
    data_consulta  = Column(String, nullable=False)

    def __repr__(self):
        return f'Vehicle (id={self.id}, marca={self.marca}, modelo={self.modelo})' 

