import os
import io
import structs.mob

if __name__ == '__main__':
    old_mob_directory = os.path.join(os.getcwd(), 'data', 'old', 'npc')
    new_mob_directory = os.path.join(os.getcwd(), 'data', 'new', 'npc')
    old_mob_files = os.listdir(old_mob_directory)
    old_mob_files = [os.path.join(old_mob_directory, file)
                     for file in old_mob_files]
    for old_file in old_mob_files:
        old_mob_file = open(old_file, 'rb')
        old_mob_struct = structs.mob.OldStructMob()
        io.BytesIO(old_mob_file.read()).readinto(old_mob_struct)
        old_mob_file.close()

        new_mob_struct = structs.mob.NewStructMob()

        new_mob_struct.MobName = old_mob_struct.MobName
        new_mob_struct.Clan = old_mob_struct.Clan
        new_mob_struct.Merchant = old_mob_struct.Merchant
        new_mob_struct.Guild = old_mob_struct.Guild
        new_mob_struct.Class = old_mob_struct.Class
        new_mob_struct.Rsv = old_mob_struct.Rsv
        new_mob_struct.Quest = old_mob_struct.Quest
        new_mob_struct.Coin = old_mob_struct.Coin
        new_mob_struct.Exp = old_mob_struct.Exp
        new_mob_struct.SPX = old_mob_struct.SPX
        new_mob_struct.SPY = old_mob_struct.SPY

        new_mob_struct.BaseScore.Level = old_mob_struct.BaseScore.Level
        new_mob_struct.BaseScore.Ac = old_mob_struct.BaseScore.Ac
        new_mob_struct.BaseScore.Damage = old_mob_struct.BaseScore.Damage
        new_mob_struct.BaseScore.Merchant = old_mob_struct.BaseScore.Merchant
        new_mob_struct.BaseScore.AttackRun = old_mob_struct.BaseScore.AttackRun
        new_mob_struct.BaseScore.Direction = old_mob_struct.BaseScore.Direction
        new_mob_struct.BaseScore.ChaosRate = old_mob_struct.BaseScore.ChaosRate
        new_mob_struct.BaseScore.MaxHp = old_mob_struct.BaseScore.MaxHp
        new_mob_struct.BaseScore.MaxMp = old_mob_struct.BaseScore.MaxMp
        new_mob_struct.BaseScore.Hp = old_mob_struct.BaseScore.Hp
        new_mob_struct.BaseScore.Mp = old_mob_struct.BaseScore.Mp
        new_mob_struct.BaseScore.Str = old_mob_struct.BaseScore.Str
        new_mob_struct.BaseScore.Int = old_mob_struct.BaseScore.Int
        new_mob_struct.BaseScore.Dex = old_mob_struct.BaseScore.Dex
        new_mob_struct.BaseScore.Con = old_mob_struct.BaseScore.Con
        new_mob_struct.BaseScore.Special = old_mob_struct.BaseScore.Special

        new_mob_struct.CurrentScore.Level = old_mob_struct.CurrentScore.Level
        new_mob_struct.CurrentScore.Ac = old_mob_struct.CurrentScore.Ac
        new_mob_struct.CurrentScore.Damage = old_mob_struct.CurrentScore.Damage
        new_mob_struct.CurrentScore.Merchant = old_mob_struct.CurrentScore.Merchant
        new_mob_struct.CurrentScore.AttackRun = old_mob_struct.CurrentScore.AttackRun
        new_mob_struct.CurrentScore.Direction = old_mob_struct.CurrentScore.Direction
        new_mob_struct.CurrentScore.ChaosRate = old_mob_struct.CurrentScore.ChaosRate
        new_mob_struct.CurrentScore.MaxHp = old_mob_struct.CurrentScore.MaxHp
        new_mob_struct.CurrentScore.MaxMp = old_mob_struct.CurrentScore.MaxMp
        new_mob_struct.CurrentScore.Hp = old_mob_struct.CurrentScore.Hp
        new_mob_struct.CurrentScore.Mp = old_mob_struct.CurrentScore.Mp
        new_mob_struct.CurrentScore.Str = old_mob_struct.CurrentScore.Str
        new_mob_struct.CurrentScore.Int = old_mob_struct.CurrentScore.Int
        new_mob_struct.CurrentScore.Dex = old_mob_struct.CurrentScore.Dex
        new_mob_struct.CurrentScore.Con = old_mob_struct.CurrentScore.Con
        new_mob_struct.CurrentScore.Special = old_mob_struct.CurrentScore.Special

        item_id = 0
        for old_equip_item in old_mob_struct.Equip:
            new_mob_struct.Equip[item_id].Id = old_equip_item.Id
            new_mob_struct.Equip[item_id].Effects[0].Effect = old_equip_item.Effects[0].Effect
            new_mob_struct.Equip[item_id].Effects[0].Value = old_equip_item.Effects[0].Value
            new_mob_struct.Equip[item_id].Effects[1].Effect = old_equip_item.Effects[1].Effect
            new_mob_struct.Equip[item_id].Effects[1].Value = old_equip_item.Effects[1].Value
            new_mob_struct.Equip[item_id].Effects[2].Effect = old_equip_item.Effects[2].Effect
            new_mob_struct.Equip[item_id].Effects[2].Value = old_equip_item.Effects[2].Value
            item_id += 1

        item_id = 0
        for old_carry_item in old_mob_struct.Carry:
            new_mob_struct.Carry[item_id].Id = old_carry_item.Id
            new_mob_struct.Carry[item_id].Effects[0].Effect = old_carry_item.Effects[0].Effect
            new_mob_struct.Carry[item_id].Effects[0].Value = old_carry_item.Effects[0].Value
            new_mob_struct.Carry[item_id].Effects[1].Effect = old_carry_item.Effects[1].Effect
            new_mob_struct.Carry[item_id].Effects[1].Value = old_carry_item.Effects[1].Value
            new_mob_struct.Carry[item_id].Effects[2].Effect = old_carry_item.Effects[2].Effect
            new_mob_struct.Carry[item_id].Effects[2].Value = old_carry_item.Effects[2].Value
            item_id += 1

        new_mob_struct.LearnedSkill = old_mob_struct.LearnedSkill
        new_mob_struct.Magic = old_mob_struct.Magic
        new_mob_struct.ScoreBonus = old_mob_struct.ScoreBonus
        new_mob_struct.SpecialBonus = old_mob_struct.SpecialBonus
        new_mob_struct.SkillBonus = old_mob_struct.SkillBonus
        new_mob_struct.Critical = old_mob_struct.Critical
        new_mob_struct.SaveMana = old_mob_struct.SaveMana
        new_mob_struct.SkillBar[0] = old_mob_struct.SkillBar[0]
        new_mob_struct.SkillBar[1] = old_mob_struct.SkillBar[1]
        new_mob_struct.SkillBar[2] = old_mob_struct.SkillBar[2]
        new_mob_struct.SkillBar[3] = old_mob_struct.SkillBar[3]
        new_mob_struct.GuildLevel = old_mob_struct.GuildLevel
        new_mob_struct.RegenHP = old_mob_struct.RegenHP
        new_mob_struct.RegenMP = old_mob_struct.RegenMP
        new_mob_struct.Resist[0] = old_mob_struct.Resist[0]
        new_mob_struct.Resist[1] = old_mob_struct.Resist[1]
        new_mob_struct.Resist[2] = old_mob_struct.Resist[2]
        new_mob_struct.Resist[3] = old_mob_struct.Resist[3]

        new_mob_file = old_file.replace(old_mob_directory, new_mob_directory)
        new_mob_buffer = io.BytesIO(new_mob_struct).getbuffer().tobytes()
        new_mob_file = open(new_mob_file, "wb")
        new_mob_file.write(new_mob_buffer)
        new_mob_file.close()
