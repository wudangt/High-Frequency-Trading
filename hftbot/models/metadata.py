#!/usr/bin/env python
from sqlalchemy import (
    Column,
    Text,
)

from . import HftbotBase


class Metadata(HftbotBase):
    __tablename__ = "Metadata"

    key = Column(Text, primary_key=True, nullable=False)
    value = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"Metadata(key='{self.key}', value='{self.value}')"
