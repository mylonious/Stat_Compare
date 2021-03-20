import math
import colorama

from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def elem(elem_in, stat_list, e_stat_f):
    resistance = []
    elem_list = ["f", "w", "g", "r", "e", "p", "i", "a", "d", "l", "a"]
    ind = 1
    index2 = 0

    stater = [
        [3, 0, 3, 2, 2, 2, 1, 3, 2, 2, 2],  # 275   E.ATK   1,2,0,1,4  | 8 | 19/ 22 = 41   - ATTACK/M.ATK     # FIRE -
        [3, 3, 0, 1, 0, 1, 2, 3, 2, 2, 2],  # 200           0,1,2,2,3  | 8 | 17/ 19 = 36   - DEFENCE/M.atk   w
        [0, 3, 3, 2, 2, 2, 0, 3, 2, 2, 2],  # 250          0,1,1,2,4  | 8 | 15/ 21 = 36   -                   g
        [3, 1, 1, 3, -1, 2, 2, 2, 2, 2, 2],  # 225          0,2,1,3,1  | 7 | 18/ 19 = 37   - DEFENCE          r
        [3, 3, 2, 0, 3, 1, 0, 2, 2, 2, 2],  # 225          1,0,1,4,2  | 9 | 18/ 20 = 38   - SPEED             e
        [0, 1, 3, 0, 2, 3, 1, 2, 2, 2, 2],  # 175          0,0,3,4,1  | 8 | 18/ 18 = 36   - ATTACK/SPEED      p
        [-1, 2, 3, 2, 3, 2, 2, 2, 2, 2],  # 250          0,2,2,3,1  | 8 | 18/ 19 = 37   - DEFENCE/M.def       i
        [2, 2, 2, 3, 2, 1, 3, 2, 2, 2],  # 275          0,0,0,5,3  | 8 | 13/ 21 = 34   - SPEED/DEFENCE
    ]
    rez_key = {
        -1: -50,
        0: -25,
        1: 0,
        2: 25,
        3: 50,
    }
    resistance_names = ["Fire",
                        "Water",
                        'Grass',
                        'Rock',
                        "Electric",
                        "Poison",
                        "Ice",
                        "Air",
                        "Dark",
                        "Light",
                        "Arcane",
                        ]

    elem1 = input()
    elem_out = []
    check_var = "x"

    boo, elem_out = in_list_3_letter(elem1, resistance_names)

    if elem_out == "FIRE":
        col = colorama.Fore.LIGHTRED_EX
        stat_list = stat_list[3, 5, 7, 8] + e_stat_f
        stat_list = stat_list[0, 4, 9, 10] - e_stat_f
        return stat_list

    elif elem_out == "WATER":
        col = colorama.Fore.LIGHTBLUE_EX
        stat_list = stat_list[0, 1, 4, 10] + e_stat_f
        stat_list = stat_list[3, 4, 7, 8] - e_stat_f
        return stat_list

    elif elem_out == "GRASS":
        col = colorama.Fore.GREEN

    elif elem_out == "ROCK":
        col = colorama.Fore.LIGHTBLACK_EX
        stat_list = stat_list[0, 4] + e_stat_f*2
        stat_list = stat_list[2, 5] - e_stat_f*2
        return stat_list
    elif elem_out == "ELECTRIC":
        col = colorama.Fore.LIGHTYELLOW_EX
        stat_list = stat_list[0, 1, 4, 10] + e_stat_f
        stat_list = stat_list[3, 4, 7, 8] - e_stat_f
        return stat_list
    elif elem_out == "POISON":
        col = colorama.Fore.MAGENTA

    elif elem_out == "ICE":
        col = colorama.Fore.LIGHTWHITE_EX

    elif elem_out == "AIR":
        col = colorama.Fore.WHITE

    elif elem_out == "DARK":
        col = colorama.Fore.BLACK

    elif elem_out == "LIGHT":
        col = colorama.Fore.LIGHTCYAN_EX

    elif elem_out == "ARCANE":
        col = colorama.Fore.LIGHTMAGENTA_EX


def in_list_3_letter(is_in, list_obj):
    br = False
    is_in = str.upper(is_in)

    for ind1 in list_obj:
        # print(ind1)
        check_against = str.upper(ind1)
        if is_in[0:2] == check_against[0:2]:
            br = True
            # print(check_against)
            return br, ind1

        # if br is False:
            # print(is_in + " no find")


# set priority exponent - In ( base, subtract_num ) [regular .8 .75 .7 .6 .5 .4 .3]
def typer_help(base, d_float):
    output = []

    list.append(output, base)
    for each in range(5):

        if each <= 1:
            base -= d_float / 2
            list.append(output, base)

        else:
            base -= d_float
            list.append(output, base)

    return output


# return stat weighting base on letter input
def typer(stat_base, expo, num, type1):
    check_var = "x"
    type_names = ["BAL",
                  "STR",  "STDEF", "STMAG", "STSKL",
                  "DEF", "DSTR", "DMAG", "DSKL",
                  "MAG", "MDEF", "MSKL", "MSTR",
                  "SKL", "SKDEF", "SKSTR", "SKMAG"]
    n = 0

    six_exp, five_exp, four_exp, \
        three_exp, two_exp, one_exp, = typer_help(stat_base, expo)

    six = round(num * six_exp, 2)
    five = round(num * five_exp, 2)
    four = round(num * four_exp, 2)
    three = round(num * three_exp, 2)
    two = round(num * two_exp, 2)
    one = round(num * one_exp, 2)
    six_b = round(num * six_exp, 2)
    five_b = round(num * five_exp, 2)
    four_b = round(num * four_exp, 2)
    three_b = round(num * three_exp, 2)
    two_b = round(num * two_exp, 2)
    one_b = round(num * one_exp, 2)

    stat_prio = [
        # H  MP SP| S  D  A  M |PA MA PD MD

        # BAL                                    @
        [three, three, three,
         three, three, three, three,
         two, two, three, two, "BAL"],

        # STR                                    @
        [three, two, three,
         six, three, three, one,
         four, two, two, one, "STR"],
        # STR/DEF                                @
        [four, two, three,
         five, four, two, one,
         three, two, two, two, "ST.D"],
        # STR/MAG                                @
        [three, four, two,
         five, two, one, four,
         three, three, two, one, "ST.M"],
        # STR/SKL                               @
        [three, two, four,
         five, two, four, one,
         three, three, two, one, "ST.S"],

        # DEF                                   @
        [five, two, two,
         three, six, one, two,
         two, one, three, three, "DEF"],
        # DEF/STR                               @
        [five, two, three,
         four, five, one, one,
         two, two, three, two, "D.ST"],
        # DEF/MAG                               @
        [five, four, two,
         one, four, one, four,
         one, two, three, three, "DE.M"],
        # DEF/SKL                              @
        [four, two, four,
         one, five, four, one,
         one, two, three, three, "D.SK"],

        # MAG                                   @
        [three, five, two,
         one, two, two, six,
         one, four, one, three, "MAG"],
        # MAG/DEF                               @
        [five, four, three,
         one, four, three, five,
         one, three, two, two, "MA.D"],
        # MAG/SKL                               @
        [three, five, four,
         one, one, three, four,
         three, three, one, two, "M.SK"],
        # MAG/STR                               @
        [three, four, two,
         four, two, one, five,
         two, four, one, two, "M.ST"],

        # SKL
        [three, two, four,
         one, two, six, three,
         two, three, two, two, "SKL"],
        # SKL/DEF                              @
        [four, two, four,
         one, four, five, one,
         one, two, two, three, "SK.D"],
        # SKL/ATK                             @
        [three, two, four,
         four, two, five, one,
         one, two, two, three, "SK.S"],
        # SKL/MAG
        [three, four, five,
         one, one, four, three,
         three, two, two, two, "SK.M"],


        [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],  # MAG
        [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],  # MAG

    ]

    for each in type_names:
        check_var = str.lower(each)
        n += 1
        if str.lower(type1[0:3]) == check_var[0:3]:
            # print("TRUE", type1[0:3], "type1", check_var[0:3], "list")
            return stat_prio[n - 1]
        # else:
            # print(type1[0:3], "type1", check_var[0:3], "list")




