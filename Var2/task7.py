s = (
    {'X10', 1982, 'URWEB'},
    {'X10', 1982, 'APL'},
    {'X10', 1982, 'JAVA'},
    {'X10', 1958, 'URWEB'},
    {'X10', 1958, 'APL'},
    {'X10', 1958, 'JAVA'},
    {'X10', 2015},
    {'KICAD', 1982, 'URWEB'},
    {'KICAD', 1982, 'APL'},
    {'KICAD', 1982, 'JAVA'},
    {'KICAD', 1958},
    {'KICAD', 2015},
    {'SELF'}
)


def main(r):
    s1 = set(r)
    return [i for i in range(len(s)) if not (len(s[i] - s1))][0]


print(main(['JAVA', 2015, 'VHDL', 'KICAD']))
print(main(['URWEB', 2015, 'VHDL', 'SELF']))
print(main(['URWEB', 1982, 'NCL', 'X10']))
print(main(['APL', 1958, 'MIRAH', 'X10']))
print(main(['APL', 1982, 'MIRAH', 'KICAD']))
