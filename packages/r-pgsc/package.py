# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgsc(RPackage):
	"""Computes Powell's Generalized Synthetic Control Estimator

	Computes the generalized synthetic control estimator described in
    Powell (2017) <doi:10.7249/WR1142>.  Provides both point estimates, and hypothesis testing.
	"""
	
	homepage = "https://github.com/philipbarrett/pgsc"
	cran = "pgsc" 

	version("1.0.0", md5="ecabccfa4d3bcd2bc8058de8e1d5d351")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
