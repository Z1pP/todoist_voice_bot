import logging
from contextlib import contextmanager

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

from config import settings
from database.models import Base

logger = logging.getLogger(__name__)

# Создаем движок базы данных
engine = create_engine(f"sqlite:///{settings.db_name}")

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)

# Создаем фабрику сессий
Session = sessionmaker(bind=engine)


@contextmanager
def get_session():
    """Context manager для управления сессией."""
    db_session = Session()  # Создаем новую сессию
    try:
        yield db_session  # Передаем управление сессией
        db_session.commit()  # Коммитим изменения
        logger.info("Транзакция успешно завершена.")
    except exc.SQLAlchemyError as e:
        logger.error(f"Произошла ошибка в транзакции: {e}")
        db_session.rollback()  # Откатываем изменения
        raise  # Выбрасываем исключение для обработки выше
    finally:
        db_session.close()  # Закрываем сессию
        logger.info("Сессия успешно закрыта.")
