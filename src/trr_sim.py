from pybullet_utils import bullet_client as bc
from pathlib import Path
import numpy as np

TRACK = Path(__file__).parent / "track/robot.urdf"
TURN_DISTANCE = 24.3  # meter


class TrrSim:
    def __init__(self, bullet_client: bc):
        self._p = bullet_client
        self.track = self._p.loadURDF(str(TRACK), [0, 0, 0])

    def reset_car(self, car_id: int):
        self.car = car_id
        rpy = self._p.getQuaternionFromEuler([0, 0, 0])
        self._p.resetBasePositionAndOrientation(car_id, [0, 0, 0.05], rpy)
        self.car_pos = np.array([0, 0])
        self.distance = 0

    def step(self):
        car_pos = np.array(self._p.getBasePositionAndOrientation(self.car)[0][:2])
        self.distance += np.linalg.norm(car_pos - self.car_pos)
        self.car_pos = car_pos
        if self.distance > TURN_DISTANCE and car_pos[0] > 7:
            print("Finish line crossed")
