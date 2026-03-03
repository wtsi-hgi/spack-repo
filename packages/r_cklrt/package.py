# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCklrt(RPackage):
	"""Composite Kernel Machine Regression Based on Likelihood Ratio
Test

	Composite Kernel Machine Regression based on Likelihood Ratio Test (CKLRT): in this package, we develop a kernel machine regression framework to model the overall genetic effect of a SNP-set, considering the possible GE interaction. Specifically, we use a composite kernel to specify the overall genetic effect via a nonparametric function and we model additional covariates parametrically within the regression framework. The composite kernel is constructed as a weighted average of two kernels, one corresponding to the genetic main effect and one corresponding to the GE interaction effect. We propose a likelihood ratio test (LRT) and a restricted likelihood ratio test (RLRT) for statistical significance. We derive a Monte Carlo approach for the finite sample distributions of LRT and RLRT statistics. (N. Zhao, H. Zhang, J. Clark, A. Maity, M. Wu. Composite Kernel Machine Regression based on Likelihood Ratio Test with Application for Combined Genetic and Gene-environment Interaction Effect (Submitted).) 
	"""
	
	cran = "CKLRT" 

	version("0.2.3", md5="fe2f2174f9b9dd253ffa123713b0e800")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
