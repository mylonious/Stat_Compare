import func
import colorama
import random
import math
from colorama import Fore, Back, Style
from tkinter import *
from openpyxl import Workbook
letter = "A"
offset = 2
first_bool = True

workbook = Workbook()
sheet = workbook.active
row = 1
column = "A"
location = column + str(row)

stat_data = open('stat.txt', 'r')

num, ex, x, stat_base, stat_spread = (stat_data.readlines()[0:5])

lines = (stat_data.readlines())


stat_data.close()
print(lines[:])
num = float(num)
ex = float(ex)
x = float(x)
stat_base = float(stat_base)
stat_spread = float(stat_spread)

print(num, ex, x, stat_base, stat_spread)


colorama.init(autoreset=True)


bump = " | "
Length = 40



#  #########         VISUAL ETC         ##########  ##




def fill(symbol, count):  # add x amount of "symbol"  ---- Next Print Comes in same line
    for n in range(count):
        print(symbol, end='')
        n += 1


def fill2(symbol, count):  # add x amount of "symbol" ----- Following Print Next Line
    for n in range(count):
        print(symbol, end='')
        n += 1
    print('')


def fill_nl(symbol, count):
    color = Back.LIGHTBLACK_EX + Fore.LIGHTBLACK_EX
    for n in range(count):
        print(symbol, end='')
        n += 1
    print('')


def setuper(leng):
    leng = leng
    fill_nl("-", leng * 12)
    fill("|", 1)
    fill(" ", 11)  # initial indent
    fill("|", 3)
    for i in range(leng):  # Level Line
        if i > 9:
            print(" ", i, " ", bump, end='')
            i += 1
        else:
            print("  ", i, " ", bump, end='')
            i += 1
    print('')
    fill("|", 1)
    fill(" ", 11)  # initial indent
    fill("|", 3)
    for i in range(leng):  # Level Line
        if i > 9:
            print("      ", bump, end='')
            i += 1
        else:
            print("      ", bump, end='')
            i += 1
    print('')
    fill_nl("-", leng * 12)




#  #########        TEXT WRAPPERS       ##########  ##




def resize(num, int_bool):
    col = Fore.BLUE
    if int_bool == 0:
        col = Fore.GREEN

    if num >= 1000:
        print(" ", col + str(math.floor(num)), bump, end="")
    elif num >= 100:
        print(" ", col + str(math.floor(num)), "", bump, end="")
    elif num >= 10:
        print(" ", col + str(math.floor(num)), " ", bump, end="")
    else:
        print(" ", col + str(math.floor(num)), "  ", bump, end="")


def resizep(num, num2):
    num = math.floor(num)
    num2 = math.floor(num2)
    if num - num2 >= 1000:
        print("+", round(num - num2), bump, end="")
    elif num - num2 >= 100:
        print("+", round(num - num2), "", bump, end="")
    elif num - num2 >= 10:
        print(" +", round(num - num2), "", bump, end="")
    else:
        print("  +", round(num - num2), "", bump, end="")


def resizepl(num, num2):
    if num >= 1000:
        print("+", "0", bump, end="")
    elif num >= 100:
        print("+", "0", "", bump, end="")
    elif num >= 10:
        print("+", "0", "  ", bump, end="")
    else:
        print("  + 0", "", bump, end="")


def resizel(num):
    if num >= 1000:
        print(" ", "-", "  ", bump, end="")
    elif num >= 100:
        print(" ", "-", "  ", bump, end="")
    elif num >= 10:
        print(" ", "-", "  ", bump, end="")
    else:
        print(" ", "-   ", bump, end="")


def resizename(name, int_bool):
    col = Fore.BLUE
    if int_bool == 0:
        col = Fore.GREEN

    print(" ", col + str(name), bump, end="")


def stat_calc(name, ding, length, current, expo):
    compare = current
    greater_than = True
    add_stat = ding
    ret = 0
    watcher = 1
    w = True

    print("|", name, " ", end='')  # setup
    for n in range(length):
        if n == 0:  # if 0 print 0
            if current > 9:
                print("{:2.2f}".format(expo), "|||", end='')
                n += 1
            else:
                print("{:2.2f}".format(expo), "|||", end='')
                n += 1
        elif n == 1:
            ret = math.floor(current)

        elif greater_than is True:
            compare = math.floor(current)

        current += ding  # add stat xp
        if current >= (compare + 1):  # check if xp has hit 1.0
            current = current + add_stat  # add stat amount
            add_stat = add_stat + add_stat * expo  # Y + ( x * X/4)
            resize(current, 1)  # print stat
            greater_than = True
            n += 1

        else:
            if n == watcher:
                greater_than = False
                if w is True:

                    resize(current, 0)
                    watcher = 20
                    w = False
                    n += 1

                else:
                    resize(current, 0)
                    watcher += 10
                    n += 1

            else:
                resizel(current)
                greater_than = False
                n += 1

    print(''),
    return ret


def stat_calc_n_print(ding, length, current, expo, watcher):
    compare = current
    greater_than = True
    add_stat = ding
    ret = 0
    w = True

    for n in range(length):
        if greater_than is True:
            compare = math.floor(current)

        current += ding  # add stat xp
        if current >= (compare + 1):  # check if xp has hit 1.0
            current = current + add_stat  # add stat amount
            add_stat = add_stat + add_stat * expo  # Y + ( x * X/4)
            greater_than = True
            if n == watcher:
                ret = current
            n += 1

        else:
            if n == watcher:
                greater_than = False
                ret = math.floor(current)
                n += 1

            elif n == 10:
                greater_than = False
                ret = math.floor(current)
                n += 1

            else:
                greater_than = False
                n += 1

    return ret


def stat_calc_add(name, ding, length, current, expo):
    compare = current
    greater_than = True
    add_stat = ding
    stat_list = []

    print("| ", "    ", end='')  # "STR      "
    for n in range(length):
        if n == 0:  # if 0 print 0
            print("{:.2f}".format(ding), "|||", end='')
            n += 1
        else:
            if greater_than is True:
                compare = math.floor(current)

        current += ding
        if current >= (compare + 1):
            current = current + add_stat
            add_stat = add_stat + add_stat * expo
            resizep(current, compare)
            greater_than = True
            n += 1

        else:
            resizel(current)
            greater_than = False
            n += 1

    print(''),


def stat_disp(name, priority, count, base, exp):
    stat = stat_calc(name, priority, count, base, exp)
    stat_calc_add(name, priority, count, base, exp)
    fill_nl("-", count * 12)
    return stat


def v(x):
    x = x * 2 * 4
    return x


def vr(x):
    x = x * 4 * 14
    return x


def creature_creator():

    print(Fore.GREEN + " NAME: ")
    name = str(input())
    print(Fore.CYAN + " ELEM: ")
    elem = str(input())
    print(Fore.LIGHTRED_EX + " TYPE: ")
    typee = str(input())
    print("Level to: ", end=''),
    level_count = input()
    print("Level weighting: ", end=''),
    med = float(input())
    print("HP/MP/SP growth rate/exponent: ", end=''),
    hxo = float(input())
    print("STR/DEF/MAG/AGI growth rate/exponent: ", end=''),
    xo = float(input())
    print("[STATS] priority base (.4 - 2.0) ", end=''),
    xob = float(input())
    print("[STATS] priority spread exponent [subtract] (0.01 - 0.1) ", end=''),
    xobe = float(input())
    make_graph(name, elem, typee, med, int(level_count), hxo, xo, xob, xobe)


def make_graph(name, elem, type1, length, level_record):
    global num
    global ex
    global x
    global stat_base
    global stat_spread

    leng = length * 13
    length = length + 1

#
#
#

    h_pr, m_pr, s_pr, st_pr, de_pr, ag_pr, ma_pr, at_pr, mt_pr, pd_pr, md_pr, type_out = \
        func.typer(stat_base, stat_spread, num, type1)

    # stat_expo_holder = [h_pr, m_pr, s_pr, st_pr, de_pr, ag_pr, ma_pr, at_pr, mt_pr, pd_pr, md_pr]

    # h_pr, m_pr, s_pr, st_pr, de_pr, ag_pr, ma_pr, at_pr, mt_pr, pd_pr, md_pr, elem_out = \
    #    func.elem(elem, stat_expo_holder, .21)

    h_b, m_b, s_b, st_b, de_b, ag_b, ma_b, pat_b, mat_b, pde_b, mde_b\
        = vr(h_pr), vr(m_pr), vr(s_pr), v(st_pr), v(de_pr), v(ag_pr), v(ma_pr), v(at_pr), v(mt_pr), v(pd_pr), v(md_pr)

#
#
#

    # assign stat priority
    fill_nl("+", leng)
    fill_nl("+", leng)
    fill_nl("-", leng)
    print(name + bump, "   ", type_out)
    print('')
    fill_nl("-", leng)
    print(elem + bump)

#
#
#

    setuper(length)

    stat_disp("HP ", h_pr, length, h_b, ex)
    hp = stat_calc_n_print(h_pr, length, h_b, ex, level_record)

    stat_disp("MP ", m_pr, length, m_b, ex)
    mp = stat_calc_n_print(m_pr, length, m_b, ex, level_record)

    stat_disp("SP ", s_pr, length, s_b, ex)
    sp = stat_calc_n_print(s_pr, length, s_b, ex, level_record)

    fill_nl("-", leng)

    stat_disp("STR", st_pr, length, st_b, x)
    stre = stat_calc_n_print(st_pr, length, st_b, x, level_record)

    stat_disp("DEF", de_pr, length, de_b, x)
    de = stat_calc_n_print(de_pr, length, de_b, x, level_record)

    stat_disp("AGI", ag_pr, length, ag_b, x)
    agi = stat_calc_n_print(ag_pr, length, ag_b, x, level_record)

    stat_disp("MAG", ma_pr, length, ma_b, x)
    mag = stat_calc_n_print(ma_pr, length, ma_b, x, level_record)

    fill_nl("-", leng)

    stat_disp("ATK", at_pr, length, pat_b, x),
    patk = stat_calc_n_print(at_pr, length, pat_b, x, level_record)

    stat_disp("MTK", mt_pr, length, mat_b, x),
    matk = stat_calc_n_print(mt_pr, length, mat_b, x, level_record)

    stat_disp("PEF", pd_pr, length, pde_b, x),
    pef = stat_calc_n_print(pd_pr, length, pde_b, x, level_record)

    stat_disp("MEF", md_pr, length, mde_b, x)
    mef = stat_calc_n_print(md_pr, length, mde_b, x, level_record)

    fill_nl("-", leng)
    fill_nl(" ", leng)
    xp = stat_disp("XP", 34, length, 34, x)
    character_sheet = [hp, mp, sp, stre, de, agi, mag, patk, matk, pef, mef, name, type_out]
    return character_sheet


def stat_calc_xlsx(name, ding, length, current, expo):
    compare = current
    greater_than = True
    add_stat = ding
    ret = 0
    n = 1
    global sheet
    global letter

    loc = letter + str(n + offset)
    print(loc)
    sheet[str(loc)] = current
    for n in range(length):
        print(n)
        print(loc)

        if greater_than is True:
            compare = math.floor(current)

        current += ding  # add stat xp
        loc = letter + str(n + offset)
        if current >= (compare + 1):  # check if xp has hit 1.0
            current = current + add_stat  # add stat amount

            sheet[str(loc)] = math.floor(current)
            add_stat = add_stat + add_stat * expo  # Y + ( x * X/4)
            greater_than = True
            n += 1

        else:
            sheet[str(loc)] = math.floor(current)
            greater_than = False
            n += 1


def make_stat_chain(name, elem, type1, length):
    global num
    global ex
    global x
    global stat_base
    global stat_spread
    global sheet
    global letter
    global offset
    global first_bool

    if first_bool is False:
        offset += length + 1
    else:
        first_bool = False

    sheet["A" + str(offset)] = name

    for each in range(length):
        row_a = "A" + str(each + offset + 1)
        row_b = "B" + str(each + offset)
        sheet[row_a] = name + str(each+2)
        sheet[row_b] = str(each + 1)

#
#
#

    h_pr, m_pr, s_pr, st_pr, de_pr, ag_pr, ma_pr, at_pr, mt_pr, pd_pr, md_pr, type_out = \
        func.typer(stat_base, stat_spread, num, type1)

    # stat_expo_holder = [h_pr, m_pr, s_pr, st_pr, de_pr, ag_pr, ma_pr, at_pr, mt_pr, pd_pr, md_pr]

    # h_pr, m_pr, s_pr, st_pr, de_pr, ag_pr, ma_pr, at_pr, mt_pr, pd_pr, md_pr, elem_out = \
    #    func.elem(elem, stat_expo_holder, .21)

    h_b, m_b, s_b, st_b, de_b, ag_b, ma_b, pat_b, mat_b, pde_b, mde_b\
        = vr(h_pr), vr(m_pr), vr(s_pr), v(st_pr), v(de_pr), v(ag_pr), v(ma_pr), v(at_pr), v(mt_pr), v(pd_pr), v(md_pr)

    letter = "C"
    stat_calc_xlsx("HP ", h_pr, length, h_b, ex)

    letter = "D"
    stat_calc_xlsx("MP ", m_pr, length, m_b, ex)

    letter = "E"
    stat_calc_xlsx("SP ", s_pr, length, s_b, ex)

    letter = "F"
    stat_calc_xlsx("STR", st_pr, length, st_b, x)

    letter = "G"
    stat_calc_xlsx("DEF", de_pr, length, de_b, x)

    letter = "H"
    stat_calc_xlsx("AGI", ag_pr, length, ag_b, x)

    letter = "I"
    stat_calc_xlsx("MAG", ma_pr, length, ma_b, x)

    letter = "J"
    stat_calc_xlsx("ATK", at_pr, length, pat_b, x)

    letter = "K"
    stat_calc_xlsx("MTK", mt_pr, length, mat_b, x)

    letter = "L"
    stat_calc_xlsx("PEF", pd_pr, length, pde_b, x)

    letter = "M"
    stat_calc_xlsx("MEF", md_pr, length, mde_b, x)

    workbook.save(filename="test_sheet.xlsx")


def creature_choice(self, opponent, st_exp, e_hp):
    a, b, c = [0, 1, 2], [3, 4, 5], [6, 7, 8]
    finished = False
    random_check_finished = False
    choice = 0
    if self[3] > self[5] and self[6]:
        a, b, c = [0, 1, 2, 3, 4, 5], [6], [7, 8]

    elif self[5] > self[3] and self[6]:
        a, b, c = [0, 1], [2, 3], [4, 5, 6, 7, 8]

    elif self[6] > self[3] and self[5]:
        a, b, c = [0, 1], [2, 3, 4, 5, 6, ], [7, 8]

    while finished is False:
        choice = random.randint(0, 8)
        for d in a:
            if choice == a[d]:
                choice = 0
                finished = True
                break
        if finished is True:
            break

        for e in b:

            if choice == b[(e - len(a))]:
                choice = 1
                finished = True
                break
        if finished is True:
            break

        for f in c:
            if choice == c[(f - len(a) - len(b))]:
                choice = 2
                finished = True
                break

    if choice == 0:
        finished = True
        return attack(self, opponent, st_exp, e_hp)

    elif choice == 1:
        finished = True
        return magic(self, opponent, st_exp, e_hp)

    elif choice == 2:
        finished = True
        return skill(self, opponent, st_exp, e_hp)


def fight_simu(c1, c2, st_exp):
    turn_count = 0
    c1_first = True
    c1hp = c1[0]
    c2hp = c2[0]
    if c2[3] > c1[3]:
        c1_first = False
    fill_nl("-", 30)
    fill_nl("- ", 15)
    print("|", "        STAT//SIM)        ", "|")
    fill_nl("- ", 15)
    fill_nl("-", 30)

    print(colorama.Fore.LIGHTMAGENTA_EX + c1[11], "    vs    ", c2[11])
    fill_nl("-", 30)
    print(colorama.Fore.LIGHTRED_EX + c1[12], "    -------   ", colorama.Fore.LIGHTRED_EX + c2[12])

    for each in range(11):
        if c1[each] > 9:
            print("{:2.2f}".format(c1[each]), "   -------   ", "{:2.2f}".format(c2[each]))

        else:
            print("0""{:2.2f}".format(c1[each]), "   -------   ", "{:2.2f}".format(c2[each]))
    print(int((c1[0] / 10 / 4) + (c1[1] / 10 / 4) + (c1[2] / 10 / 4) + c1[3] + c1[4] + c1[5] + c1[6] + c1[7] + c1[8] +
              c1[9] + c1[10]),
          "                ",
          (int((c2[0] / 10 / 4) + (c2[1] / 10 / 4) + (c2[2] / 10 / 4) + c2[3] + c2[4] + c2[5] + c2[6] + c2[7] + c2[8] +
               c2[9] + c2[10])))
    while c1hp > 0 and c2hp > 0:
        fill_nl("- ", 15)
        print(colorama.Fore.GREEN + "TURN       ", end="")
        print(colorama.Fore.GREEN + str(turn_count), end='')
        if c1_first is True:
            print(colorama.Fore.WHITE + "  -  ", c1[11])
        else:
            print(colorama.Fore.WHITE + "  -  ", c2[11])
        fill_nl("- ", 15)
        print(int(c1hp), " / ", int(c1[0]), "     ", c1[11])
        print(int(c2hp), " / ", int(c2[0]), "     ", c2[11])
        fill_nl("- ", 15)
        turn_count += 1
        if c1_first is True:
            c2hp = creature_choice(c1, c2, st_exp, c2hp)
            c1_first = False

        else:
            c1hp = creature_choice(c2, c1, st_exp, c1hp)
            c1_first = True

    print(colorama.Fore.GREEN + c1[11] + " wins")


def attack(attacker, defender, atk_to_str_f, e_hp):
    e_hp = int(e_hp)
    defense, p_defense = int(defender[4]), int(defender[9])
    a_strength, a_attack = int(attacker[3]), int(attacker[7])
    print(attacker[11], "uses attack")
    print("")
    damage = a_attack + (a_strength / 2)
    print("( ", a_attack, " atk ) + ( ", a_strength / 2, " str) = (", damage, " )")

    damage = damage - ((defense / 4) + (p_defense / 2))
    print("( ", defense / 4, " def ) + ( ", p_defense / 2, " pdef) = (", damage, " )")

    print("hit", defender[11], "    -", int(damage), "Health",)
    e_hp = e_hp - int(damage)

    print("HP = ", e_hp)
    return e_hp


def magic(attacker, defender, atk_to_str_f, e_hp):
    e_hp = int(e_hp)
    health, healthmax = int(defender[0]), int(defender[0])
    a_mag, a_mag_atk = int(attacker[6]), int(attacker[8])
    damage = a_mag_atk + (a_mag / 2)
    print(attacker[11], "uses magic")
    print("hit", defender[11], "    -", int(damage), "Health",)
    health = e_hp - int(damage)

    print("HP = ", health)
    return health


def skill(attacker, defender, atk_to_str_f, e_hp):
    e_hp = int(e_hp)
    defense, p_defense = defender[4], defender[8]
    a_strength, a_attack, a_skill = int(attacker[3]), int(attacker[7]), int(attacker[5])

    damage = (a_attack / 2) + ((a_strength / 4) + (a_skill / 2))
    print(damage, a_attack, " ", a_strength, " ", a_skill)

    print(attacker[11], "uses skill")

    damage = damage - (p_defense / 2)
    print(damage, "D - (d/2)")

    print("hit", defender[11], "    -", int(damage), "Health",)
    e_hp = e_hp - int(damage)

    print("HP = ", e_hp)
    return e_hp


def save_settings():
    global num
    global ex
    global x
    global stat_base
    global stat_spread

    cool_list = num, ex, x, stat_base, stat_spread
    stat_data_loc = open('stat.txt', 'w')
    stat_data_loc.writelines([str(num), "\n", str(ex), "\n", str(x), "\n", str(stat_base), "\n", str(stat_spread)])
    stat_data_loc.close()


def settingss():
    global num
    global ex
    global x
    global stat_base
    global stat_spread

    print(colorama.Fore.LIGHTGREEN_EX + "SET GROWTH RATE (CURRENT = ", end='')
    print(colorama.Fore.LIGHTGREEN_EX + str(num), end='')
    print(colorama.Fore.LIGHTGREEN_EX + ")")
    num = float(input())
    print(colorama.Fore.LIGHTGREEN_EX + "SET HP/MP/SP G.RATE (CURRENT = ", end='')
    print(colorama.Fore.LIGHTGREEN_EX + str(ex), end='')
    print(colorama.Fore.LIGHTGREEN_EX + ")")
    ex = float(input())
    print(colorama.Fore.LIGHTGREEN_EX + "SET S/D/A/M G.RATE (CURRENT = ", end='')
    print(colorama.Fore.LIGHTGREEN_EX + str(x), end='')
    print(colorama.Fore.LIGHTGREEN_EX + ")")
    x = float(input())
    print(colorama.Fore.LIGHTGREEN_EX + "SET STAT BASE - [base - stat spread(n.times)] (CURRENT = ", end='')
    print(colorama.Fore.LIGHTGREEN_EX + str(stat_base), end='')
    print(colorama.Fore.LIGHTGREEN_EX + ")")
    stat_base = float(input())
    print(colorama.Fore.LIGHTGREEN_EX + "SET STAT SPREAD (CURRENT = ", end='')
    print(colorama.Fore.LIGHTGREEN_EX + str(ex), end='')
    print(colorama.Fore.LIGHTGREEN_EX + ")")
    stat_spread = float(input())

    save = str(input())

    if str.lower(save) == "y":
        save_settings()

    else:
        select_dad(main_menu)


def auto():
    c1 = make_graph("NPC1", "GRASS  ", "bal", 20, 20)
    c2 = make_graph("NPC2   ", "GRASS  ", "std", 20, 20)
    c3 = make_graph("NPC3   ", "ROCK   ", "skl", 20, 20)
    c4 = make_graph("NPC4  ", "POISON ", "mde", 20, 20)
    c5 = make_graph("NPC5    ", "POISON ", "mag", 20, 20)
    c6 = make_graph("NPC6    ", "ROCK   ", "def", 20, 20)
    fight_simu(c1, c2, .5)
    fight_simu(c3, c4, .5)
    fight_simu(c5, c6, .5)

# def sim_manager():


def csv():
    sheet["B1"] = "LVL"
    sheet["C1"] = "HP"
    sheet["D1"] = "MP"
    sheet["E1"] = "SP"
    sheet["F1"] = "STR"
    sheet["G1"] = "DEF"
    sheet["H1"] = "AGI"
    sheet["I1"] = "MAG"
    sheet["J1"] = "PATK"
    sheet["K1"] = "MATK"
    sheet["L1"] = "PDEF"
    sheet["M1"] = "MEF"


def select_dad(dictio):
    boo = False
    q_disp(dictio)
    inp = input()

    while boo is False:
        boo, out = func.in_list_3_letter(inp, dictio)
    if boo is True:
        dictio[out]()


def q_disp(op_list):

    for each in op_list:
        print(colorama.Fore.LIGHTBLUE_EX + "| ", end='')
        print(colorama.Fore.LIGHTBLUE_EX + each, "", end='')
    print(colorama.Fore.LIGHTBLUE_EX + "|")


main_menu = {
        "CREATE CREATURE": creature_creator,
        "SIMULATE": auto,
        "MAKE.GRAPH": auto,
        "SETTINGS": settingss,
        "CSV": csv
    }
settings = {
        "TWEAK": auto,
        "SAVE": save_settings
    }
a = True
while a is True:
    select_dad(main_menu)
