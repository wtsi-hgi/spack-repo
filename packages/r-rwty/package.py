# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwty(RPackage):
	"""R We There Yet? Visualizing MCMC Convergence in Phylogenetics

	Implements various tests, visualizations, and metrics
    for diagnosing convergence of MCMC chains in phylogenetics.  It implements
    and automates many of the functions of the AWTY package in the R
    environment.
	"""
	
	cran = "rwty" 

	version("1.0.2", md5="f5b58de3e83e0375a410334e98f6d2a7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
