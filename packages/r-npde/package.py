# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpde(RPackage):
	"""Normalised Prediction Distribution Errors for Nonlinear
Mixed-Effect Models

	Provides routines to compute normalised prediction distribution errors, a metric designed to evaluate non-linear mixed effect models such as those used in pharmacokinetics and pharmacodynamics.
	"""
	
	cran = "npde" 

	version("3.5", md5="e5af11b894801fbf4ecafdfd9e48b17a")

	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
