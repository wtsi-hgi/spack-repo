# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmq(RPackage):
	"""Dynamic Multiple Quantile (DMQ) Model

	Perform estimation, prediction, and simulations using the Dynamic Multiple Quantile model of Catania and Luati (2023) <doi:10.1016/j.jeconom.2022.11.002>. Can be used to estimate a set of conditional time-varying quantiles of a time series that do not cross.
	"""
	
	cran = "DMQ" 

	version("0.1.2", md5="bf374ebe2b7383221da683a314f5b82a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
