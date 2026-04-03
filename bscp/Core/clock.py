###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


import time

from bscp.Systems import open_log


class Clock:

    def __init__(
            self
    ) -> None:
        self._last_time: float = time.perf_counter()
        self._delta_time: float = 0.0
        self._time_scale: float = 1.0
        self._frame_count: int = 0
        self._fps: float = 0.0
        self._fps_timer: float = self._last_time
        open_log().log(
            "VALID",
            "Clock",
            f"created: {repr(self)}"
        )

    @property
    def delta_time(
            self
    ) -> float:
        return self._delta_time * self._time_scale

    @property
    def time_scale(
            self
    ) -> float:
        return self._time_scale

    @time_scale.setter
    def time_scale(
            self,
            scale: float
    ) -> None:
        if not isinstance(scale, float):
            open_log().log(
                "WARN",
                "Clock",
                f"time_scale: scale must be a float (currently {repr(type(scale))})"
            )
        if scale <= 0:
            open_log().log(
                "ERROR",
                "Clock",
                f"time_scale: scale must greater than 0 (currently {repr(scale)})"
            )
            return
        self._time_scale = scale

    @property
    def fps(
            self
    ) -> float:
        return self._fps

    def tick(
            self
    ) -> None:
        current_time = time.perf_counter()
        self._delta_time = current_time - self._last_time
        self._last_time = current_time

    def sleep(
            self,
            duration: float
    ) -> None:
        if not isinstance(duration, float):
            open_log().log(
                "WARN",
                "Clock",
                f"sleep: duration must be a float (currently {repr(type(duration))})"
            )
        if duration < 0:
            open_log().log(
                "ERROR",
                "Clock",
                f"sleep: duration must be greater or equal to 0 (currently {repr(duration)})"
            )
            return
        time.sleep(duration / self._time_scale)

    def reset(
            self
    ) -> None:
        self._last_time = time.perf_counter()
        self._delta_time = 0.0
        self._frame_count = 0
        self._fps = 0.0
        self._fps_timer = self._last_time

    def frame(
            self
    ) -> None:
        current_time = time.perf_counter()
        self._frame_count += 1

        elapsed = current_time - self._fps_timer
        if elapsed >= (1 / 8):
            self._fps = self._frame_count / elapsed
            self._frame_count = 0
            self._fps_timer = current_time

    def __repr__(
            self
    ) -> str:
        return f"<Clock delta_time={self._delta_time:.4f} fps={self._fps:.2f} time_scale={self._time_scale}>"
