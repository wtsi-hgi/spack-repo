# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbsc(RPackage):
	""""Empirical Bayes Smoothing Splines with Correlated Errors"

	Presents a statistical method that uses a recursive algorithm for signal extraction. The method handles a non-parametric estimation for the correlation of the errors. See "Krivobokova", "Serra", "Rosales" and "Klockmann" (2021) <arXiv:1812.06948> for details.
	"""
	
	cran = "eBsc" 

	version("4.17", md5="54e1a2804f7f4fd72c0283c3dfa9a5ef")

	depends_on("r-brobdingnag", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
