from HW_11.I_Radar import IRadar
from HW_11.I_Anti_missile_defense import IHittingTarget


# Inheritance
# Abstraction
class AirDefense(IHittingTarget, IRadar):
    def __init__(self, capability: int):
        # Hiding
        self.__name = 'Patriot'
        self.__radar = True
        self.__capability = capability

    # Polymorphism
    def _scan_area(self, quantity):
        """
        Function to scan area
        :param quantity: amount of air targets
        """
        print(f'{self.__name} is scanning area')
        print(f'{quantity} air targets were recorded')

    # Hiding
    def __air_raid_alarm_on(self):
        """Function to turn on air raid alarm"""
        print(f'Air raid alarm in Ukraine')

    # Hiding
    def __air_raid_alarm_off(self):
        """Function to turn-off air raid alarm"""
        print(f'Danger is over. Air area is clear and safe.')

    # Polymorphism
    def _hit_target(self, target_type: str, quantity: int):
        """
        Function to hit the air target
        :param target_type: type of the air target, e.g. 'missile', 'ballistic', 'UAV'
        :param quantity: amount of air targets
        """
        charge = self.__capability
        targets = quantity
        while targets > 0:
            print(f'The {target_type} target was shot down')
            targets -= 1
            charge -= 1
            if charge == 0 and targets >= 1:
                print(f'{self.__capability} {target_type} air targets were intercepted')
                print(f'{quantity - self.__capability} {target_type} targets, unfortunately, were not intercepted')
                break
            if targets == 0:
                print(f'All {target_type} targets were successfully intercepted')

    # Encapsulation
    def trigger_air_defence(self, target_type: str, quantity: int):
        """
        Function to trigger the air defence
        :param target_type: type of the air target, e.g. 'missile', 'ballistic', 'UAV'
        :param quantity: amount of air targets
        """
        self.__air_raid_alarm_on()
        self._scan_area(quantity)
        self._hit_target(target_type, quantity)
        self.__air_raid_alarm_off()


if __name__ == '__main__':
    Patriot = AirDefense(6)
    Patriot.trigger_air_defence('missile', 3)
    Patriot.trigger_air_defence('ballistic', 6)
    Patriot.trigger_air_defence('UAV', 7)
