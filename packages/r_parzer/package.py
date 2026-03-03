# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParzer(RPackage):
	"""Parse Messy Geographic Coordinates

	Parse messy geographic coordinates from various character formats
    to decimal degree numeric values. Parse coordinates into
    their parts (degree, minutes, seconds); calculate hemisphere
    from coordinates; pull out individually degrees,
    minutes, or seconds; add and subtract degrees, minutes,
    and seconds. C++ code herein originally inspired from code
    written by Jeffrey D. Bogan, but then completely re-written.
	"""
	
	homepage = "https://github.com/ropensci/parzer"
	cran = "parzer" 

	version("0.4.1", md5="7e13ac9d973807f639d510bd49acfa77")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
