from functools import reduce

from omega.data.CPF import CPF


def test_CPF():
    cpf = [
        (CPF("000.000.001-91"), 1),
        (CPF("000.000.00191"), 0),
        (CPF("000.000001-91"), 0),
        (CPF("000.00000191"), 0),
        (CPF("000000.001-91"), 0),
        (CPF("000000.00191"), 0),
        (CPF("000000001-91"), 0),
        (CPF("00000000191"), 1),
        (CPF("000 000 001 91"), 0),
        (CPF("000 000 00191"), 0),
        (CPF("000 000001 91"), 0),
        (CPF("000 00000191"), 0),
        (CPF("000000 001 91"), 0),
        (CPF("000000 00191"), 0),
        (CPF(" 000.000.001-91"), 0),
        (CPF("000.000.001-91 "), 0),
        (CPF(" 000.000.001-91 "), 0),
        (CPF(" 00000000191"), 0),
        (CPF("00000000191 "), 0),
        (CPF(" 00000000191 "), 0),
    ]

    N = len(cpf)

    state = [[1 for j in range(5)] for i in range(N)]

    for i in range(N):
        state[i][0] = 1 if cpf[i][0].patterns_match() == True else 0
        state[i][1] = (
            1 if cpf[i][0].dissect() == ("000", "000", "001", "91") else 0
        )
        state[i][2] = 1 if cpf[i][0].strfmt("raw") == "00000000191" else 0
        state[i][3] = 1 if cpf[i][0].strfmt("std") == "000.000.001-91" else 0
        state[i][4] = 1 if cpf[i][0].digits_match() == True else 0

    for i in range(N):
        print(
            "%02d: %2d %2d %2d %2d %2d | %s"
            % (
                i,
                state[i][0],
                state[i][1],
                state[i][2],
                state[i][3],
                state[i][4],
                reduce(lambda x, y: x * y, state[i]) == cpf[i][1],
            )
        )


def main():
    test_CPF()


if __name__ == "__main__":
    main()
