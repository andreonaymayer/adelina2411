def cria(x=rnd(), y=rnd(), z=rnd(), w=rnd(), cc=None, ft=None):
    return {'x': x,
            'y': y,
            'z': z,
            'w': w,
            'cromossomo': cc,
            'fitness': ft}

def cria(x=rnd(), y=rnd(), z=rnd(), w=rnd(), cc=None, ft=None):
    return [x, y, z, w, cc, ft]