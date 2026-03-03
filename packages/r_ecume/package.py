# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcume(RPackage):
	"""Equality of 2 (or k) Continuous Univariate and Multivariate
Distributions

	We implement (or re-implements in R) a variety of statistical tools. They are focused on non-parametric two-sample (or k-sample) distribution comparisons in the univariate or multivariate case. See the vignette for more info.
	"""
	
	cran = "Ecume" 

	version("0.9.1", md5="f73491fd7ab9b44d669264a33afebbcb")

	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
