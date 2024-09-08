import re
from datetime import date, datetime


class CPF:  # {{{1
    re_cpfnr = re.compile(r"\b(\d{3})\.?(\d{3})\.?(\d{3})-?(\d{2})\b")

    def __init__(self, cpfnr: str) -> None:  # {{{2
        self.cpfnr = cpfnr  # }}}

    def pattern_match(self) -> bool:  # {{{2
        B = False
        if self.re_cpfnr.match(self.cpfnr):
            B = True
        return B  # }}}

    def strfmt(self, fmt: str) -> str | None:  # {{{2
        cpf_strfmt = None
        style = {
            "raw": self.re_cpfnr.sub(r"\1\2\3\4", self.cpfnr),
            "fmt": self.re_cpfnr.sub(r"\1.\2.\3-\4", self.cpfnr),
        }
        if self.pattern_match() and fmt in style.keys():
            cpf_strfmt = style[fmt]
        return cpf_strfmt  # }}}

    def digits_match(self) -> bool:  # {{{2
        B = False
        if self.pattern_match():
            cpf = self.strfmt("raw")
            blacklist = ["00000000000"]
            if cpf not in blacklist:
                D = [0, 0]
                for i in range(9):
                    D[0] += (10 - i) * int(cpf[i])
                for i in range(10):
                    D[1] += (11 - i) * int(cpf[i])
                D0_is_OK = ((10 * D[0]) % 11) % 10 == int(cpf[9])
                D1_is_OK = ((10 * D[1]) % 11) % 10 == int(cpf[10])
                if D0_is_OK and D1_is_OK:
                    B = True
        return B  # }}}

    def __repr__(self) -> bool:  # {{{2
        return self.strfmt("fmt")  # }}} # }}}


class DATE:  # {{{1
    re_D = r"0[1-9]|[12][0-9]|3[01]"
    re_M = r"0[1-9]|1[012]"
    re_Y = r"[0-9]{4}"

    dt_1 = re.compile(r"\b(%s)[/-]?(%s)[/-]?(%s)\b" % (re_Y, re_M, re_D))
    dt_2 = re.compile(r"\b(%s)[/-]?(%s)[/-]?(%s)\b" % (re_D, re_M, re_Y))

    def __init__(self, date_str: str) -> None:  # {{{2
        self.date_str = date_str  # }}}

    def patterns_match(self) -> bool:  # {{{2
        B = False
        if self.dt_1.match(self.date_str) or self.dt_2.match(self.date_str):
            B = True
        return B  # }}}

    def dissect(self) -> tuple[str] | None:  # {{{2
        DISSECT = None
        if self.patterns_match():
            if self.dt_1.match(self.date_str):
                Y = self.dt_1.match(self.date_str).group(1)
                M = self.dt_1.match(self.date_str).group(2)
                D = self.dt_1.match(self.date_str).group(3)
            else:
                Y = self.dt_2.match(self.date_str).group(3)
                M = self.dt_2.match(self.date_str).group(2)
                D = self.dt_2.match(self.date_str).group(1)
            DISSECT = Y, M, D
        return DISSECT  # }}}

    def exists(self) -> bool:  # {{{2
        B = False
        if self.patterns_match():
            Y, M, D = self.dissect()
            y, m, d = int(Y), int(M), int(D)
            ndays = {
                1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31,
            }
            is_leap_year = False
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                is_leap_year = True
            if (is_leap_year is True) and (m == 2):
                ndays[m] += 1
            if d <= ndays[m]:
                B = True
        return B  # }}}

    def stdfmt(self) -> str | None:  # {{{2
        std_format = None
        if self.exists():
            Y, M, D = self.dissect()
            std_format = f"{Y}{M}{D}"
        return std_format  # }}}

    def date_obj(self) -> date | None:  # {{{2
        dobj = None
        if self.exists():
            dobj = datetime.fromisoformat(self.stdfmt())
        return dobj  # }}}

    def strfmt(self, fmt: str) -> str | None:  # {{{2
        strfmt = None
        if self.exists():
            style = {
                "yyyy-mm-dd": "%Y-%m-%d",
                "yyyy/mm/dd": "%Y/%m/%d",
                "dd-mm-yyyy": "%d-%m-%Y",
                "dd/mm/yyyy": "%d/%m/%Y",
            }
            if fmt in style.keys():
                strfmt = self.date_obj().strftime(style[fmt])
        return strfmt  # }}}

    def is_not_in_the_future(self) -> bool:  # {{{2
        B = False
        if self.exists():
            if self.date_obj() <= datetime.now():
                B = True
        return B  # }}}

    def year_belongs_to_selected_range(self) -> bool:  # {{{2
        B = False
        if self.exists():
            if self.date_obj().year in range(1974, 2021):
                B = True
        return B  # }}}

    def __repr__(self) -> str:  # {{{2
        return self.stdfmt()  # }}} # }}}


def beancount(dt1: date, dt2: date) -> str:  # {{{
    if dt1 < dt2:
        beans = f"{(dt2 - dt1).days} dias"
    else:
        beans = "---"
    return beans  # }}}


save_the_date = {  # {{{
    "registration": {
        "opening": DATE("20240615"),
        "closing": DATE("20240715"),
    },
    "exam": {
        "1": DATE("20240914"),
        "2": DATE("20241005"),
    },
}  # }}}


payload = {  # {{{
    "edition": 2024,
    "quota": 10,
    "save_the_date": save_the_date,
    "days_until": {
        "registration": {
            "opening": beancount(
                datetime.today(),
                save_the_date["registration"]["opening"].date_obj(),
            ),
            "closing": beancount(
                datetime.today(),
                save_the_date["registration"]["closing"].date_obj(),
            ),
        },
        "exam": {
            "1": beancount(
                datetime.today(), save_the_date["exam"]["1"].date_obj()
            ),
            "2": beancount(
                datetime.today(), save_the_date["exam"]["2"].date_obj()
            ),
        },
    },
}  # }}}
