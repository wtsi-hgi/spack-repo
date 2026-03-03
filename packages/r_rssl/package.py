# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRssl(RPackage):
	"""Implementations of Semi-Supervised Learning Approaches for
Classification

	A collection of implementations of semi-supervised classifiers
    and methods to evaluate their performance. The package includes implementations
    of, among others, Implicitly Constrained Learning, Moment Constrained Learning,
    the Transductive SVM, Manifold regularization, Maximum Contrastive Pessimistic
    Likelihood estimation, S4VM and WellSVM.
	"""
	
	homepage = "https://github.com/jkrijthe/RSSL"
	cran = "RSSL" 

	version("0.9.7", md5="2ccb1a0b6d715ac0777541a47b9a9169")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
