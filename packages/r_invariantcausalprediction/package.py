# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvariantcausalprediction(RPackage):
	"""Invariant Causal Prediction

	Confidence intervals for causal effects, using data collected in different experimental or environmental conditions. Hidden variables can be included in the model with a more experimental version. 
	"""
	
	cran = "InvariantCausalPrediction" 

	version("0.8", md5="3b1f03e65c6dc29aa98e65702746a46b")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
