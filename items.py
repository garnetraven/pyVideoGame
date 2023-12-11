from globals import *
from sprite import *

class Item:
    def __init__(self, name: str = "default", quantity: int = 0) -> None:
        self.name = name
        self.quantity = quantity
    def use(self, *args, **kwargs):
        pass
    def attack(self, *args, **kwargs):
        pass
    def __str__(self) -> str:
        return f'Name: {self.name}, Quantity: {self.quantity}'

class BlockItem(Item): # placeable item (block)
    def __init__(self, name: str, quantity: int = 0) -> None:
        super().__init__(name, quantity)
    def use(self, player, position: tuple): # placing the block
        if self.quantity > 0:
            items[self.name].use_type([player.group_list[group] for group in items[self.name].groups],
                                       player.textures[self.name],
                                       position,
                                       self.name)
            self.quantity -= 1
            if self.quantity <= 0:
                self.name = "default"
        else:
            self.name = "default"
        
class SwordItem(Item):
    def __init__(self, name: str = "default", quantity: int = 0) -> None:
        super().__init__(name, quantity)
    def attack(self, player, target):
        target.health -= 1

class ToolItem(Item):
    def __init__(self, name: str = "default", quantity: int = 0) -> None:
        super().__init__(name, quantity)
    def use(self, player, target):
        pass
            

class ItemData:
    def __init__(self, name: str, quantity: int = 1, groups: list[str] = ['sprites', 'block_group'], use_type: Entity = Entity, item_type: Item = Item) -> None:
        self.name = name
        self.quantity = quantity
        self.groups = groups
        self.use_type = use_type
        self.item_type = item_type

items: dict[str, ItemData] = {
    'grass':ItemData('grass', item_type=BlockItem),
    'dirt':ItemData('dirt', item_type=BlockItem),
    'stone':ItemData('stone', item_type=BlockItem),
    'wood_log':ItemData('wood_log', item_type=BlockItem),
    'gold':ItemData('stone', item_type=BlockItem),
    'silver':ItemData('stone', item_type=BlockItem),
    'sword':ItemData('sword', use_type="weapon", item_type=SwordItem),
    'pickaxe':ItemData('pickaxe', use_type="tool", item_type=ToolItem),
    'health_potion':ItemData('health_potion', item_type=Item)
}
