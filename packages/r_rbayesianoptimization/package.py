# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbayesianoptimization(RPackage):
	"""Bayesian Optimization of Hyperparameters

	A Pure R implementation of Bayesian Global Optimization with Gaussian Processes.
	"""
	
	homepage = "https://github.com/yanyachen/rBayesianOptimization"
	cran = "rBayesianOptimization" 

	version("1.2.0", md5="7efeea2c04390d6b15596985d0bdadf1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gpfit", type=("build", "run"))
