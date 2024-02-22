# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbst(RPackage):
	"""The Full Bayesian Evidence Test, Full Bayesian Significance Test
and the e-Value

	Provides access to a range of functions for computing and visualizing the Full Bayesian Significance Test (FBST) and the e-value for testing a sharp hypothesis against its alternative, and the Full Bayesian Evidence Test (FBET) and the (generalized) Bayesian evidence value for testing a composite (or interval) hypothesis against its alternative. The methods are widely applicable as long as a posterior MCMC sample is available.
	"""
	
	cran = "fbst" 

	version("2.2", md5="968a8bbce8fe2cab7cc7a4581d9ce133")

	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rstanarm", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
