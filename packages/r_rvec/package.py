# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvec(RPackage):
	"""Vector Representing a Random Variable

	Random vectors, called rvecs. An rvec holds
    multiple draws, but tries to behave like a standard
    R vector, including working well in data frames. Rvecs are
    useful for working with output from a simulation or
    a Bayesian analysis.
	"""
	
	homepage = "https://bayesiandemography.github.io/rvec/"
	cran = "rvec" 

	version("0.0.6", md5="1d377f2b918971c9132baab70198df9a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
