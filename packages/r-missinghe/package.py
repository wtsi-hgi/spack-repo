# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissinghe(RPackage):
	"""Missing Outcome Data in Health Economic Evaluation

	Contains a suite of functions for health economic evaluations with missing outcome data. 
  The package can fit different types of statistical models under a fully Bayesian approach using the software 'JAGS' (which should be installed locally and which is loaded in 'missingHE' via the 'R' package 'R2jags'). 
  Three classes of models can be fitted under a variety of missing data assumptions: selection models, pattern mixture models and hurdle models.
  In addition to model fitting, 'missingHE' provides a set of specialised functions to assess model convergence and fit, and to summarise the statistical and economic results using different types of measures and graphs. 
  The methods implemented are described in Mason (2018) <doi:10.1002/hec.3793>, Molenberghs (2000) <doi:10.1007/978-1-4419-0300-6_18> and Gabrio (2019) <doi:10.1002/sim.8045>.
	"""
	
	cran = "missingHE" 

	version("1.5.0", md5="3fcd56b45ba9da44c16dc22478ec1215")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mcmcplots", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggmcmc", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-bcea", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mcmcr", type=("build", "run"))
