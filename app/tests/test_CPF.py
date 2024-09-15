from functools import reduce

from app.data.CPF import CPF


def test_CPF():
    cpfnr = {  # {{{
        0: {
            "cpfnr": CPF("000.000.001-91"),
            "patterns_match": True,
            "dissect": ("000", "000", "001", "91"),
            "strfmt_raw": "00000000191",
            "strfmt_std": "000.000.001-91",
            "digits_match": True,
        },
        1: {
            "cpfnr": CPF("000.000.00191"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        2: {
            "cpfnr": CPF("000.000001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        3: {
            "cpfnr": CPF("000.00000191"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        4: {
            "cpfnr": CPF("000000.001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        5: {
            "cpfnr": CPF("000000.00191"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        6: {
            "cpfnr": CPF("000000001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        7: {
            "cpfnr": CPF("00000000191"),
            "patterns_match": True,
            "dissect": ("000", "000", "001", "91"),
            "strfmt_raw": "00000000191",
            "strfmt_std": "000.000.001-91",
            "digits_match": True,
        },
        8: {
            "cpfnr": CPF(" 000.000.001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        9: {
            "cpfnr": CPF("000.000.001-91 "),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        10: {
            "cpfnr": CPF(" 000.000.001-91 "),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        11: {
            "cpfnr": CPF("000 000 001 91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        12: {
            "cpfnr": CPF("000.000.001.91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        13: {
            "cpfnr": CPF("000.000.001/91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        14: {
            "cpfnr": CPF("000000001/91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        15: {
            "cpfnr": CPF("000 000.001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        16: {
            "cpfnr": CPF("00.000.001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        17: {
            "cpfnr": CPF("0000.000.001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        18: {
            "cpfnr": CPF("000.000.001-912"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
        19: {
            "cpfnr": CPF("000.000.001-92"),
            "patterns_match": True,
            "dissect": ("000", "000", "001", "92"),
            "strfmt_raw": "00000000192",
            "strfmt_std": "000.000.001-92",
            "digits_match": False,
        },
        20: {
            "cpfnr": CPF("000.0001.001-91"),
            "patterns_match": False,
            "dissect": None,
            "strfmt_raw": None,
            "strfmt_std": None,
            "digits_match": False,
        },
    }  # }}}

    result = {  # {{{
        k: {
            "cpfnr": cpfnr[k]["cpfnr"],
            "patterns_match": cpfnr[k]["cpfnr"].patterns_match(),
            "dissect": cpfnr[k]["cpfnr"].dissect(),
            "strfmt_raw": cpfnr[k]["cpfnr"].strfmt("raw"),
            "strfmt_std": cpfnr[k]["cpfnr"].strfmt("std"),
            "digits_match": cpfnr[k]["cpfnr"].digits_match(),
        }
        for k in cpfnr.keys()
    }  # }}}

    state = [  # {{{
        [
            (
                1
                if result[k]["patterns_match"] == cpfnr[k]["patterns_match"]
                else 0
            ),
            1 if result[k]["dissect"] == cpfnr[k]["dissect"] else 0,
            1 if result[k]["strfmt_raw"] == cpfnr[k]["strfmt_raw"] else 0,
            1 if result[k]["strfmt_std"] == cpfnr[k]["strfmt_std"] else 0,
            1 if result[k]["digits_match"] == cpfnr[k]["digits_match"] else 0,
        ]
        for k in cpfnr.keys()
    ]  # }}}

    for k in cpfnr.keys():  # {{{
        print(
            "%02d: %2d %2d %2d %2d %2d | %s"
            % (
                k,
                state[k][0],
                state[k][1],
                state[k][2],
                state[k][3],
                state[k][4],
                True if reduce(lambda x, y: x * y, state[k]) == 1 else False,
            )
        )  # }}}


def main():
    test_CPF()


if __name__ == "__main__":
    main()
