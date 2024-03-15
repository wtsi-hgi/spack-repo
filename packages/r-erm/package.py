# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErm(RPackage):
	"""Extended Rasch Modeling

	Fits Rasch models (RM), linear logistic test models (LLTM), rating scale model (RSM), linear rating scale models (LRSM), partial credit models (PCM), and linear partial credit models (LPCM).  Missing values are allowed in the data matrix.  Additional features are the ML estimation of the person parameters, Andersen's LR-test, item-specific Wald test, Martin-Loef-Test, nonparametric Monte-Carlo Tests, itemfit and personfit statistics including infit and outfit measures, ICC and other plots, automated stepwise item elimination, simulation module for various binary data matrices.
	"""
	
	cran = "eRm" 

	version("1.0-6", md5="c30c91e3d2c8274da69166d5b2d9a031")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
