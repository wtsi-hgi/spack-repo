# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdsmap(RPackage):
	"""High Density Genetic Linkage Mapping using Multidimensional
Scaling

	Estimate genetic linkage maps for markers on a single chromosome (or in a single linkage group) from pairwise recombination fractions or intermarker distances using weighted metric multidimensional scaling. The methods are suitable for autotetraploid as well as diploid populations. Options for assessing the fit to a known map are also provided. Methods are discussed in detail in Preedy and Hackett (2016) <doi:10.1007/s00122-016-2761-8>.
	"""
	
	cran = "MDSMap" 

	version("1.1", md5="9103d463d31539e0bb7c0d2535eb595f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-smacof@1.9:", type=("build", "run"))
	depends_on("r-princurve@2.1.2:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
