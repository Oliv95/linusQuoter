#!/usr/bin/python3
#
# Much like the program fortune but with quotes from Linus Torvalds
#
# Copyright 2017 Axel Olivecrona <axel.olivecrona1995@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import random

lines = open("quotes").readlines()
line  = random.choice(lines)[:-1:]
print(line)
