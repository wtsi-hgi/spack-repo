# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmmibayes(RPackage):
	"""Bayesian Ammi Model for Continuous Data

	Flexible multi-environment trials analysis via MCMC method for Additive Main Effects and Multiplicative Model (AMMI) for continuous data. 
 Biplot with the averages and regions of confidence can be generated. The chains run in parallel on Linux systems and run serially on Windows.
	"""
	
	cran = "ammiBayes" 

	version("1.0-2", md5="e46726d57965c1d4d54e0019ea53a76f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-distfree-cr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
