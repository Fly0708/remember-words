from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import func,String, text, Text

from ..base import Base


class AIExplain(Base):
    __tablename__ = 'ai_explain'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    word_id: Mapped[int] = mapped_column()
    word_text: Mapped[str] = mapped_column(String(255))
    explanation: Mapped[str] = mapped_column(Text)
    model:Mapped[str] = mapped_column(String(50))
    create_time: Mapped[datetime | None] = mapped_column( server_default=func.now())
    update_time: Mapped[datetime | None] = mapped_column( server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return (f"AIExplain(id={self.id}, word_id={self.word_id}, word_text='{self.word_text}', "
                f"explanation='{self.explanation}', model='{self.model}', "
                f"create_time={self.create_time}, update_time={self.update_time})")