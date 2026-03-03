# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeplots(RPackage):
	"""Visualizing Hypothesis Tests in Multivariate Linear Models

	Provides HE plot and other functions for visualizing hypothesis
    tests in multivariate linear models. HE plots represent sums-of-squares-and-products 
    matrices for linear hypotheses and for error using ellipses (in two
    dimensions) and ellipsoids (in three dimensions). The related 'candisc' package
    provides visualizations in a reduced-rank canonical discriminant space when
    there are more than a few response variables.
	"""
	
	homepage = "http://friendly.github.io/heplots/"
	cran = "heplots" 

	version("1.6.2", md5="8e6ec4d6adbe95bccccaa81aedb4315c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
