from business_object.pokemon.attacker_pokemon import AttackerPokemon


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AttackerPokemon(level=0)

        # WHEN
        snorlax.level_up()

        # THEN
        assert snorlax._level == 1


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
