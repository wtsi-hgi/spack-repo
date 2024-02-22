# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmbayes(RPackage):
	"""Joint Modeling of Longitudinal and Time-to-Event Data under a
Bayesian Approach

	Shared parameter models for the joint modeling of longitudinal and time-to-event data using MCMC; Dimitris Rizopoulos (2016) <doi:10.18637/jss.v072.i07>. 
	"""
	
	homepage = "https://github.com/drizopoulos/JMbayes"
	cran = "JMbayes" 

	version("0.8-85", md5="68c3480dc34ca59407c802b4660a12db")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jagsui", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
