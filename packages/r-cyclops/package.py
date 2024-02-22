# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyclops(RPackage):
	"""Cyclic Coordinate Descent for Logistic, Poisson and Survival
Analysis

	This model fitting tool incorporates cyclic coordinate descent and
    majorization-minimization approaches to fit a variety of regression models
    found in large-scale observational healthcare data.  Implementations focus
    on computational optimization and fine-scale parallelization to yield
    efficient inference in massive datasets.  Please see:
    Suchard, Simpson, Zorych, Ryan and Madigan (2013) <doi:10.1145/2414416.2414791>.
	"""
	
	homepage = "https://github.com/ohdsi/cyclops"
	cran = "Cyclops" 

	version("3.4.0", md5="5bd3dee13ba8cd5f476a2980fb5c5588")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-andromeda@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2:", type=("build", "run"))
