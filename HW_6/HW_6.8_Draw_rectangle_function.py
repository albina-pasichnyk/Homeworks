"""
8. Write a function with the following signature: def display_box(width: int, height: int, character="*") . This
function will draw a simple ASCII-art rectangle (non-filled) of the given height and width, using character to print
the lines. For example, display_box(5, 4, 'x') should output the following:
xxxxx
x _ x
x _ x
xxxxx
"""

def display_box(width: int, height: int, character="*"):
    print(character * width)  # Print top border
    for i in range(height - 2): # -2 as there expected top & bottom lines
        print(f'{character}{" " * (width - 2)}{character}')  # Print sides. #  -2 empty chars as there expected side lines
    if height > 1:
        print(character * width)  # Print bottom border

#display_box(6,4, '&')
#display_box(5,5)
