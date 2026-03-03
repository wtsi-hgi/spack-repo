# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIivpredictor(RPackage):
	"""Modeling Within Individual Variability as Predictor

	Time parceling method and Bayesian variability modeling methods for modeling within individual variability indicators as predictors.For more details, see <https://github.com/xliu12/IIVpredicitor>.  
	"""
	
	cran = "IIVpredictor" 

	version("0.1.0", md5="17002bd90de77568413a44bcde851081")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
