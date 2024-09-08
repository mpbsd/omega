class Professor(UserMixin, db.Model):
    taxnr: so.Mapped[str] = so.mapped_column(sa.String(11), primary_key=True)
    fname: so.Mapped[str] = so.mapped_column(sa.String(255))
    email: so.Mapped[str] = so.mapped_column(
        sa.String(255), index=True, unique=True
    )
    pswrd: so.Mapped[Optional[str]] = so.mapped_column(sa.String(255))

    def set_password(self, password):
        self.pswrd = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pswrd, password)

    def get_id(self):
        return self.taxnr

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {"reset_password": self.taxnr, "exp": time() + expires_in},
            Config.SECRET_KEY,
            algorithm="HS256",
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            taxnr = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])[
                "reset_password"
            ]
        except jwt.exceptions.InvalidTokenError as Err:
            print(Err)
            return None
        return db.session.get(Professor, taxnr)

    @staticmethod
    def get_registration_request_token(email, expires_in=600):
        return jwt.encode(
            {"email": email, "exp": time() + expires_in},
            Config.SECRET_KEY,
            algorithm="HS256",
        )

    @staticmethod
    def verify_registration_request_token(token):
        try:
            email = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])[
                "email"
            ]
        except jwt.exceptions.InvalidTokenError as Err:
            print(Err)
            return None
        return email

    def __repr__(self):
        return f"Professor {self.taxnr}"
