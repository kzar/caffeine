# Caffeine

## Intro

Simple open-source clone of the [Caffeine Mac app](http://lightheadsw.com/caffeine/) for Ubuntu.

![Caffeine screenshot](http://i.imgur.com/lSLjyMw.png)

Written in Python, tested and developed on Ubuntu 14.04LTS.


## Installation

First make sure to remove [the other caffeine](https://launchpad.net/caffeine) if you have installed it:

    sudo apt-get remove caffeine --purge
    sudo add-apt-repository --remove ppa:caffeine-developers/ppa

Now you can install:

    sudo add-apt-repository ppa:kzar/caffeine
    sudo apt-get update && sudo apt-get install caffeine
    caffeine &


## Releasing

Upload a new PPA release (Only package maintainer needs to do this, assumes version 0.0.2):

    git clone https://github.com/kzar/caffeine
    tar -zcf caffeine_0.0.2.orig.tar.gz caffeine
    cd caffeine
    debuild -S
    dput ppa:kzar/caffeine ../caffeine_0.0.2_source.changes
    # Release for other Ubuntu releases (precise, utopic)
    http://askubuntu.com/a/30146/336620


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
