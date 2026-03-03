# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIeeeround(RPackage):
	"""Functions to set and get the IEEE rounding mode

	A pair of functions for getting and setting the IEEE
        rounding mode for floating point computations.
	"""
	
	homepage = "http://www.sci.unich.it/~amato"
	cran = "ieeeround" 

	version("0.2-0", md5="42e3eee0d17a8b29604ee1d023a746f5")

