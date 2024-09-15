class School(db.Model):
    inep: so.Mapped[str] = so.mapped_column(sa.String(8), primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(96))
    city: so.Mapped[str] = so.mapped_column(sa.String(27))
    zone: so.Mapped[str] = so.mapped_column(sa.String(6))
    tier: so.Mapped[str] = so.mapped_column(sa.String(7))
    code: so.Mapped[str] = so.mapped_column(sa.String(9))
    pnum: so.Mapped[str] = so.mapped_column(sa.String(14), nullable=True)
    latd: so.Mapped[str] = so.mapped_column(sa.Float, nullable=True)
    lotd: so.Mapped[str] = so.mapped_column(sa.Float, nullable=True)

    def __repr__(self):
        return f"School {self.inep}"
