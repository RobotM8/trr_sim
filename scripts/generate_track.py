from pathlib import Path
import numpy as np

TRACK_NPY = Path(__file__).parent.parent / "src/trr_sim/track/track.npy"


def add_turn(track, radius, angle, resolution=0.1):
    start_angle = 0
    if len(track) > 1:
        vector = track[-1] - track[-2]
        start_angle = np.arctan2(vector[1], vector[0])
        if angle > 0:
            start_angle -= np.pi / 2
        else:
            start_angle += np.pi / 2
    elif len(track) == 0:
        track = np.array([0, 0])

    angle = np.radians(angle)
    center = track[-1] - radius * np.array([np.cos(start_angle), np.sin(start_angle)])
    step = resolution / radius * np.sign(angle)
    delta = 0

    while abs(delta) <= abs(angle - step):
        delta += step
        x = center[0] + radius * np.cos(start_angle + delta)
        y = center[1] + radius * np.sin(start_angle + delta)
        track = np.vstack([track, np.array([x, y])])

    x = center[0] + radius * np.cos(start_angle + angle)
    y = center[1] + radius * np.sin(start_angle + angle)
    track = np.vstack([track, np.array([x, y])])

    return track


def add_line(track, length, angle, resolution=0.1):
    angle = np.radians(angle)
    delta = 0
    if length < 0:
        resolution *= -1
    while abs(delta) < abs(length - resolution):
        delta += resolution
        track = np.vstack(
            [track, track[-1] + resolution * np.array([np.cos(angle), np.sin(angle)])]
        )
    track = np.vstack(
        [track, track[-1] + (length - delta) * np.array([np.cos(angle), np.sin(angle)])]
    )

    return track


def main():
    track = add_line(np.zeros((1, 2)), 7, 0)
    angle = -(360 - 159.6)
    track = add_turn(track, 1, -(360 - 159.6))
    track = add_line(track, 1.0305, angle)
    angle += 122.2
    track = add_turn(track, 1, 122.2)
    track = add_line(track, 0.5879, angle)
    angle += -(360 - 168.2)
    track = add_turn(track, 1, -(360 - 168.2))
    track = add_line(track, 0.5, angle)
    angle += 90
    track = add_turn(track, 1, 90)
    track = add_line(track, 1.5, angle)
    angle -= 180
    track = add_turn(track, 1, -180)

    np.save(TRACK_NPY, track)


if __name__ == "__main__":
    main()
