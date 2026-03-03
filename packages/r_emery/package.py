# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmery(RPackage):
	"""Accuracy Statistic Estimation for Imperfect Gold Standards

	Produce maximum likelihood estimates of common accuracy statistics
 for multiple measurement methods when a gold standard is not available. An R 
 implementation of the expectation maximization algorithms described in Zhou et 
 al. (2011) <doi:10.1002/9780470906514> with additional functions for creating 
 simulated data and visualizing results. Supports binary, ordinal, and 
 continuous measurement methods.
	"""
	
	cran = "emery" 

	version("0.5.1", md5="528888378eeb0fa51296f72899073181")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
