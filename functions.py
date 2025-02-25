def extract_features(message):
    return [1, 2, 3]

def extract_reactions(message):
    result = {}
    if message.reactions is not None: 
        for reaction in message.reactions.reactions:
            if not reaction.emoji in result:
                result[reaction.emoji] = reaction.count
    return result