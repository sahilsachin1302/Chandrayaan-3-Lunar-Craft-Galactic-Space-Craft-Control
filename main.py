from galactic_spacecraft import GalacticSpaceCraft

if __name__ == '__main__':
    starting_position = (0, 0, 0)
    commands = input("Enter the commands (e.g., 'f b r l u d'): ").split()

    spacecraft = GalacticSpaceCraft(*starting_position)
    final_position, final_direction = spacecraft.execute_commands(commands)
    print("Starting Position:", starting_position)
    print("Final Position:", final_position)
    print("Final Direction:", final_direction)
