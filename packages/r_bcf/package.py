# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcf(RPackage):
	"""Causal Inference using Bayesian Causal Forests

	Causal inference for a binary treatment and continuous outcome using Bayesian Causal Forests. See Hahn, Murray and Carvalho (2020) <doi:10.1214/19-BA1195> for additional information. This implementation relies on code originally accompanying Pratola et. al. (2013) <arXiv:1309.1906>.
	"""
	
	cran = "bcf" 

	version("2.0.2", md5="b227772606c6f98fa5a4abdb7185a31c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
