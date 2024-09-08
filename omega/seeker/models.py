class Student(db.Model):
    cpfnr: so.Mapped[str] = so.mapped_column(sa.String(11), primary_key=True)
    fname: so.Mapped[str] = so.mapped_column(sa.String(255))
    birth: so.Mapped[str] = so.mapped_column(sa.String(8))
    email: so.Mapped[str] = so.mapped_column(
        sa.String(255), index=True, unique=True
    )

    def __repr__(self):
        return f"Student {self.cpfnr}"
