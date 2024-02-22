# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioinactivation(RPackage):
	"""Mathematical Modelling of (Dynamic) Microbial Inactivation

	Functions for modelling microbial inactivation under
    isothermal or dynamic conditions. The calculations are based on several mathematical models broadly
    used by the scientific community and industry. Functions enable to make predictions for cases where the
    kinetic parameters are known. It also implements functions for parameter estimation for isothermal and
    dynamic conditions. The model fitting capabilities include an Adaptive Monte Carlo method for a Bayesian
    approach to parameter estimation.
	"""
	
	cran = "bioinactivation" 

	version("1.2.3", md5="4e03ce06bc5e5f2944c6d11152555fdc")

	depends_on("r-dplyr@0.4.1:", type=("build", "run"))
	depends_on("r-desolve@1.11:", type=("build", "run"))
	depends_on("r-fme@1.3.2:", type=("build", "run"))
	depends_on("r-lazyeval@0.1.10:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-mass@7.3.39:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
