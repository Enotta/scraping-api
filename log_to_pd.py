import json
import pandas as pd

# Парсинг
data = []
with open('py_log.log', 'r', encoding="utf-8") as file:
    for line in file:
        if not line.startswith("INFO:root:"):
            continue
        line = line.split("INFO:root:")[1]
        if not line:
            continue
        try:
            entry = json.loads(line)
            data.append(entry)

        except json.JSONDecodeError:
            continue

# Кодирование тэгов и реакций
unique_reactions = set()
unique_tags = set()

for entry in data:
    reactions = entry.get('reactions', {})
    unique_reactions.update(reactions.keys())
    
    tags = entry.get('tags', [])
    unique_tags.update(tags)

unique_reactions = list(unique_reactions)
unique_tags = list(unique_tags)

# Собираем датафрейм
processed_data = []
for entry in data:
    new_entry = entry.copy()
    
    reactions = new_entry.pop('reactions', {})
    tags = new_entry.pop('tags', [])
    
    for reaction in unique_reactions:
        new_entry[f'reaction_{reaction}'] = reactions.get(reaction, 0)
    
    for tag in unique_tags:
        new_entry[f'tag_{tag}'] = 1 if tag in tags else 0
    
    processed_data.append(new_entry)

df = pd.DataFrame(processed_data)
df.to_csv("api.csv")
