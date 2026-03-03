# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustblme(RPackage):
	"""Robust Bayesian Linear Mixed-Effects Models using ABC

	Bayesian robust fitting of linear mixed effects models through weighted likelihood equations and approximate Bayesian computation as proposed by Ruli et al. (2017) <arXiv:1706.01752>.
	"""
	
	homepage = "https://github.com/erlisR/robustBLME"
	cran = "robustBLME" 

	version("0.1.3", md5="fb36efe81056a07d2f538552ec0ad568")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lme4@1.1.12:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
