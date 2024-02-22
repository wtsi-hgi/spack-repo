# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTou(RPackage):
	"""Transformed Ornstein-Uhlenbeck Model for Adsorption Kinetics

	Estimates the parameters of a Transformed Ornstein-Uhlenbeck (TOU) stochastic model for adsorption data and also the parameters of the related pseudo-n-order (PNO) model, such as the maximum adsorption capacity (qe), the adsorption rate constant (kn) and the order of the model (n).
	"""
	
	cran = "TOU" 

	version("0.1.0", md5="572e29ee708ef9375dc1b52e7d227695")

	depends_on("r-deoptim@2.2.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
