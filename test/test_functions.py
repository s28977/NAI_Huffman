from src.functions import map_to_symbols_list


def test_map_to_symbols():
    string = 'abcabaaabcedfabaccafc'
    symbols = map_to_symbols_list(string)
    assert symbols[0].order == 0
    assert symbols[1].order == 1
    assert symbols[2].order == 2
    assert symbols[3].order == 3
    assert symbols[4].order == 4
    assert symbols[5].order == 5

    assert symbols[0].char == 'a'
    assert symbols[1].char == 'b'
    assert symbols[2].char == 'c'
    assert symbols[3].char == 'e'
    assert symbols[4].char == 'd'
    assert symbols[5].char == 'f'

    assert symbols[0].count == 8
    assert symbols[1].count == 4
    assert symbols[2].count == 5
    assert symbols[3].count == 1
    assert symbols[4].count == 1
    assert symbols[5].count == 2
