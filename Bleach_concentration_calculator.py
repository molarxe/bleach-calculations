# --------------------------
# Note: EDIT THESE VARIABLES TO YOUR LIKING
"""
If you want higher concentrations of bleach you have to cool the brine down and use a higher concentration brine for such purposes

to get a high one you can use :-
Brine concentration = 20-30 % by weight
Temp = 0-5 °C
"""

MILLIAMPS = 304
BRINE_PERCENTAGE = 5
VOLUME_OF_WATER = 100
NUMBER_OF_CYCLES = 2
PERCENTAGE_OF_NAOCL_WANTED = 1
# Note DO NOT SET THE PERCENTAGE ABOVE THE THEORETICAL MAX PERCENT RUN THIS ONCE WITH IT SET TO 1% ONLY THEN CHANGE
# --------------------------


def mA_to_A(mA: float) -> float:
    return mA / 1_000


def grams_of_NaOCl_per_hour(amps: float) -> float:
    production_rate = (amps * 3_600 * 74.44) / (2 * 96_485)
    return production_rate


def weight_of_NaOCl(conc: float, volume: float) -> float:
    return volume * (conc / 100) * 1.274


def value_from_percentage(percentage: float, total: float) -> float:
    return (percentage / 100) * total


def percentage(part: float, total: float) -> float:
    return (part / total) * 100


print(
    f"NaOCl production rate at {MILLIAMPS} mA is {grams_of_NaOCl_per_hour(mA_to_A(MILLIAMPS)):.2f} g/hour"
)


print(
    f"Total weight of NaOCl attainable {weight_of_NaOCl(BRINE_PERCENTAGE, VOLUME_OF_WATER):.2f} g"
)

print(
    f"Total Theoretical Time is {(weight_of_NaOCl(BRINE_PERCENTAGE, VOLUME_OF_WATER) / grams_of_NaOCl_per_hour(mA_to_A(MILLIAMPS))):.2f} Hours"
)

print(
    f"The cycles are {NUMBER_OF_CYCLES}x of {(((weight_of_NaOCl(BRINE_PERCENTAGE, VOLUME_OF_WATER) / grams_of_NaOCl_per_hour(mA_to_A(MILLIAMPS))) * 60) / NUMBER_OF_CYCLES):.0f} Minutes each"
)

print(
    f"Total probable Percentage yield of NaOCl is ~ {percentage(weight_of_NaOCl(BRINE_PERCENTAGE, VOLUME_OF_WATER),VOLUME_OF_WATER):.2f}%"
)

print("\n\n===================================================")
print("Ignore everything above those are highly theoretical calculations")
print("===================================================\n\n")

print(
    f"True yield is around {value_from_percentage(PERCENTAGE_OF_NAOCL_WANTED, VOLUME_OF_WATER):.2f} g or 1%"
)

print(
    f"The Total electrolysis time is {(value_from_percentage(PERCENTAGE_OF_NAOCL_WANTED, VOLUME_OF_WATER) / grams_of_NaOCl_per_hour(mA_to_A(MILLIAMPS))):.2f} Hours"
)

print(
    f"The cycles are {NUMBER_OF_CYCLES}x of {(((value_from_percentage(PERCENTAGE_OF_NAOCL_WANTED, VOLUME_OF_WATER) / grams_of_NaOCl_per_hour(mA_to_A(MILLIAMPS))) * 60) / NUMBER_OF_CYCLES):.0f} Minutes each"
)
