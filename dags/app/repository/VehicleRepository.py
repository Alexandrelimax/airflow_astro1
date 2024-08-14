from sqlalchemy.exc import SQLAlchemyError
from app.model.VehicleModel import Vehicle  


class VehicleRepository:
    def __init__(self, connection):
        self.session = connection.get_session()

    def insert(self, vehicle_data):
        try:
            vehicle = Vehicle(**vehicle_data)
            self.session.add(vehicle)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
        finally:
            self.session.close()


    def get_vehicle_by_id(self, vehicle_id):
        try:
            return self.session.query(Vehicle).filter_by(id=vehicle_id).first()
        except SQLAlchemyError as e:
            print(f"Error: {e}")
        finally:
            self.session.close()


    def get_all(self):
        try:
            return self.session.query(Vehicle).all()
        except SQLAlchemyError as e:
            print(f"Error: {e}")
        finally:
            self.session.close()
