from abstract_pokemon import AbstractPokemon


class Speedster(AbstractPokemon):
    def __init__(self):
        super().__init__(stat_max=None, stat_current=None, level=0, name=None,type_pk=None)

    def get_pokemon_attack_coef(self) -> int:
        return 1 + (self.speed_current + self.sp_atk_current) / 200