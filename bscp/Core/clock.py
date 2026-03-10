###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import time


class Clock:

    def __init__(self) -> None:
        self._last_time: float = time.perf_counter()
        self._delta_time: float = 0.0
        self._time_scale: float = 1.0
        self._frame_count: int = 0
        self._fps: float = 0.0
        self._fps_timer: float = self._last_time

    @property
    def delta_time(self) -> float:
        return self._delta_time * self._time_scale

    @property
    def time_scale(self) -> float:
        return self._time_scale

    @time_scale.setter
    def time_scale(self, scale: float) -> None:
        if scale <= 0: raise ValueError("Time scale must be positive")
        self._time_scale = scale

    @property
    def fps(self) -> float:
        return self._fps

    def tick(self) -> None:
        current_time = time.perf_counter()
        self._delta_time = current_time - self._last_time
        self._last_time = current_time
        self._frame_count += 1
        if current_time - self._fps_timer >= 1.0:
            self._fps = self._frame_count / (current_time - self._fps_timer)
            self._frame_count = 0
            self._fps_timer = current_time

    def sleep(self, duration: float) -> None:
        if duration < 0:
            raise ValueError("Sleep duration must be non-negative")
        time.sleep(duration / self._time_scale)

    def reset(self) -> None:
        self._last_time = time.perf_counter()
        self._delta_time = 0.0
        self._frame_count = 0
        self._fps = 0.0
        self._fps_timer = self._last_time

    def __repr__(self) -> str:
        return f"<Clock delta_time={self._delta_time:.4f} fps={self._fps:.2f} time_scale={self._time_scale}>"
