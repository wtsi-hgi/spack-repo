# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesgpfit(RPackage):
	"""Fast Bayesian Gaussian Process Regression Fitting

	Bayesian inferences on nonparametric regression via Gaussian Processes with a modified exponential square kernel using a basis expansion approach.
	"""
	
	cran = "BayesGPfit" 

	version("1.1.0", md5="30d12ad2bc63d390bd57d1dcbb29a715")

	depends_on("r-lattice", type=("build", "run"))
