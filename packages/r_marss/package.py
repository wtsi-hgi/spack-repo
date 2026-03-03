# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarss(RPackage):
	"""Multivariate Autoregressive State-Space Modeling

	The MARSS package provides maximum-likelihood parameter
    estimation for constrained and unconstrained linear multivariate autoregressive
    state-space (MARSS) models, including partially deterministic models. MARSS models are a class 
    of dynamic linear model (DLM) and vector autoregressive model (VAR)
    model. Fitting available via Expectation-Maximization (EM), BFGS (using optim), and 'TMB'
    (using the 'marssTMB' companion package). Functions are provided for parametric and 
    innovations bootstrapping, Kalman filtering and smoothing, model selection criteria including
    bootstrap AICb, confidences intervals via the Hessian approximation or bootstrapping, and all
    conditional residual types. See the user guide for examples of dynamic factor analysis, 
    dynamic linear models, outlier and shock detection, and multivariate AR-p models.  
    Online workshops (lectures, eBook, and computer labs) 
    at <https://atsa-es.github.io/>.
	"""
	
	homepage = "https://atsa-es.github.io/MARSS/"
	cran = "MARSS" 

	version("3.11.9", md5="162badce002b5bbf27ab8a9dce49077a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-kfas@1.0.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
