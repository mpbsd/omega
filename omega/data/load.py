import re
from datetime import date, datetime


class CPF:  # {{{1
    cpf_pattern_1 = r"([0-9]{3})([0-9]{3})([0-9]{3})([0-9]{2})"
    cpf_pattern_2 = r"([0-9]{3})\.([0-9]{3})\.([0-9]{3})-([0-9]{2})"

    cpf_1 = re.compile(r"\b%s\b" % cpf_pattern_1)
    cpf_2 = re.compile(r"\b%s\b" % cpf_pattern_2)

    def __init__(self, cpf: str) -> None:  # {{{2
        self.cpf = cpf  # }}}

    def patterns_match(self) -> bool:  # {{{2
        B = False
        if self.cpf_1.match(self.cpf) or self.cpf_2.match(self.cpf):
            B = True
        return B  # }}}

    def dissect(self) -> tuple[str] | None:  # {{{2
        DISSECT = None
        if self.patterns_match():
            if self.cpf_1.match(self.cpf):
                G1 = self.cpf_1.match(self.cpf).group(1)
                G2 = self.cpf_1.match(self.cpf).group(2)
                G3 = self.cpf_1.match(self.cpf).group(3)
                G4 = self.cpf_1.match(self.cpf).group(4)
            else:
                G1 = self.cpf_2.match(self.cpf).group(1)
                G2 = self.cpf_2.match(self.cpf).group(2)
                G3 = self.cpf_2.match(self.cpf).group(3)
                G4 = self.cpf_2.match(self.cpf).group(4)
            DISSECT = G1, G2, G3, G4
        return DISSECT  # }}}

    def strfmt(self, sty: str) -> str | None:  # {{{2
        fmt = None
        if self.patterns_match() and sty in ["raw", "std"]:
            G1, G2, G3, G4 = self.dissect()
            if sty == "raw":
                fmt = f"{G1}{G2}{G3}{G4}"
            else:
                fmt = f"{G1}.{G2}.{G3}-{G4}"
        return fmt  # }}}

    def digits_match(self) -> bool:  # {{{2
        B = False
        blacklist = ["00000000000"]
        if self.patterns_match():
            cpf = self.strfmt("raw")
            if cpf not in blacklist:
                D = [0, 0]
                for i in range(9):
                    D[0] += (10 - i) * int(cpf[i])
                for i in range(10):
                    D[1] += (11 - i) * int(cpf[i])
                D0_is_OK = ((10 * D[0]) % 11) % 10 == int(cpf[9])
                D1_is_OK = ((10 * D[1]) % 11) % 10 == int(cpf[10])
                B = D0_is_OK and D1_is_OK
        return B  # }}}

    def __repr__(self) -> str:  # {{{2
        fmt = "None"
        if self.patterns_match():
            fmt = self.strfmt("std")
        return fmt  # }}} # }}}


class DATE:  # {{{1
    re_D = r"0[1-9]|[12][0-9]|3[01]"
    re_M = r"0[1-9]|1[012]"
    re_Y = r"[0-9]{4}"

    dt_pattern_1 = f"({re_Y})({re_M})({re_D})"
    dt_pattern_2 = f"({re_D})({re_M})({re_Y})"
    dt_pattern_3 = f"({re_Y})/({re_M})/({re_D})"
    dt_pattern_4 = f"({re_D})/({re_M})/({re_Y})"
    dt_pattern_5 = f"({re_Y})-({re_M})-({re_D})"
    dt_pattern_6 = f"({re_D})-({re_M})-({re_Y})"

    dt_1 = re.compile(r"\b%s\b" % dt_pattern_1)
    dt_2 = re.compile(r"\b%s\b" % dt_pattern_2)
    dt_3 = re.compile(r"\b%s\b" % dt_pattern_3)
    dt_4 = re.compile(r"\b%s\b" % dt_pattern_4)
    dt_5 = re.compile(r"\b%s\b" % dt_pattern_5)
    dt_6 = re.compile(r"\b%s\b" % dt_pattern_6)

    def __init__(self, date_str: str) -> None:  # {{{2
        self.date_str = date_str  # }}}

    def patterns_match(self) -> bool:  # {{{2
        B = False
        if (
            self.dt_1.match(self.date_str)
            or self.dt_2.match(self.date_str)
            or self.dt_3.match(self.date_str)
            or self.dt_4.match(self.date_str)
            or self.dt_5.match(self.date_str)
            or self.dt_6.match(self.date_str)
        ):
            B = True
        return B  # }}}

    def dissect(self) -> tuple[str] | None:  # {{{2
        DISSECT = None
        if self.patterns_match():
            if self.dt_1.match(self.date_str):
                Y = self.dt_1.match(self.date_str).group(1)
                M = self.dt_1.match(self.date_str).group(2)
                D = self.dt_1.match(self.date_str).group(3)
            elif self.dt_2.match(self.date_str):
                Y = self.dt_2.match(self.date_str).group(3)
                M = self.dt_2.match(self.date_str).group(2)
                D = self.dt_2.match(self.date_str).group(1)
            elif self.dt_3.match(self.date_str):
                Y = self.dt_3.match(self.date_str).group(1)
                M = self.dt_3.match(self.date_str).group(2)
                D = self.dt_3.match(self.date_str).group(3)
            elif self.dt_4.match(self.date_str):
                Y = self.dt_4.match(self.date_str).group(3)
                M = self.dt_4.match(self.date_str).group(2)
                D = self.dt_4.match(self.date_str).group(1)
            elif self.dt_5.match(self.date_str):
                Y = self.dt_5.match(self.date_str).group(1)
                M = self.dt_5.match(self.date_str).group(2)
                D = self.dt_5.match(self.date_str).group(3)
            else:
                Y = self.dt_6.match(self.date_str).group(3)
                M = self.dt_6.match(self.date_str).group(2)
                D = self.dt_6.match(self.date_str).group(1)
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
            if is_leap_year and (m == 2):
                ndays[m] += 1
            if d <= ndays[m]:
                B = True
        return B  # }}}

    def isofmt(self) -> str | None:  # {{{2
        fmt = None
        if self.exists():
            Y, M, D = self.dissect()
            fmt = f"{Y}{M}{D}"
        return fmt  # }}}

    def date_obj(self) -> date | None:  # {{{2
        obj = None
        if self.exists():
            obj = date.fromisoformat(self.isofmt())
        return obj  # }}}

    def strfmt(self, sty: str) -> str | None:  # {{{2
        style = {
            "yyyy-mm-dd": "%Y-%m-%d",
            "yyyy/mm/dd": "%Y/%m/%d",
            "dd-mm-yyyy": "%d-%m-%Y",
            "dd/mm/yyyy": "%d/%m/%Y",
        }
        fmt = None
        if self.exists() and sty in style.keys():
            fmt = self.date_obj().strftime(style[sty])
        return fmt  # }}}

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
        fmt = "None"
        if self.exists():
            fmt = self.isofmt()
        return fmt  # }}} # }}}


def beancount(dt1: DATE, dt2: DATE) -> str:  # {{{
    DT1 = dt1.date_obj()
    DT2 = dt2.date_obj()
    if DT1 < DT2:
        beans = f"{(DT2 - DT1).days} dias"
    else:
        beans = "---"
    return beans  # }}}


save_the_date = {
    "registration": {
        "opening": DATE("20240615"),
        "closing": DATE("20240715"),
    },
    "exam": {
        "1": DATE("20240914"),
        "2": DATE("20241005"),
    },
}

today = DATE(date.today().strftime("%Y%m%d"))

payload = {
    "edition": 2024,
    "quota": 10,
    "save_the_date": save_the_date,
    "days_until": {
        "registration": {
            "opening": beancount(
                today,
                save_the_date["registration"]["opening"],
            ),
            "closing": beancount(
                today,
                save_the_date["registration"]["closing"],
            ),
        },
        "exam": {
            "1": beancount(today, save_the_date["exam"]["1"]),
            "2": beancount(today, save_the_date["exam"]["2"]),
        },
    },
}
