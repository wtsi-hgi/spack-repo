# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepbeta(RPackage):
	"""Stepwise Procedure for Beta, Beta-Binomial and Negative Binomial
Regression Models

	Starting from a Regression Model, it provides a stepwise 
              procedure to select the linear predictor.
	"""
	
	cran = "StepBeta" 

	version("2.1.0", md5="80443082abccdad4d12eac2007a98498")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
