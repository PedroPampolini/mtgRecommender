
class DeckType:
  def __init__(self, name, tier, deckQuantity, format):
    self.name = name
    self.tier = tier
    self.deckQuantity = deckQuantity
    self.format = format
    self.url = self.makeUlr(name, format)
    self.deckList = []
    
  def makeUlr(self, name: str, format: str):
    name = name.replace(" ", "-").lower()
    return f"https://mtgdecks.net/{format}/{name}"
  
  def __str__(self):
    return f"[{self.name} - {self.tier} - {self.deckQuantity} - {self.format} - {self.url}]"
  
  def __repr__(self):
    return f"[{self.name} - {self.tier} - {self.deckQuantity} - {self.format} - {self.url}]"
  
  def toDict(self):
    deckListDict = []
    for deck in self.deckList:
      deckListDict.append(deck.toDict())
    return {
      "name": self.name,
      "tier": self.tier,
      "deckQuantity": self.deckQuantity,
      "format": self.format,
      "url": self.url,
      "deckList": deckListDict
    }

class Deck:
  def __init__(self, name, deckType, url, _type, rank, playersQuantity):
    self.name = name
    self.deckType = deckType
    self.playersQuantity = 0
    self.type = _type
    self.rank = rank
    self.url = url
    self.cards = []
    
  def __str__(self):
    return f"[{self.name} - {self.deckType.name} - {self.playersQuantity} - {self.type} - {self.rank} - {self.url}]"
  
  def __repr__(self):
    return f"[{self.name} - {self.deckType.name} - {self.playersQuantity} - {self.type} - {self.rank} - {self.url}]"
  
  def toDict(self):
    cardsDict = []
    # for card in self.cards:
    #   cardsDict.append(card.toDict())
    return {
      "name": self.name,
      "deckType": self.deckType.name,
      "playersQuantity": self.playersQuantity,
      "type": self.type,
      "rank": self.rank,
      "url": self.url,
      "cards": cardsDict
    }
