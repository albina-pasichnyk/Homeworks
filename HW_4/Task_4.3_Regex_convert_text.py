import re

# Defining variable with text from file
text_from_file = 'The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was ' \
                 'launched into low Earth orbit in 1990 and remains in operation.... It was not the first space ' \
                 'telescope, but it is one of the largest and most versatile, renowned both as a vital research tool ' \
                 'and as a public relations boon for astronomy. The Hubble telescope is named after astronomer Edwin ' \
                 'Hubble and is one of NASA\'s Great Observatories..... The Space Telescope Science Institute (STScI) ' \
                 'selects Hubble\'s targets and processes the resulting data, while the Goddard Space Flight Center (' \
                 'GSFC) controls the spacecraft.A commission headed by Lew Allen, director of the Jet Propulsion ' \
                 'Laboratory, was established to determine how the error could have arisen. The Allen Commission ' \
                 'found that a reflective null corrector, a testing device used to achieve a properly shaped ' \
                 'non-spherical mirror, had been incorrectly assembled—one lens was out of position by 1.3 mm (0.051 ' \
                 'in).'

# Defining general pattern and apply it for splitting sentences where . followed by space
pattern = re.compile(r'(?<=[.?!])\s+(?=[A-Z])')
processing_list = pattern.split(text_from_file)

# Defining edge case pattern to apply for specific list element, with its replacement.
# Note: Since unified pattern could not be found
edge_pattern = re.compile(r'(?<=\.)\s*')
edge_case = edge_pattern.split(processing_list.pop(3))
processing_list.insert(3,edge_case[0])
processing_list.insert(4,edge_case[1])

# Print each of split sentence separately
for each in processing_list:
    print(each)
