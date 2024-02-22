# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsem(RPackage):
	"""Composite-Based Structural Equation Modeling

	Estimate, assess, test, and study linear, nonlinear, hierarchical 
  and multigroup structural equation models using composite-based approaches 
  and procedures, including estimation techniques such as partial least squares 
  path modeling (PLS-PM) and its derivatives (PLSc, ordPLSc, robustPLSc), 
  generalized structured component analysis (GSCA), generalized structured 
  component analysis with uniqueness terms (GSCAm), generalized canonical 
  correlation analysis (GCCA), principal component analysis (PCA), 
  factor score regression (FSR) using sum score, regression or 
  bartlett scores (including bias correction using Croon’s approach), 
  as well as several tests and typical postestimation procedures 
  (e.g., verify admissibility of the estimates, assess the model fit, 
  test the model fit etc.).
	"""
	
	homepage = "https://github.com/M-E-Rademaker/cSEM/"
	cran = "cSEM" 

	version("0.5.0", md5="8d20e26ff1a889199ba5f9032f8b3e76")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-expm@0.999.5:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-symmoments", type=("build", "run"))
	depends_on("r-truncatednormal", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
