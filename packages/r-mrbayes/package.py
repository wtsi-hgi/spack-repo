# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrbayes(RPackage):
	"""Bayesian Summary Data Models for Mendelian Randomization Studies

	Bayesian estimation of inverse variance weighted (IVW), Burgess 
    et al. (2013) <doi:10.1002/gepi.21758>, and MR-Egger, Bowden et 
    al. (2015) <doi:10.1093/ije/dyv080>, summary data models for Mendelian 
    randomization analyses.
	"""
	
	homepage = "https://github.com/okezie94/mrbayes"
	cran = "mrbayes" 

	version("0.5.1", md5="91fd7752cc96d34c6c34575576e98abc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
