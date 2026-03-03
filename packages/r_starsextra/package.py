# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarsextra(RPackage):
	"""Miscellaneous Functions for Working with 'stars' Rasters

	Miscellaneous functions for working with 'stars' objects, mainly single-band rasters. Currently includes functions for: (1) focal filtering, (2) detrending of Digital Elevation Models, (3) calculating flow length, (4) calculating the Convergence Index, (5) calculating topographic aspect and topographic slope.
	"""
	
	homepage = "https://michaeldorman.github.io/starsExtra/"
	cran = "starsExtra" 

	version("0.2.8", md5="bf9a95efcf85c074133bc919b9d5e45e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nngeo", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
