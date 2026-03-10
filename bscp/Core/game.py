###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from typing import List

from bscp.Core.clock import Clock
from bscp.Entities.Factions.npc import NPC
from bscp.Entities.SCPs.scp import SCP
from bscp.Systems.logger_instance import open_log
from bscp.Utils.file_utils import FileUtils
from bscp.Utils.logger import BSCPLog
from bscp.Utils.vector import Vector


class Game:

    def __init__(self):
        self.npcs: List[NPC] = []
        self.scps: List[SCP] = []
        self.clock = Clock()
        self.dt: float = 0.0
        self.log: BSCPLog = open_log()
        self.save_path = "saves/"
        FileUtils.ensure_dir(self.save_path)

    def add_npc(self, npc: NPC):
        self.npcs.append(npc)

    def get_npc(self, identifier: str | int) -> NPC | None:
        if isinstance(identifier, int):
            return self.npcs[identifier] if 0 <= identifier < len(self.npcs) else None
        elif isinstance(identifier, str):
            for npc in self.npcs:
                if npc.name == identifier:
                    return npc
        return None

    def get_all_npcs(self) -> List[NPC]:
        return self.npcs.copy()

    def add_scp(self, scp: SCP):
        self.scps.append(scp)

    def get_scp(self, identifier: str | int) -> SCP | None:
        if isinstance(identifier, int):
            return self.scps[identifier] if 0 <= identifier < len(self.scps) else None
        elif isinstance(identifier, str):
            for scp in self.scps:
                if scp.name == identifier:
                    return scp
        return None

    def get_all_scps(self) -> List[SCP]:
        return self.scps.copy()

    def update_entities(self):
        for npc in self.npcs:
            npc.update(self.dt)
        for scp in self.scps:
            scp.update(self.dt)

    def save_game(self, file_name: str = "game_save"):

        def serialize_value(value):
            if isinstance(value, Vector):
                return {"x": value.x, "y": value.y}
            elif isinstance(value, list):
                return [serialize_value(v) for v in value]
            elif isinstance(value, dict):
                return {k: serialize_value(v) for k, v in value.items() if k != "entity"}
            elif isinstance(value, (int, float, str, bool, type(None))):
                return value
            else:
                return str(value)

        def serialize_entity(entity):
            data = {
                "name": entity.name,
                "pos": serialize_value(entity.position),
                "rotation": entity.rotation,
                "velocity": serialize_value(entity.velocity),
                "active": entity.active,
                "visible": entity.visible,
                "components": {}
            }
            for comp_type, comp in entity._components.items():
                data["components"][comp_type.__name__] = serialize_value(comp.__dict__)
            return data

        state = {
            "npcs": [serialize_entity(n) for n in self.npcs],
            "scps": [serialize_entity(s) for s in self.scps]
        }
        FileUtils.save_json(state, self.save_path, file_name)

    def load_game(self, file_name: str = "game_save"):

        def deserialize_value(value):
            if isinstance(value, dict):
                if "x" in value and "y" in value and len(value) == 2:
                    return Vector(value["x"], value["y"])
                return {k: deserialize_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [deserialize_value(v) for v in value]
            return value

        def restore_entity(data, entity_class):
            from bscp.Entities.Components import COMPONENT_REGISTRY
            entity = entity_class(
                name=data.get("name", "Entity"),
                position=deserialize_value(data.get("pos", {"x": 0, "y": 0}))
            )
            entity.rotation = data.get("rotation", 0.0)
            entity.velocity = deserialize_value(data.get("velocity", {"x": 0, "y": 0}))
            entity.active = data.get("active", True)
            entity.visible = data.get("visible", True)
            components_data = data.get("components", {})
            for comp_name, comp_values in components_data.items():
                comp_class = COMPONENT_REGISTRY.get(comp_name)
                if comp_class is None:
                    continue
                comp_instance = comp_class.__new__(comp_class)
                comp_instance.__dict__.update(
                    deserialize_value(comp_values)
                )
                comp_instance.entity = entity
                entity.add_component(comp_instance)
            return entity

        try:
            state = FileUtils.load_json(self.save_path, file_name)
            self.npcs.clear()
            self.scps.clear()
            for n_data in state.get("npcs", []):
                npc = restore_entity(n_data, NPC)
                self.npcs.append(npc)
            for s_data in state.get("scps", []):
                scp = restore_entity(s_data, SCP)
                self.scps.append(scp)
        except FileNotFoundError:
            pass

    def run(self, steps: int = 10):
        for step in range(steps):
            self.clock.tick()
            self.dt = self.clock.delta_time
            self.update_entities()
            self.clock.sleep(0.016)
