# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsmselect(RPackage):
	"""Linear and Smooth Predictor Modelling with Penalisation and
Variable Selection

	Fit a model with potentially many linear and smooth predictors. Interaction
    effects can also be quantified. Variable selection is done using penalisation. For l1-type penalties
    we use iterative steps alternating between using linear predictors (lasso) and smooth predictors
    (generalised additive model).
	"""
	
	cran = "plsmselect" 

	version("0.2.0", md5="42e777e762081521c88e91e0916edc29")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-glmnet@2.0.16:", type=("build", "run"))
	depends_on("r-mgcv@1.8.26:", type=("build", "run"))
	depends_on("r-survival@2.43.3:", type=("build", "run"))
