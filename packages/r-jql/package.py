# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJql(RPackage):
	"""Jump Q-Learning for Individualized Interval-Valued Dose Rule

	We provide tools to estimate the individualized interval-valued dose rule (I2DR) that maximizes the expected beneficial clinical outcome for each individual and returns an optimal interval-valued dose, by using the jump Q-learning (JQL) method. The jump Q-learning method directly models the conditional mean of the response given the dose level and the baseline covariates via jump penalized least squares regression under the framework of Q learning. We develop a searching algorithm by dynamic programming in order to find the optimal I2DR with the time complexity O(n2) and spatial complexity O(n). To alleviate the effects of misspecification of the Q-function, a residual jump Q-learning is further proposed to estimate the optimal I2DR. The outcome of interest includes the best partition of the entire dosage of interest, the regression coefficients of each partition, and the value function under the estimated I2DR as well as the Wald-type confidence interval of value function constructed through the Bootstrap.
	"""
	
	cran = "JQL" 

	version("3.6.9", md5="71f1138ffb38287463a5e0de6454d925")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
