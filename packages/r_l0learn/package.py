# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL0learn(RPackage):
	"""Fast Algorithms for Best Subset Selection

	Highly optimized toolkit for approximately solving L0-regularized learning problems (a.k.a. best subset selection).
    The algorithms are based on coordinate descent and local combinatorial search.
    For more details, check the paper by Hazimeh and Mazumder (2020) <doi:10.1287/opre.2019.1919>.
	"""
	
	homepage = "https://github.com/hazimehh/L0Learn"
	cran = "L0Learn" 

	version("2.1.0", md5="9d251a0c149b86f984515adc01a8a81f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
