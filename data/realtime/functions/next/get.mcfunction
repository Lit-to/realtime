#> realtime:next/get
loot replace entity @s weapon.mainhand loot realtime:predicate_van
data modify storage realtime: now.hour set from entity @s HandItems[0].tag.Now[0]
data modify storage realtime: now.minute set from entity @s HandItems[0].tag.Now[1]
data modify storage realtime: now.second set from entity @s HandItems[0].tag.Now[2]

