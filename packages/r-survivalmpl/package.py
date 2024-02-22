# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalmpl(RPackage):
	"""Penalised Maximum Likelihood for Survival Analysis Models

	Estimate the regression coefficients and the baseline hazard 
      of proportional hazard Cox models with left, right or interval censored survival data 
      using maximum penalised likelihood. A 'non-parametric' smooth estimate of the baseline hazard
      function is provided.
	"""
	
	cran = "survivalMPL" 

	version("0.2-3", md5="5d5132e8186eb188eabd9c23b362d020")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
