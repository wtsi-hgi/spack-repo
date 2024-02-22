# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdrc(RPackage):
	"""Bayesian Discharge Rating Curves

	Fits a discharge rating curve based on the power-law and the generalized power-law from data on paired stage and discharge measurements in a given river using a Bayesian hierarchical model as described in Hrafnkelsson et al. (2020) <arXiv:2010.04769>.
	"""
	
	cran = "bdrc" 

	version("1.1.0", md5="a30375f2f43875ce5f18e40c6ef16f50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
