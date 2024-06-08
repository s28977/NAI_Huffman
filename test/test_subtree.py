from src.model.subtree import Subtree, join
from src.model.symbol import Symbol


def test_correct_total_order():
    node1 = Subtree(Symbol('z', 1, 3))
    node2 = Subtree(Symbol('p', 2, 3))
    node3 = Subtree(Symbol('c', 3, 7))
    assert node1 != node2
    assert node1 < node2
    assert node1 <= node2
    assert node1 != node3
    assert node1 < node3
    assert node1 <= node3
    assert node2 != node3
    assert node2 < node3
    assert node2 <= node3


def test_correct_join():
    z = Subtree(Symbol('z', 1, 3))
    p = Subtree(Symbol('p', 2, 3))
    s = Subtree(Symbol('s', 3, 5))
    t = Subtree(Symbol('t', 4, 3))
    o = Subtree(Symbol('o', 5, 1))
    o_z = join(o, z)
    assert o_z.count == 4
    assert o_z.symbol.char == 'z'
    assert o_z.symbol.order == 1
    assert o_z.left == o
    assert o_z.right == z
    p_t = join(p, t)
    assert p_t.count == 6
    assert p_t.symbol.char == 'p'
    assert p_t.symbol.order == 2
    assert p_t.left == p
    assert p_t.right == t
    o_z_s = join(o_z, s)
    assert o_z_s.count == 9
    assert o_z_s.symbol.char == 'z'
    assert o_z_s.symbol.order == 1
    assert o_z_s.left == o_z
    assert o_z_s.right == s
    p_t_o_z_s = join(p_t, o_z_s)
    assert p_t_o_z_s.count == 15
    assert p_t_o_z_s.symbol.char == 'z'
    assert p_t_o_z_s.symbol.order == 1
    assert p_t_o_z_s.left == p_t
    assert p_t_o_z_s.right == o_z_s


def test_correct_get_huffman_code():
    z = Subtree(Symbol('z', 1, 3))
    p = Subtree(Symbol('p', 2, 3))
    s = Subtree(Symbol('s', 3, 5))
    t = Subtree(Symbol('t', 4, 3))
    o = Subtree(Symbol('o', 5, 1))
    o_z = join(o, z)
    p_t = join(p, t)
    o_z_s = join(o_z, s)
    p_t_o_z_s = join(p_t, o_z_s)
    code_dict = {}
    p_t_o_z_s.get_huffman_code(code_dict)
    assert code_dict == dict(p='00', t='01', o='100', z='101', s='11')
