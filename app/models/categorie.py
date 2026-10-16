
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Categorie(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    image: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    actif: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )

    def __repr__(self) -> str:
        return f"<Categorie(id={self.id}, nom='{self.nom}')>"