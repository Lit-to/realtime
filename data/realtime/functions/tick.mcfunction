#> realtime:tick
#execute positioned 0 -64 0 if block ~ ~ ~ command_block{Command:"Lit_to"} unless block ~ ~ ~ command_block{LastOutput:"a"} as @a[tag=own,limit=1] run function realtime:next
