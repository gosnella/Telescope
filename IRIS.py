import argparse
import json
from Antenna import Antenna
from Telescope import Telescope


def main():

    parser = argparse.ArgumentParser(
        prog='IRIS.py',
        description='Calculates various quantities of a telescope')

    parser.add_argument('command')
    parser.add_argument('-f', '--file', type=str)

    args = parser.parse_args()

    f = open(args.file)
    telescope = json.load(f)
    coords = telescope['antennae']

    coords_list = []
    for coord in coords:
        coords_list.append(Antenna([coord['x'], coord['y'], coord['z']]))
    tscope = Telescope(coords_list)

    tscope_args = telescope['telescope']
    for arg in tscope_args:

        if args.command == 'baseline_length':
            baseline_length = tscope.baseline_length(arg["ind1"], arg["ind2"])
            print(baseline_length)

        elif args.command == 'baseline_between':
            baseline_between = tscope.baseline_between(arg["ind1"], arg["ind2"])
            print(baseline_between)

        elif args.command == 'path_difference':
            path_difference = tscope.path_difference(arg["ind1"], arg["ind2"], arg["theta"], arg["alpha"])
            print(path_difference)

        elif args.command == 'phase_difference':
            phase_difference = tscope.phase_difference(arg["ind1"], arg["ind2"], arg["wavelength"], arg["theta"], arg["alpha"])
            print(phase_difference)

        else:
            print("invalid command")


if __name__ == "__main__":

    main()

