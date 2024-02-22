# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPavo(RPackage):
	"""Perceptual Analysis, Visualization and Organization of Spectral
Colour Data

	A cohesive framework for the spectral and spatial analysis of 
    colour described in Maia, Eliason, Bitton, Doucet & Shawkey (2013) 
    <doi:10.1111/2041-210X.12069> and Maia, Gruson, Endler & White (2019)
    <doi:10.1111/2041-210X.13174>.
	"""
	
	homepage = "http://pavo.colrverse.com"
	cran = "pavo" 

	version("2.9.0", md5="5d5c99d58dbaefca67c5ecc31c30e5ee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-geometry@0.4:", type=("build", "run"))
	depends_on("r-lightr@1:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
