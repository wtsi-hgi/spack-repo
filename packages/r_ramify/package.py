# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamify(RPackage):
	"""Additional Matrix Functionality

	Additional matrix functionality for R including: (1) wrappers for 
    the base matrix function that allow matrices to be created from character
    strings and lists (the former is especially useful for creating block
    matrices), (2) better printing of large matrices via the generic "pretty" 
    print function, and (3) a number of convenience functions for users more
    familiar with other scientific languages like 'Julia', 'Matlab'/'Octave', or
    'Python'+'NumPy'.
	"""
	
	homepage = "https://github.com/bgreenwell/ramify"
	cran = "ramify" 

	version("0.3.3", md5="f75289f6bb01962acb2fedc7159ba250")

