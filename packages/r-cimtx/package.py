# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCimtx(RPackage):
	"""Causal Inference for Multiple Treatments with a Binary Outcome

	Different methods to conduct causal inference for multiple treatments with a binary outcome, including regression adjustment, vector matching, Bayesian additive regression trees, targeted maximum likelihood and inverse probability of treatment weighting using different generalized propensity score models such as multinomial logistic regression, generalized boosted models and super learner. For more details, see the paper by Hu et al. <doi:10.1177/0962280220921909>.
	"""
	
	cran = "CIMTx" 

	version("1.2.0", md5="79dac412e96c2bbe97db3b13914ca4fa")

	depends_on("r-nnet@7.3.16:", type=("build", "run"))
	depends_on("r-bart@2.9:", type=("build", "run"))
	depends_on("r-twang@2.5:", type=("build", "run"))
	depends_on("r-arm@1.2.12:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-matching@4.9.11:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-weightit@0.12:", type=("build", "run"))
	depends_on("r-tmle@1.5.0.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-cowplot@1.1.1:", type=("build", "run"))
	depends_on("r-mgcv@1.8.38:", type=("build", "run"))
	depends_on("r-metr@0.11:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-superlearner@2.0.28:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.16:", type=("build", "run"))
