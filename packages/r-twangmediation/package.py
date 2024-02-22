# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwangmediation(RPackage):
	"""Twang Causal Mediation Modeling via Weighting

	Provides functions for estimating natural direct and indirect effects for mediation analysis. It uses weighting where the weights are functions of estimates of the probability of exposure or treatment assignment (Hong, G (2010). <https://cepa.stanford.edu/sites/default/files/workshops/GH_JSM%20Proceedings%202010.pdf> Huber, M. (2014). <doi:10.1002/jae.2341>). Estimation of probabilities can use generalized boosting or logistic regression. Additional functions provide diagnostics of the model fit and weights. The vignette provides details and examples.
	"""
	
	cran = "twangMediation" 

	version("1.2", md5="697afe579380a98775fc1ecd2dfa7e37")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-gbm@1.5.3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
