# Caffeine

## Intro

Simple open-source clone of the [Caffeine Mac app](http://lightheadsw.com/caffeine/) for Ubuntu.

![Caffeine screenshot](http://i.imgur.com/lSLjyMw.png)

Written in Python, tested and developed on Ubuntu 14.04LTS.


## Usage

TODO Create a PPA release that does all this automatically (contributors welcome!)

    # Clone the repository
    sudo git clone https://github.com/kzar/caffeine /usr/src/caffeine
    # Add script to our path
    sudo ln /usr/src/caffeine/caffeine.py /usr/bin/caffeine.py
    # Have Caffeine start when you login
    ln -s /usr/src/caffeine/caffeine.py.desktop ~/.config/autostart/caffeine.py.desktop
    # Launch it for now
    caffeine.py &


## License

Icons are copyright James Creixems, [he kindly made them available for use, for free in any projects](https://webjac.com/design/caffeine-retina-icons/).

Source code is released under GPLv3

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
