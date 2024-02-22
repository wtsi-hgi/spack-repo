# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskregression(RPackage):
	"""Risk Regression Models and Prediction Scores for Survival
Analysis with Competing Risks

	Implementation of the following methods for event history analysis.
    Risk regression models for survival endpoints also in the presence of competing
    risks are fitted using binomial regression based on a time sequence of binary
    event status variables. A formula interface for the Fine-Gray regression model
    and an interface for the combination of cause-specific Cox regression models.
    A toolbox for assessing and comparing performance of risk predictions (risk
    markers and risk prediction models). Prediction performance is measured by the
    Brier score and the area under the ROC curve for binary possibly time-dependent
    outcome. Inverse probability of censoring weighting and pseudo values are used
    to deal with right censored data. Lists of risk markers and lists of risk models
    are assessed simultaneously. Cross-validation repeatedly splits the data, trains
    the risk prediction models on one part of each split and then summarizes and
    compares the performance across splits.
	"""
	
	homepage = "https://github.com/tagteam/riskRegression"
	cran = "riskRegression" 

	version("2023.12.21", md5="a5fb11f16239940fb066a6d6e36e9525")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lava@1.6.5:", type=("build", "run"))
	depends_on("r-mets", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-prodlim@2018.4.18:", type=("build", "run"))
	depends_on("r-publish", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rms@5.1.3:", type=("build", "run"))
	depends_on("r-survival@2.44.1:", type=("build", "run"))
	depends_on("r-timereg@1.9.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
