import requests
import pandas as pd
import json

import traditional_chinese


def load_TFTdata_from_github(URL_TFT_DATA):
    print(f"Requesting data from TFT Github")
    req = requests.get(URL_TFT_DATA, verify=False)
    data = req.json()
    print(f"Compass Data from TFT Github saved \n")
    data_dir = {}
    for each in data["data"]:
        data_dir[each["name"]] = each["chaos"]

    return data_dir


def load_NINJAdata_from_github():
    print(f"Requesting currency from NINJAdata Github")
    req = requests.get(URL_NINJA_DATA).text
    data = json.loads(req)
    print(f"Currency Data from NINJAdata Github saved \n")

    return data


def Global_compass_data_alias(compass_price_dir, compass_english2chinese):
    price_compass_dir_alias = {compass_english2chinese[key]: compass_price_dir[key] for key in compass_english2chinese}
    return price_compass_dir_alias


compass_english2chinese = {"Yellow Plants": "地图内的庄园至少有一片黄庄稼",
                           "Mirror of Delirium": "地图中有一个惊悸迷雾之镜",
                           "Beyond": "你的地图中的超越恶魔群规模提高",
                           "Blue Plants": "至少有一片蓝庄稼",
                           "Purple Plants": "至少有一片紫庄稼",
                           "Sacred Grove": "你的地图包含古灵庄园",
                           "8 Modifiers": "地图内发现的地图被 8 个词缀腐化",
                           "Conqueror Map": "额外掉落一个征服者地图",
                           "Abyss": "该地图会出现 1 个额外深渊",
                           "Shaper Guardian": "额外掉落一个塑界守卫地图",
                           "Alva": "该地图会出现【阿尔瓦】",
                           "Copy of Beasts": "复制一头地图中被捕捉的魔物",
                           "Chayula": "地图内裂隙属于夏乌拉",
                           "Strongbox Enraged": "保险箱里的怪物已暴怒",
                           "Delirium Reward": "惊悸迷雾奖励条进度加快 100%",
                           "Elder Guardian": "额外掉落一个裂界守卫地图",
                           "Legion": "该地图会额外出现 1 个战乱之殇事件",
                           "Magic Pack Size": "魔法怪物群大小提高 25%",
                           "Mysterious Harbinger": "地图首领由 1 个神秘先驱者守护",
                           "Oils Tier": "你的地图中发现的圣油高一阶",
                           "Splinters Emblems Duplicate": "地图内的战乱之殇怪物掉落的印记和裂片会复制",
                           "Uul-Netol": "地图内裂隙属于乌尔尼多",
                           "Contracts Implicit": "夺宝奇兵契约额外有一个基底词缀",
                           "Gloom Shrine": "隐忍神龛",
                           "Jun": "该地图会出现【琼】",
                           "Map 20% Quality": "你的地图的品质为20%",
                           "Runic Monster Markers": "符纹怪物之印的数量提高 100%",
                           "Syndicate Intelligence": "不朽辛迪加目标处获得的情报提高100%",
                           "Unidentified Map": "你的未鉴定的地图中的怪物群规模提高20%",
                           "Alluring": "这些地图吸引鱼",
                           "Breach": "该地图会额外出现 1 个裂隙",
                           "Gilded Scarab": "前 3 个被附身的怪物会掉落 1 个额外的镀金圣甲虫",
                           "Ritual Altars": "地图内有驱灵祭坛",
                           "Strongbox Corrupted": "该地图内的保险箱已被腐化",
                           "Bodyguards": "地图首领由守卫守护完成该地图时会额外掉落 1 张地图",
                           "Smuggler's Cache": "区域内有一个走私者秘藏 ",
                           "Soul Gain Prevention": "玩家的瓦尔技能无法用于【阻灵术】",
                           "Lightning Monsters": "闪电属性怪物",
                           "Blight": "菌潮遭遇战",
                           "Boss Drop Unique": "地图首领额外掉落一件传奇物品",
                           "Chaos Monsters": "混沌属性怪物",
                           "Cold Monsters": "冰霜属性怪物",
                           "Convert Monsters": "击败后可转化的怪物",
                           "Einhar": "该地图会出现【伊恩哈尔】",
                           "Esh": "地图内裂隙属于艾许",
                           "Essence": "这些地图会额外出现 1 个精华",
                           "Fire Monsters": "火焰属性怪物",
                           "Hunted Traitors": "被悬赏的叛徒",
                           "Map Quality to Rarity": "地图的品质加成也会影响掉落物品的稀有度",
                           "Mortal/Sacrifice Fragment": "每使用 1 个献祭碎片就能让该地图出现献祭之礼的几率增加 50%",
                           "Niko": "该地图会出现【尼克】",
                           "Rare Map Rare Packs": "你的魔法地图额外包含4个魔法怪物群",
                           "Reflected": "不会受到反射伤害",
                           "Resonating Shrine": "共鸣神龛",
                           "Rogue Exiles": "该地图会出现 2 位额外的【盗贼流放者】",
                           "Tormented Heretic": "前 3 个被附身的怪物会掉落 1 张额外地图",
                           "Tul": "地图内裂隙属于托沃",
                           "Vaal Monsters Items Corrupted": "这些地图的腐化瓦尔怪物掉落的物品有 25% 的几率被腐化",
                           "Xoph": "地图内裂隙属于索伏",
                           "Boss Drop Vaal": "腐化的异界地图中的地图首领额外掉落2个瓦尔物品",
                           "Flasks Instant": "玩家使用药剂回复的生命和魔力会立即回复",
                           "Mysterious Barrels": "该地图会出现 25 个额外神秘木桶堆",
                           "Physical Monsters": "物理属性怪物",
                           "Polished Scarab": "前 3 个被附身的怪物会掉落 1 个额外的抛光圣甲虫",
                           "Ritual Rerolling": "在你的地图中的驱灵祭坛处第1次重置恩典无消耗",
                           "Rusted Scarab": "前 3 个被附身的怪物会掉落 1 个额外的锈蚀圣甲虫",
                           "Tormented Graverobber": "前 3 个被附身的怪物会掉落 1 个额外的传奇物品",
                           # "Ultimatum": "地图内有致命贪婪遭遇战",
                           "Unique Monsters Drop Corrupted": "传奇怪物掉落腐化物品",
                           "Vaal Soul On Kill": "击败敌人时，玩家获得一个额外的瓦尔之灵"}


if __name__ == "__main__":
    URL_TFT_DATA = "https://raw.githubusercontent.com/The-Forbidden-Trove/tft-data-prices/master/lsc/bulk-compasses.json"
    URL_NINJA_DATA = "https://poe.ninja/api/data/currencyoverview?league=Affliction&type=Currency"

    global_server_compass_data = load_TFTdata_from_github(URL_TFT_DATA)
    price_compass_dir_alias = Global_compass_data_alias(global_server_compass_data, compass_english2chinese)
    print(price_compass_dir_alias)

    # global_server_currency_data = load_NINJAdata_from_github()
    # for key, value in global_server_currency_data.items():
    #     if key == "lines":
    #         for each in value:
    #             if each["currencyTypeName"] == "Divine Orb":
    #                 print(each["currencyTypeName"] + " : " + str(each["receive"]["value"]) + " chaos")
