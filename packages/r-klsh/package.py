# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlsh(RPackage):
	"""Blocking for Record Linkage

	An implementation of the blocking algorithm KLSH in Steorts, Ventura, Sadinle, Fienberg (2014) <DOI:10.1007/978-3-319-11257-2_20>, which is a k-means variant of locality sensitive hashing. The method is illustrated with examples and a vignette. 
	"""
	
	cran = "klsh" 

	version("0.1.0", md5="894fb7399c6608fdf71bd948327ef3e8")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-blink", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
