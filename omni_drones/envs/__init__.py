# MIT License
#
# Copyright (c) 2023 Botian Xu, Tsinghua University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# from .single import Hover, Track, FlyThrough
from .single import Hover, SingleJuggleVolleyball, Pinball
from .payload import PayloadHover, PayloadTrack, PayloadFlyThrough
from .inv_pendulum import InvPendulumHover, InvPendulumTrack, InvPendulumFlyThrough
from .dragon import DragonHover
from .platform import PlatformHover, PlatformTrack, PlatformFlyThrough
from .transport import TransportHover, TransportTrack, TransportFlyThrough
from .formation import Formation
from .rearrange import Rearrange
from .isaac_env import IsaacEnv

# try:
#      from .single import Pinball
#      from .single import Forest
#  except ModuleNotFoundError:
#      print(
#          "To run the environments which use `ContactSensor` and `RayCaster`,"
#          "please install Isaac Orbit (https://github.com/NVIDIA-Omniverse/orbit)."
#      )
