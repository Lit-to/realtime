#> realtime:next
execute as @a[tag=own,limit=1] positioned 0 -64 0 run function realtime:next/am
#data modify storage realtime: time set from entity @e[type=armor_stand,tag=r_time,limit=1] HandItems[1].tag.
tag @e remove own
