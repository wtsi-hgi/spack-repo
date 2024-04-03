# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRisca(RPackage):
	"""Causal Inference and Prediction in Cohort-Based Analyses

	Numerous functions for cohort-based analyses, either for prediction or causal inference. For causal inference, it includes Inverse Probability Weighting and G-computation for marginal estimation of an exposure effect when confounders are expected. We deal with binary outcomes, times-to-events, competing events, and multi-state data. For multistate data, semi-Markov model with interval censoring may be considered, and we propose the possibility to consider the excess of mortality related to the disease compared to reference lifetime tables. For predictive studies, we propose a set of functions to estimate time-dependent receiver operating characteristic (ROC) curves with the possible consideration of right-censoring times-to-events or the presence of confounders. Finally, several functions are available to assess time-dependent ROC curves or survival curves from aggregated data.
	"""
	
	cran = "RISCA" 

	version("1.0.5", md5="4859a55e5903fd1b445509e7b5002d78")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-relsurv", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-date", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-mosaic", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
