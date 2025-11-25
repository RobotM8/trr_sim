# Toulouse Robot Race simulator

This repository host a python libray to help create simulation for the [Toulouse Robot Race](http://www.toulouse-robot-race.org/).

## Dependencies

- [PyBullet](https://pybullet.org/wordpress/) a real-time physic simulation engine

## Installation

I do not intend to publish this library to PyPi.
In order to install this library, clone the repository

```bash
git clone https://github.com/RobotM8/trr_sim.git
```

and install the library with `pip`

```bash
cd trr_sim
pip install .
```

or with [`uv``](https://docs.astral.sh/uv/)

```bash
uv pip install .
```

## Example

There is a simulation example in the `examples` folder.
It shows how to import the track into PyBullet and how to get the track waypoints.
