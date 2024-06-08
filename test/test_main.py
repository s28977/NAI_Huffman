from src.main import map_to_subtrees_list


def test_map_to_subtrees_list():
    string = 'abcabaaabcedfabaccafc'
    subtrees = map_to_subtrees_list(string)
    assert subtrees[0].symbol.order == 0
    assert subtrees[1].symbol.order == 1
    assert subtrees[2].symbol.order == 2
    assert subtrees[3].symbol.order == 3
    assert subtrees[4].symbol.order == 4
    assert subtrees[5].symbol.order == 5

    assert subtrees[0].symbol.char == 'a'
    assert subtrees[1].symbol.char == 'b'
    assert subtrees[2].symbol.char == 'c'
    assert subtrees[3].symbol.char == 'e'
    assert subtrees[4].symbol.char == 'd'
    assert subtrees[5].symbol.char == 'f'

    assert subtrees[0].count == 8
    assert subtrees[1].count == 4
    assert subtrees[2].count == 5
    assert subtrees[3].count == 1
    assert subtrees[4].count == 1
    assert subtrees[5].count == 2
