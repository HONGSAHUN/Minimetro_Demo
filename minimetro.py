from dataclasses import dataclass

MIN_CAR_COUNT = 2
MAX_CAR_COUNT = 12
MAX_PASSENGERS_PER_CAR = 100


@dataclass(frozen=True)
class MetroTemplate:
    name: str
    station_style: str
    line_color_system: str


SEOUL_METRO_TEMPLATE = MetroTemplate(
    name="Seoul Metro",
    station_style="dense transfer hubs",
    line_color_system="numbered lines with clear color coding",
)

TOKYO_METRO_TEMPLATE = MetroTemplate(
    name="Tokyo Metro",
    station_style="high-frequency urban network",
    line_color_system="alphabet + number station indexing",
)


class Train:
    def __init__(self, car_count: int) -> None:
        if not MIN_CAR_COUNT <= car_count <= MAX_CAR_COUNT:
            raise ValueError(
                f"car_count must be between {MIN_CAR_COUNT} and {MAX_CAR_COUNT}"
            )

        self.car_count = car_count
        self._passengers_per_car = [0] * car_count

    @property
    def max_capacity(self) -> int:
        return self.car_count * MAX_PASSENGERS_PER_CAR

    @property
    def passenger_count(self) -> int:
        return sum(self._passengers_per_car)

    def board(self, car_index: int, passengers: int) -> None:
        if not 0 <= car_index < self.car_count:
            raise IndexError("car_index is out of range")

        if passengers < 0:
            raise ValueError("passengers must be non-negative")

        current = self._passengers_per_car[car_index]
        if current + passengers > MAX_PASSENGERS_PER_CAR:
            raise ValueError("a single car cannot exceed 100 passengers")

        self._passengers_per_car[car_index] = current + passengers

    def alight(self, car_index: int, passengers: int) -> None:
        if not 0 <= car_index < self.car_count:
            raise IndexError("car_index is out of range")

        if passengers < 0:
            raise ValueError("passengers must be non-negative")

        current = self._passengers_per_car[car_index]
        if passengers > current:
            raise ValueError("cannot alight more passengers than currently in the car")

        self._passengers_per_car[car_index] = current - passengers
