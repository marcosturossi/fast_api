from src.models import models, data_base


class Manager:
    db = data_base.SessionLocal()
    models = None

    def create(self, data):
        instance = self.models(**data)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get_by(self, id):
        return self.db.query(models.Book).filter(models.Book.id == id).first()

    def get_all(self):
        return self.db.query(models.Book).all()
