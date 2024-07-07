# Racing Game

A simple racing game built using Pygame. Navigate your car through the blocks without crashing!

## Getting Started

### Prerequisites

- Python 3.x
- Pygame

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/racing-game.git
    cd racing-game
    ```

2. Install Pygame:

    ```bash
    sudp pip3 install pygame
    ```

### Running the Game

1. Ensure you have the required assets in the `assets` directory:
    - `track.png` (background image of the track)
    - `porsche.png` (image of the car)

2. Run the game:

    ```bash
    python racing_game.py
    ```

### Controls

- Use the left arrow key to move the car left.
- Use the right arrow key to move the car right.

### Game Features

- Scoreboard that keeps track of how many blocks you have passed.
- Crash detection when the car collides with a block.
- Game restarts automatically after a crash.

### Customization

You can customize the game by modifying the following parameters in the `racing_game.py` file:

- `self.speedx` in the `Player` class to adjust the speed of the car.
- `self.speedy` in the `Block` class to adjust the speed of the blocks.
- `self.gap` in the `Block` class to adjust the gap between blocks.

### Contributing

Feel free to fork this repository and contribute by submitting a pull request. Any improvements or bug fixes are welcome!

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the Pygame community for providing extensive documentation and support.

