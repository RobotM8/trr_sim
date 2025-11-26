from pathlib import Path
import numpy as np
import numpy.typing as npt
import pybullet as p

DATA = Path(__file__).parent / "track"
TRACK = DATA / "robot.urdf"
POLYLINE = np.load(DATA / "track.npy")


def load_track(client):
    """Load the TRR track into pybullet"""
    return client.loadURDF(
        str(TRACK),
        basePosition=[0, 0, 0],
        baseOrientation=p.getQuaternionFromEuler([0, 0, np.pi]),
    )


def get_waypoints(position: npt.ArrayLike = [0, 0], yaw: float = 0.0):
    """Return the waypoints representing the track

    Passing optional position and yaw will modify the waypoints so that the provided position becomes the origin of the referential.
    """
    translation = np.array(position)
    c = np.cos(yaw)
    s = np.sin(yaw)
    rotation = np.array([[c, -s], [s, c]])
    return (POLYLINE - translation) @ rotation
