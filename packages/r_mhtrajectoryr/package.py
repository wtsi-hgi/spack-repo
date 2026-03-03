# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhtrajectoryr(RPackage):
	"""Bayesian Model Selection in Logistic Regression for the
Detection of Adverse Drug Reactions

	Spontaneous adverse event reports have a high potential for detecting adverse drug reactions. However, due to their dimension, the analysis of such databases requires statistical methods. We propose to use a logistic regression whose sparsity is viewed as a model selection challenge. Since the model space is huge, a Metropolis-Hastings algorithm carries out the model selection by maximizing the BIC criterion.
	"""
	
	cran = "MHTrajectoryR" 

	version("1.0.1", md5="d6a951905d7fbb3b2dffcfa89b2dba51")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
