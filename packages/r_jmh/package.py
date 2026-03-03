# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmh(RPackage):
	"""Joint Model of Heterogeneous Repeated Measures and Survival Data

	Maximum likelihood estimation for the semi-parametric joint modeling of competing risks and longitudinal data in the presence of heterogeneous within-subject variability, proposed by Li and colleagues (2023) <arXiv:2301.06584>.
             The proposed method models the within-subject variability of the biomarker and associates it with the risk of the competing risks event. The time-to-event data is modeled using a (cause-specific) Cox proportional hazards regression model with time-fixed covariates. 
             The longitudinal outcome is modeled using a mixed-effects location and scale model. The association is captured by shared random effects. The model 
             is estimated using an Expectation Maximization algorithm.
	"""
	
	cran = "JMH" 

	version("1.0.3", md5="5eb9f32b98845713f0d3b085ddf49708")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-timeroc", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
