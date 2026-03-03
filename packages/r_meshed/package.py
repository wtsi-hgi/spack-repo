# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeshed(RPackage):
	"""Bayesian Regression with Meshed Gaussian Processes

	Fits Bayesian regression models based on latent Meshed Gaussian Processes (MGP) as described in Peruzzi, Banerjee, Finley (2020) <doi:10.1080/01621459.2020.1833889>, Peruzzi, Banerjee, Dunson, and Finley (2021) <arXiv:2101.03579>, Peruzzi and Dunson (2022) <arXiv:2201.10080>. Funded by ERC grant 856506 and NIH grant R01ES028804.
	"""
	
	cran = "meshed" 

	version("0.2.3", md5="369b666b0eee9753062b847611438df5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
