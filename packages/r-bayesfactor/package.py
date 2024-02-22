# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesfactor(RPackage):
	"""Computation of Bayes Factors for Common Designs

	A suite of functions for computing
    various Bayes factors for simple designs, including contingency tables,
    one- and two-sample designs, one-way designs, general ANOVA designs, and
    linear regression.
	"""
	
	homepage = "https://richarddmorey.github.io/BayesFactor/"
	cran = "BayesFactor" 

	version("0.9.12-4.7", md5="e4abf4b338fdf3fc940e4dd48356c408")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix@1.1.1:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-rcpp@0.11.2:", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.2:", type=("build", "run"))
