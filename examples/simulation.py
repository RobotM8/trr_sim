import os
import time

import pybullet as p
import pybullet_data
import matplotlib.pyplot as plt
import numpy as np

import trr_sim


def main():
    # Start PyBullet
    p.connect(p.GUI)

    # Load the track
    trr_sim.load_track(p)

    p.setRealTimeSimulation(1)
    p.setGravity(0, 0, -9.8)

    car = p.loadURDF(
        os.path.join(pybullet_data.getDataPath(), "racecar/racecar.urdf"),
        basePosition=[0.5, 0, 0],
        baseOrientation=p.getQuaternionFromEuler([0, 0, 3.14]),
    )
    inactive_wheels = [3, 5, 7]
    for wheel in inactive_wheels:
        p.setJointMotorControl2(
            car, wheel, p.VELOCITY_CONTROL, targetVelocity=0, force=0
        )
    wheels = [2]
    steering = [4, 6]

    # Replace the debug paramters with your controller
    targetVelocitySlider = p.addUserDebugParameter("Velocity", -10, 10, 0)
    maxForceSlider = p.addUserDebugParameter("Force", 0, 10, 10)
    steeringSlider = p.addUserDebugParameter("Steering", -0.5, 0.5, 0)
    mapButton = p.addUserDebugParameter("View Map", 0, -1, 0)

    # simulation loop
    last_show_map = 0
    while True:
        maxForce = p.readUserDebugParameter(maxForceSlider)
        targetVelocity = p.readUserDebugParameter(targetVelocitySlider)
        steeringAngle = p.readUserDebugParameter(steeringSlider)
        show_map = p.readUserDebugParameter(mapButton)

        for wheel in wheels:
            p.setJointMotorControl2(
                car,
                wheel,
                p.VELOCITY_CONTROL,
                targetVelocity=targetVelocity,
                force=maxForce,
            )

        for steer in steering:
            p.setJointMotorControl2(
                car, steer, p.POSITION_CONTROL, targetPosition=steeringAngle
            )

        if show_map != last_show_map:
            last_show_map = show_map
            pos, quat = p.getBasePositionAndOrientation(car)
            yaw = -p.getEulerFromQuaternion(quat)[2] - np.pi / 2
            car_origin = trr_sim.get_waypoints(pos[:2], yaw)
            track_origin = trr_sim.get_waypoints()
            _, ax = plt.subplots(1, 2)
            ax[0].plot(*car_origin.T, "sk")
            ax[0].plot(0, 0, "or")
            ax[1].plot(*track_origin.T, "sk")
            ax[1].plot(pos[0], pos[1], "or")
            plt.show()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
