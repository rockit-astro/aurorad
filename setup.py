#
# This file is part of aurorad.
#
# aurorad is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# aurorad is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with aurorad.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='warwick.observatory.aurora',
      version='0',
      packages = ['warwick.observatory.aurora'],
      author='Paul Chote',
      description='Common backend code for the Aurora daemon',
      license='GNU GPLv3',
      author_email='p.chote@warwick.ac.uk',
      url='https://github.com/warwick-one-metre/aurorad',
)
