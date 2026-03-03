# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStochvoltmb(RPackage):
	"""Likelihood Estimation of Stochastic Volatility Models

	Parameter estimation for stochastic volatility models using maximum likelihood. The latent log-volatility is 
    integrated out of the likelihood using the Laplace approximation. The models are fitted via 'TMB' (Template Model
    Builder) (Kristensen, Nielsen, Berg, Skaug, and Bell (2016) <doi:10.18637/jss.v070.i05>). 
	"""
	
	homepage = "https://github.com/JensWahl/stochvolTMB"
	cran = "stochvolTMB" 

	version("0.2.0", md5="f3aa1352fd2ae1adb0ce939be3b7dcef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
