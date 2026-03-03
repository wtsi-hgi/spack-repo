# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInlabru(RPackage):
	"""Bayesian Latent Gaussian Modelling using INLA and Extensions

	Facilitates spatial and general latent Gaussian modeling using
  integrated nested Laplace approximation via the INLA package (<https://www.r-inla.org>).
  Additionally, extends the GAM-like model class to more general nonlinear predictor
  expressions, and implements a log Gaussian Cox process likelihood for 
  modeling univariate and spatial point processes based on ecological survey data.
  Model components are specified with general inputs and mapping methods to the
  latent variables, and the predictors are specified via general R expressions,
  with separate expressions for each observation likelihood model in
  multi-likelihood models. A prediction method based on fast Monte Carlo sampling
  allows posterior prediction of general expressions of the latent variables.
  Ecology-focused introduction in Bachl, Lindgren, Borchers, and Illian (2019)
  <doi:10.1111/2041-210X.13168>.
	"""
	
	homepage = "http://www.inlabru.org"
	cran = "inlabru" 

	version("2.10.1", md5="2c903c742df16c05f8fac7b323ac38df")

	depends_on("r-fmesher@0.1.2:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp@1.4.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
