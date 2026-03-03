# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiocc(RPackage):
	"""Fits Multivariate Spatio-Temporal Occupancy Model

	Spatio-temporal multivariate occupancy models can handle multiple species in occupancy models.  This method for fitting such models is described in Hepler and Erhardt (2021) "A spatiotemporal model for multivariate occupancy data" <https://onlinelibrary.wiley.com/doi/abs/10.1002/env.2657>.
	"""
	
	cran = "multiocc" 

	version("0.2.1", md5="2daf9019c3146b6c05015c978b16ca95")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
