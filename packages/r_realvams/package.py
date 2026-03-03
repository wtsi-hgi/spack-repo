# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRealvams(RPackage):
	"""Multivariate VAM Fitting

	Fits a multivariate value-added model (VAM), see Broatch, Green, and Karl (2018) <doi:10.32614/RJ-2018-033> and Broatch and Lohr (2012) <doi:10.3102/1076998610396900>, with normally distributed test scores and a binary outcome indicator. A pseudo-likelihood approach, Wolfinger (1993) <doi:10.1080/00949659308811554>, is used for the estimation of this joint generalized linear mixed model.  The inner loop of the pseudo-likelihood routine (estimation of a linear mixed model) occurs in the framework of the EM algorithm presented by Karl, Yang, and Lohr (2013) <DOI:10.1016/j.csda.2012.10.004>. This material is based upon work supported by the National Science Foundation under grants DRL-1336027 and DRL-1336265.  
	"""
	
	cran = "RealVAMS" 

	version("0.4-5", md5="7d275d36e0de1acf9038460773e2fdc3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
