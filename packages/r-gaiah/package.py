# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaiah(RPackage):
	"""Genetic and Isotopic Assignment Accounting for Habitat
Suitability

	Tools for using genetic markers, stable isotope data, and habitat
    suitability data to calculate posterior probabilities of breeding origin of
    migrating birds.
	"""
	
	cran = "gaiah" 

	version("0.0.5", md5="87eb8e2e17614133fe6f07fa8b7d6b48")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
