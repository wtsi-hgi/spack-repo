# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputelongicovs(RPackage):
	"""Longitudinal Imputation of Categorical Variables via a Joint
Transition Model

	Imputation of longitudinal categorical covariates. We use a methodological framework which ensures that the plausibility of transitions is preserved, overfitting and colinearity issues are resolved, and confounders can be utilized. See Mamouris (2023) <doi:10.1002/sim.9919> for an overview. 
	"""
	
	cran = "ImputeLongiCovs" 

	version("0.1.0", md5="53657b2a25773111fcc89f07117285d5")

	depends_on("r@3.4.4:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
