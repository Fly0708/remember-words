from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import func,String, text

from ..base import Base


class Words(Base):
    __tablename__ = 'words'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    word: Mapped[str] = mapped_column(String(255), unique=True)
    create_time: Mapped[datetime | None] = mapped_column( server_default=text('CURRENT_TIMESTAMP'))
    update_time: Mapped[datetime | None] = mapped_column( server_default=text('CURRENT_TIMESTAMP'), onupdate=func.now())

    def __repr__(self):
        return f"Words(id={self.id}, word='{self.word}', create_time={self.create_time}, update_time={self.update_time})"

