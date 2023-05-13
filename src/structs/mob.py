import ctypes


class StructItemEffect(ctypes.Structure):
    _fields_ = [
        ("Effect", ctypes.c_ubyte),
        ("Value", ctypes.c_ubyte),
    ]


class StructItem(ctypes.Structure):
    _fields_ = [
        ("Id", ctypes.c_ushort),
        ("Effects", StructItemEffect * 3),
    ]


class NewStructScore(ctypes.Structure):
    _fields_ = [
        ("Level", ctypes.c_int),
        ("Ac", ctypes.c_int),
        ("Damage", ctypes.c_int),
        ("Merchant", ctypes.c_ubyte),
        ("AttackRun", ctypes.c_ubyte),
        ("Direction", ctypes.c_ubyte),
        ("ChaosRate", ctypes.c_ubyte),
        ("MaxHp", ctypes.c_int),
        ("MaxMp", ctypes.c_int),
        ("Hp", ctypes.c_int),
        ("Mp", ctypes.c_int),
        ("Str", ctypes.c_ushort),
        ("Int", ctypes.c_ushort),
        ("Dex", ctypes.c_ushort),
        ("Con", ctypes.c_ushort),
        ("Special", ctypes.c_ushort * 4)
    ]


class OldStructScore(ctypes.Structure):
    _fields_ = [
        ("Level", ctypes.c_int),
        ("Ac", ctypes.c_int),
        ("Damage", ctypes.c_int),
        ("Merchant", ctypes.c_ubyte),
        ("AttackRun", ctypes.c_ubyte),
        ("Direction", ctypes.c_ubyte),
        ("ChaosRate", ctypes.c_ubyte),
        ("MaxHp", ctypes.c_int),
        ("MaxMp", ctypes.c_int),
        ("Hp", ctypes.c_int),
        ("Mp", ctypes.c_int),
        ("Str", ctypes.c_ushort),
        ("Int", ctypes.c_ushort),
        ("Dex", ctypes.c_ushort),
        ("Con", ctypes.c_ushort),
        ("Special", ctypes.c_ushort * 4)
    ]


class OldStructMob(ctypes.Structure):
    _fields_ = [
        ("MobName", ctypes.c_char * 16),
        ("Clan", ctypes.c_char),
        ("Merchant", ctypes.c_ubyte),
        ("Guild", ctypes.c_ushort),
        ("Class", ctypes.c_ubyte),
        ("Rsv", ctypes.c_ushort),
        ("Quest", ctypes.c_ubyte),
        ("Coin", ctypes.c_int),
        ("Exp", ctypes.c_longlong),
        ("SPX", ctypes.c_short),
        ("SPY", ctypes.c_short),
        ("BaseScore", OldStructScore),
        ("CurrentScore", OldStructScore),
        ("Equip", StructItem * 16),
        ("Carry", StructItem * 64),
        ("LearnedSkill", ctypes.c_long),
        ("Magic", ctypes.c_uint),
        ("ScoreBonus", ctypes.c_ushort),
        ("SpecialBonus", ctypes.c_ushort),
        ("SkillBonus", ctypes.c_ushort),
        ("Critical", ctypes.c_ubyte),
        ("SaveMana", ctypes.c_ubyte),
        ("SkillBar", ctypes.c_ubyte * 4),
        ("GuildLevel", ctypes.c_ubyte),
        ("RegenHP", ctypes.c_ushort),
        ("RegenMP", ctypes.c_ushort),
        ("Resist", ctypes.c_ubyte * 4)
    ]


class NewStructMob(ctypes.Structure):
    _fields_ = [
        ("MobName", ctypes.c_char * 16),
        ("Clan", ctypes.c_char),
        ("Merchant", ctypes.c_ubyte),
        ("Guild", ctypes.c_ushort),
        ("Class", ctypes.c_ubyte),
        ("Rsv", ctypes.c_ushort),
        ("Quest", ctypes.c_ubyte),
        ("Coin", ctypes.c_int),
        ("Exp", ctypes.c_longlong),
        ("SPX", ctypes.c_short),
        ("SPY", ctypes.c_short),
        ("BaseScore", NewStructScore),
        ("CurrentScore", NewStructScore),
        ("Equip", StructItem * 20),
        ("Carry", StructItem * 64),
        ("LearnedSkill", ctypes.c_long),
        ("Magic", ctypes.c_uint),
        ("ScoreBonus", ctypes.c_ushort),
        ("SpecialBonus", ctypes.c_ushort),
        ("SkillBonus", ctypes.c_ushort),
        ("Critical", ctypes.c_ubyte),
        ("SaveMana", ctypes.c_ubyte),
        ("SkillBar", ctypes.c_ubyte * 4),
        ("GuildLevel", ctypes.c_ubyte),
        ("RegenHP", ctypes.c_ushort),
        ("RegenMP", ctypes.c_ushort),
        ("Resist", ctypes.c_ubyte * 4)
    ]
