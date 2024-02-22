# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayessur(RPackage):
	"""Bayesian Seemingly Unrelated Regression

	Bayesian seemingly unrelated regression with general variable selection and dense/sparse covariance matrix. The sparse seemingly unrelated regression is described in Bottolo et al. (2021) <doi:10.1111/rssc.12490>, the software paper is in Zhao et al. (2021) <doi:10.18637/jss.v100.i11>, and the model with random effects is described in Zhao et al. (2023) <doi:10.1093/jrsssc/qlad102>.
	"""
	
	cran = "BayesSUR" 

	version("2.1-6", md5="a078b3c7652eeeca27f58922d4215386")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tikzdevice", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9:", type=("build", "run"))
