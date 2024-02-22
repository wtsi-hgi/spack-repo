# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcee(RPackage):
	"""The Bayesian Causal Effect Estimation Algorithm

	A Bayesian model averaging approach to causal effect estimation
    based on the BCEE algorithm. Currently supports binary or continuous
    exposures and outcomes. For more details, see 
    Talbot et al. (2015) <doi:10.1515/jci-2014-0035>
    Talbot and Beaudoin (2022) <doi:10.1515/jci-2021-0023>.
	"""
	
	cran = "BCEE" 

	version("1.3.2", md5="11c04a182a34f182f40d08d5e458f7ce")

	depends_on("r-bma", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
