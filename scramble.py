from random import randint


def scramble(moves: int=20):
    face = ['R', 'L', 'F', 'B', 'U', 'D']
    rot = ['', "'", '2']
    scramble = []
    # init loop var
    f = face[randint(0, len(face)-1)]

    for x in range(moves):
        fac = face.copy()
        fac.remove(f)
        f_i = randint(0, len(fac)-1) 
        r_i = randint(0, len(rot)-1)
        f = fac[f_i]
        r = rot[r_i]
        mov = f"{f}{r}" 
        scramble.append(mov)

    return " ".join(scramble)

