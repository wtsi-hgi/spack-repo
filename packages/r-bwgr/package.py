# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBwgr(RPackage):
	"""Bayesian Whole-Genome Regression

	Whole-genome regression methods on Bayesian framework fitted via EM
    or Gibbs sampling, single step (<doi:10.1534/g3.119.400728>), univariate and multivariate (<doi:10.1186/s12711-022-00730-w>),
    with optional kernel term and sampling techniques (<doi:10.1186/s12859-017-1582-3>).
	"""
	
	cran = "bWGR" 

	version("2.2.5", md5="1b970793238860d47e22239895404937")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
