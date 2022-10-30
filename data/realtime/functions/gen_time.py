import json
result = {"pools": [{"rolls": 1, "entries": []}]}
#item = {"type": "minecraft:dynamic", "name": "minecraft:contents", "conditions": [{"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"equipment": {"mainhand": {"nbt": "{Time: '{\"extra\":[{\"color\":\"red\",\"extra\":[{\"color\":\"gray\",\"clickEvent\":{\"action\":\"suggest_command\",\"value\":\"Lit_to\"},\"extra\":[{\"text\":\"\"},{\"underlined\":true,\"color\":\"red\",\"text\":\"Lit_to\"},{\"italic\":true,\"color\":\"red\",\"translate\":\"command.context.here\"}],\"text\":\"\"}],\"text\":\"\"}],\"text\":\"[12:00:56] \"}'}"}}}}, {"type": "minecraft:item", "name": "magma_cream", "functions": [{"function": "minecraft:set_nbt", "tag": "{Now:[0,0,0]}"}]}]}

#i=37429
result_l = list()
#86400
for i in range(86400):
    timeint = i
    hour = int(timeint/3600)
    minute = int(timeint/60 % 60)
    second = int(timeint % 60)
    timel = [hour, minute, second]
    item_copy={}
    message=str()
    times=str()
    item_copy = {"type": "minecraft:dynamic", "name": "minecraft:contents", "conditions": [{"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"equipment": {"mainhand": {"nbt": "{Time: '{\"extra\":[{\"color\":\"red\",\"extra\":[{\"color\":\"gray\",\"clickEvent\":{\"action\":\"suggest_command\",\"value\":\"/Lit_to\"},\"extra\":[{\"text\":\"\"},{\"underlined\":true,\"color\":\"red\",\"text\":\"Lit_to\"},{\"italic\":true,\"color\":\"red\",\"translate\":\"command.context.here\"}],\"text\":\"\"}],\"text\":\"\"}],\"text\":\"[12:00:56] \"}'}"}}}}], "type": "minecraft:item", "name": "magma_cream", "functions": [{"function": "minecraft:set_nbt", "tag": "{Now:[0,0,0]}"}]}
    message = item_copy["conditions"][0]["predicate"]["equipment"]["mainhand"]["nbt"]
    message = message[:-8] + str(second).zfill(2)+message[-6:]
    message = message[:-11] + str(minute).zfill(2)+message[-9:]
    message = message[:-14] + str(hour).zfill(2)+message[-12:]
    item_copy["conditions"][0]["predicate"]["equipment"]["mainhand"]["nbt"] = message
    times="{Now:"+str(timel)+"}"
    item_copy["functions"][0]["tag"]=times
    result_l.append(item_copy)
result["pools"][0]["entries"] = result_l

f = open(r"data/realtime/loot_tables/predicate_van.json",mode="w",encoding="utf-8") 
json.dump(result, f)
f.close()





