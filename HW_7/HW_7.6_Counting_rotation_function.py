"""
6. You are given a string representing a sequence of N arrows, each pointing in one of the four
cardinal directions: up (^), down (v), left(<) or right (>).
Write a function that, given a string S denoting the directions of the arrows, returns
the minimum number of arrows that must be rotated to make them all point in the same
direction
Examples:
1. Given S = "^vv<v", the function should return 2. After rotating both the first ('^') and fourth ('<')
arrows downwards ('v'), all of the arrows would point down.
2. Given S = "v>>>vv", the function should return 3. After rotating the first, fifth, and sixth arrow
rightwards, all of the arrows would point right.
3. Given S = "<<<" the function should return 0. All of the arrows already point left.
Assume that:
string S is made only of the following characters: '^', 'v, '< and/or'>'.
"""


def counting_rotation(arrows: str) -> int:
    """
    Function counting_rotation receives a string denoting the directions of the arrows and then returns the minimum
    number of arrows that must be rotated to make them all point in the same direction
    :param arrows: string with arrows
    :return: int - amount of minimum number of arrows to be rotated
    """
    arrows_dict = {}
    for each in arrows:
        arrows_dict[each] = arrows.count(each)
    return len(arrows) - max(arrows_dict.values())


if __name__ == "__main__":
    assert counting_rotation('^vv<v') == 2  # Check for unequal amount of arrows to be rotated in string
    assert counting_rotation('v>>>vv') == 3  # Check for equal amount of arrows to be rotated in string
    assert counting_rotation('<<<') == 0  # Check for none of arrows to be rotated in string
