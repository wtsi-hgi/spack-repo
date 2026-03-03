# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalmpldc(RPackage):
	"""Penalised Likelihood for Survival Analysis with Dependent
Censoring

	Fitting Cox proportional hazard model under dependent right censoring using copula and maximum penalised likelihood methods.
	"""
	
	cran = "survivalMPLdc" 

	version("0.1.1", md5="98bfbc354709f5c1f0f630bac01c921f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
