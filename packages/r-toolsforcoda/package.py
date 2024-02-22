# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToolsforcoda(RPackage):
	"""Multivariate Tools for Compositional Data Analysis

	Provides functions for multivariate analysis with compositional data. Includes a function for doing compositional canonical correlation analysis.  This analysis requires two data matrices of compositions, which can be adequately transformed and used as entries in a specialized program for canonical correlation analysis, that is able to deal with singular covariance matrices. The methodology is described in Graffelman et al. (2017) <doi:10.1101/144584>. A function for log-ratio principal component analysis with condition number computations has been added to the package.
	"""
	
	homepage = "www.R-project.org"
	cran = "ToolsForCoDa" 

	version("1.0.6", md5="3be528b1f0ed2e0438c7de72a4dbbb54")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-hardyweinberg", type=("build", "run"))
