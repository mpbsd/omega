import re


class CPF:
    cpf_pattern_1 = r"([0-9]{3})([0-9]{3})([0-9]{3})([0-9]{2})"
    cpf_pattern_2 = r"([0-9]{3})\.([0-9]{3})\.([0-9]{3})-([0-9]{2})"

    cpf_1 = re.compile(r"\b%s\b" % cpf_pattern_1)
    cpf_2 = re.compile(r"\b%s\b" % cpf_pattern_2)

    def __init__(self, cpf: str) -> None:
        self.cpf = cpf  # }}}

    def patterns_match(self) -> bool:
        B = False
        if self.cpf_1.match(self.cpf) or self.cpf_2.match(self.cpf):
            B = True
        return B

    def dissect(self) -> tuple[str] | None:
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
        return DISSECT

    def strfmt(self, sty: str) -> str | None:
        fmt = None
        if self.patterns_match() and sty in ["raw", "std"]:
            G1, G2, G3, G4 = self.dissect()
            if sty == "raw":
                fmt = f"{G1}{G2}{G3}{G4}"
            else:
                fmt = f"{G1}.{G2}.{G3}-{G4}"
        return fmt

    def digits_match(self) -> bool:
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
        return B

    def __repr__(self) -> str:
        fmt = "None"
        if self.patterns_match():
            fmt = self.strfmt("std")
        return fmt
