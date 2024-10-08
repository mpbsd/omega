from functools import reduce

from app.data.DATE import DATE


def test_DATE():
    date = {  # {{{
        0: {
            "date": DATE("10032004"),
            "patterns_match": True,
            "dissect": ("2004", "03", "10"),
            "year_belongs_to_selected_range": True,
            "exists": True,
        },
        1: {
            "date": DATE("20040310"),
            "patterns_match": True,
            "dissect": ("2004", "03", "10"),
            "year_belongs_to_selected_range": True,
            "exists": True,
        },
        2: {
            "date": DATE("10/03/2004"),
            "patterns_match": True,
            "dissect": ("2004", "03", "10"),
            "year_belongs_to_selected_range": True,
            "exists": True,
        },
        3: {
            "date": DATE("2004/03/10"),
            "patterns_match": True,
            "dissect": ("2004", "03", "10"),
            "year_belongs_to_selected_range": True,
            "exists": True,
        },
        4: {
            "date": DATE("10-03-2004"),
            "patterns_match": True,
            "dissect": ("2004", "03", "10"),
            "year_belongs_to_selected_range": True,
            "exists": True,
        },
        5: {
            "date": DATE("2004-03-10"),
            "patterns_match": True,
            "dissect": ("2004", "03", "10"),
            "year_belongs_to_selected_range": True,
            "exists": True,
        },
        6: {
            "date": DATE(" 10032000"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        7: {
            "date": DATE("20040310 "),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        8: {
            "date": DATE("10/032000"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        9: {
            "date": DATE("200403/10"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        10: {
            "date": DATE("10-03 2004"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        11: {
            "date": DATE("2004 10-03"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        12: {
            "date": DATE("2023-02-29"),
            "patterns_match": True,
            "dissect": ("2023", "02", "29"),
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        13: {
            "date": DATE("2024-02-29"),
            "patterns_match": True,
            "dissect": ("2024", "02", "29"),
            "year_belongs_to_selected_range": False,
            "exists": True,
        },
        14: {
            "date": DATE("2024-20-29"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        15: {
            "date": DATE("2024/10-31"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
        16: {
            "date": DATE("2024/10/31"),
            "patterns_match": True,
            "dissect": ("2024", "10", "31"),
            "year_belongs_to_selected_range": False,
            "exists": True,
        },
        17: {
            "date": DATE("32-10-2024"),
            "patterns_match": False,
            "dissect": None,
            "year_belongs_to_selected_range": False,
            "exists": False,
        },
    }  # }}}

    result = {  # {{{
        k: {
            "date": date[k],
            "patterns_match": date[k]["date"].patterns_match(),
            "dissect": date[k]["date"].dissect(),
            "year_belongs_to_selected_range": date[k][
                "date"
            ].year_belongs_to_selected_range(),
            "exists": date[k]["date"].exists(),
        }
        for k in date.keys()
    }  # }}}

    state = [  # {{{
        [
            (
                1
                if result[k]["patterns_match"] == date[k]["patterns_match"]
                else 0
            ),
            1 if result[k]["dissect"] == date[k]["dissect"] else 0,
            (
                1
                if result[k]["year_belongs_to_selected_range"]
                == date[k]["year_belongs_to_selected_range"]
                else 0
            ),
            1 if result[k]["exists"] == date[k]["exists"] else 0,
        ]
        for k in date.keys()
    ]  # }}}

    for k in date.keys():  # {{{
        print(
            "%02d: %2d %2d %2d %2d | %s"
            % (
                k,
                state[k][0],
                state[k][1],
                state[k][2],
                state[k][3],
                True if reduce(lambda x, y: x * y, state[k]) == 1 else False,
            )
        )  # }}}


def main():
    test_DATE()


if __name__ == "__main__":
    main()
