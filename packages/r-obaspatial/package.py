# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObaspatial(RPackage):
	"""Objective Bayesian Analysis for Spatial Regression Models

	It makes an objective Bayesian analysis of the spatial regression model using both the normal (NSR) and student-T (TSR) distributions. The functions provided give prior and posterior objective densities and allow default Bayesian estimation of the model regression parameters. Details can be found in Ordonez et al. (2020) <arXiv:2004.04341>.
	"""
	
	cran = "OBASpatial" 

	version("1.9", md5="03882de7ebce96e2a2499b0a0e0b8bf7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
