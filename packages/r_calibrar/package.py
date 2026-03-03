# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibrar(RPackage):
	"""Automated Parameter Estimation for Complex Models

	General optimisation and specific tools for the parameter estimation (i.e. calibration) of complex models, including stochastic ones. It implements generic functions that can be used for fitting any type of models, especially those with non-differentiable objective functions, with the same syntax as base::optim. 
  It supports multiple phases estimation (sequential parameter masking), constrained optimization (bounding box restrictions) and automatic parallel computation of numerical gradients. 
  Some common maximum likelihood estimation methods and automated construction of the objective function from simulated model outputs is provided.  
  See <https://roliveros-ramos.github.io/calibrar/> for more details.
	"""
	
	homepage = "https://roliveros-ramos.github.io/calibrar/"
	cran = "calibrar" 

	version("0.9.0", md5="ae863a364e8504ffca6f37b497330b86")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-cmaes", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lbfgsb3c", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-soma", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
