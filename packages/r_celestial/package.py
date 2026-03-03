# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelestial(RPackage):
	"""Collection of Common Astronomical Conversion Routines and
Functions

	Contains a number of common astronomy conversion routines, particularly the HMS and degrees schemes, which can be fiddly to convert between on mass due to the textural nature of the former. It allows users to coordinate match datasets quickly. It also contains functions for various cosmological calculations.
	"""
	
	cran = "celestial" 

	version("1.4.6", md5="aa1ad3e1f3252c636fc4904f22c83370")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-nistunits", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
