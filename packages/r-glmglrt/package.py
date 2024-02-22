# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmglrt(RPackage):
	"""GLRT P-Values in Generalized Linear Models

	Provides functions to compute Generalized Likelihood Ratio Tests (GLRT) also known as Likelihood Ratio Tests (LRT) and Rao's score tests of simple
   and complex contrasts of Generalized Linear Models (GLMs). It provides the same interface as summary.glm(), adding GLRT P-values,
   less biased than Wald's P-values and consistent with profile-likelihood confidence interval generated by confint().
   See Wilks (1938) <doi:10.1214/aoms/1177732360> for the LRT chi-square approximation.
   See Rao (1948) <doi:10.1017/S0305004100023987> for Rao's score test.
   See Wald (1943) <doi:10.2307/1990256> for Wald's test.
	"""
	
	cran = "glmglrt" 

	version("0.2.2", md5="9461aba8801789371891ee9a15b36ddb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-parameters@0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
