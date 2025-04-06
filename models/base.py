from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base

from services.db import SessionLocal

Base = declarative_base()


class CRUDMixin:
    @classmethod
    def create(cls, **fields):
        try:
            with SessionLocal() as db:
                new_entity = cls(**fields)
                db.add(new_entity)
                db.commit()
                db.refresh(new_entity)

                return new_entity

        except SQLAlchemyError as e:
            raise ValueError(f"Failed to create {cls.__str__}: {str(e)}")

    @classmethod
    def find(cls, limit=25, offset=0, **filters):
        try:
            with SessionLocal() as db:
                entities = db.query(cls)

                if filters:
                    conditions = [getattr(cls, field_name) == value for field_name, value in filters.items()]
                    entities.filter(conditions)

                entities.limit(limit).offset(offset).all()

                total_count = db.query(cls).count()

                return entities, total_count

        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Failed to find {cls.__str__}: {str(e)}")

    @classmethod
    def find_one(cls, **filters):
        try:
            with SessionLocal() as db:
                conditions = [getattr(cls, field_name) == value for field_name, value in filters.items()]

                entity = db.query(cls).filter(*conditions).first()

                return entity

        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Failed to find {cls.__str__}: {str(e)}")

    @classmethod
    def update(cls, id, **fields):
        try:
            with SessionLocal() as db:
                entity = db.query(cls).filter(getattr(cls, "id") == id).first()

                for field_name, value in fields.items():
                    setattr(entity, field_name, value)

                db.commit()
                db.refresh(entity)

                return entity

        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Failed to find {cls.__str__}: {str(e)}")
