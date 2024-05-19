#! /bin/python
# Star Rail Clara's RES rate

class BOSS:
    def __init__(self, chance, hit):
        self.chance = chance
        self.hit = hit

class Character:
    def __init__(self, resist, extra_resist = 0):
        self.resist = resist
        self.extra_resist = extra_resist

    def hope(self, boss):
        print("当前被控概率: ",
              self.cal_hope(boss.chance, boss.hit, self.resist, self.extra_resist))

        # hopes
        print("效果抵抗 被控概率")
        res = list(map(lambda x: round(0.1*x, 1), range(11)))
        for x in res:
            print("{0}\t{1}".format(
                x,
                self.cal_hope(boss.chance, boss.hit, x, self.extra_resist))
            )

    def cal_hope(self, boss_chance, boss_hit, resist, extra_resist):
        # 被控概率 = BOSS基础概率 x (1-BOSS效果命中) x (1-角色效果抵抗) x (1-额外控制抵抗)
        return round(boss_chance * (1 - boss_hit) * (1 - resist) * (1 - extra_resist), 3)

def main():
    kafka = BOSS(1.2, 0.4)
    clara = Character(0.5, 0.3)
    clara.hope(kafka)


if __name__ == '__main__':
    main()