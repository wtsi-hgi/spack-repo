# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodiv(RPackage):
	"""Methods for Calculating Gradient Surface Metrics

	Methods for calculating gradient surface metrics for
    continuous analysis of landscape features. 
	"""
	
	homepage = "https://github.com/bioXgeo/geodiv"
	cran = "geodiv" 

	version("1.1.0", md5="17b974c1597ee46dfef29d6b9e403196")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-pracma@2.2.2:", type=("build", "run"))
	depends_on("r-spatial@7.3.11:", type=("build", "run"))
	depends_on("r-e1071@1.7.0:", type=("build", "run"))
	depends_on("r-sf@0.7.4:", type=("build", "run"))
	depends_on("r-zoo@1.8.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra@1.7:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
