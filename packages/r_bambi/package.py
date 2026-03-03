# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBambi(RPackage):
	"""Bivariate Angular Mixture Models

	Fit (using Bayesian methods) and simulate mixtures of univariate and bivariate angular distributions. Chakraborty and Wong (2021) <doi:10.18637/jss.v099.i11>.
	"""
	
	homepage = "https://doi.org/10.18637/jss.v099.i11"
	cran = "BAMBI" 

	version("2.3.5", md5="4acad584a840f8c68924ffc018e509e9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qrng", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-label-switching", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-loo@2.4.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-bridgesampling", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
