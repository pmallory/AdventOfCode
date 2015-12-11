def reqd_paper(l,w,h):
    return 2*(l*w+w*h+h*l)+min(l,w,h)*sorted((l,w,h))[1]

def ribbon(l,w,h):
    dims = sorted((l,w,h))
    return 2*dims[0]+2*dims[1] + l*w*h

if __name__ == "__main__":
    total = 0
    ribbon_l = 0
    with open("input") as f:
        for line in f:
            l,w,h = line.split('x')
            l,w,h = int(l), int(w), int(h)
            total += reqd_paper(l,w,h)
            ribbon_l += ribbon(l,w,h)

    print(total)
    print(ribbon_l)
