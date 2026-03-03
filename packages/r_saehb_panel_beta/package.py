# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaehbPanelBeta(RPackage):
	"""Small Area Estimation using HB for Rao Yu Model under Beta
Distribution

	Several functions are provided for small area estimation at
    the area level using the hierarchical bayesian (HB) method with panel
    data under beta distribution for variable interest. This package also
    provides a dataset produced by data generation. The 'rjags' package is
    employed to obtain parameter estimates. Model-based estimators involve
    the HB estimators, which include the mean and the variation of the
    mean. For the reference, see Rao and Molina (2015, ISBN:
    978-1-118-73578-7).
	"""
	
	homepage = "https://github.com/DianRahmawatiSalis/saeHB.panel.beta"
	cran = "saeHB.panel.beta" 

	version("0.1.3", md5="58aa2d0eb476c3bfbb59c96e4d715ba5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
