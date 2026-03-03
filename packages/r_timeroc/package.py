# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeroc(RPackage):
	"""Time-Dependent ROC Curve and AUC for Censored Survival Data

	Estimation of time-dependent ROC curve and area under time dependent ROC curve (AUC) in the presence of censored data, with or without competing risks. Confidence intervals of AUCs and tests for comparing AUCs of two rival markers measured on the same subjects can be computed, using the iid-representation of the AUC estimator. Plot functions for time-dependent ROC curves and AUC curves are provided. Time-dependent Positive Predictive Values (PPV) and Negative Predictive Values (NPV) can also be computed. See Blanche et al. (2013) <doi:10.1002/sim.5958> and references therein for the details of the methods implemented in the package.
	"""
	
	cran = "timeROC" 

	version("0.4", md5="1e4f4bba342b7d029064d1bc9c5e1871")

	depends_on("r@2.9.1:", type=("build", "run"))
	depends_on("r-pec@2.4.4:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.1:", type=("build", "run"))
