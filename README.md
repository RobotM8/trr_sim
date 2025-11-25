# Toulouse Robot Race simulator

This repository host a python libray to help create simulation for the [Toulouse Robot Race](http://www.toulouse-robot-race.org/).

## Dependencies

- [PyBullet](https://pybullet.org/wordpress/) a real-time physic simulation engine
- [Onshape to robot](https://onshape-to-robot.readthedocs.io) a tool to export [onshape](https://cad.onshape.com) model to URDF
  - [OpenSCAD](https://openscad.org/) required by onshape to robot

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

## URDF model

> [!WARNING]
> You should probably not have to reproduce this step except if you forked the model to create yours

The track model was created with onshape. You can follow this [link](https://cad.onshape.com/documents/98380bfdac5e6dc8572d41ca/w/88cbaeac20a8c1178dcba289/e/1560ecb7fbde8f88f6b0c95c?renderMode=0&uiState=6926189681ade75b7486fea5) to retrieve the original document.

To synchronize with the last version of the model

1. Follow the [onshape-to-robot](https://onshape-to-robot.readthedocs.io/en/latest/getting_started.html#setting-up-your-api-key) getting started to setup your API key
2. Run the script `python scripts/sync_onshape.py`
