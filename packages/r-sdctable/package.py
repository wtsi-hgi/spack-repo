# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdctable(RPackage):
	"""Methods for Statistical Disclosure Control in Tabular Data

	Methods for statistical disclosure control in
    tabular data such as primary and secondary cell suppression as described for example
    in Hundepol et al. (2012) <doi:10.1002/9781118348239> are covered in this package.
	"""
	
	homepage = "https://github.com/sdcTools/sdcTable"
	cran = "sdcTable" 

	version("0.32.6", md5="fc11416bfb3cb0f197159f687bc1e32d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sdchierarchies@0.19.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-glpkapi", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-matrix@1.3.0:", type=("build", "run"))
	depends_on("r-ssbtools", type=("build", "run"))
	depends_on("glpk@4.52:", type=("build", "link", "run"))
