# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvcorr(RPackage):
	"""Correlation of Bivariate Survival Times

	Estimates correlation coefficients with associated
   confidence limits for bivariate, partially censored survival times. Uses
   the iterative multiple imputation approach proposed
   by Schemper, Kaider, Wakounig and Heinze (2013) <doi:10.1002/sim.5874>. Provides a scatterplot function to visualize the bivariate 
   distribution, either on the original time scale or as copula.
	"""
	
	cran = "SurvCorr" 

	version("1.1", md5="7e5bf2f83161ba1dc96b6db2c68f3bd3")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
