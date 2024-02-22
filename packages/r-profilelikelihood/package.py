# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfilelikelihood(RPackage):
	"""Profile Likelihood for a Parameter in Commonly Used Statistical
Models

	Provides profile likelihoods for a parameter of interest in commonly used statistical models. The models include linear models, generalized linear models, proportional odds models, linear mixed-effects models, and linear models for longitudinal responses fitted by generalized least squares. The package also provides plots for normalized profile likelihoods as well as the maximum profile likelihood estimates and the kth likelihood support intervals.
	"""
	
	cran = "ProfileLikelihood" 

	version("1.3", md5="1a6b42aac666a2730ff53970d54fb3e3")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
