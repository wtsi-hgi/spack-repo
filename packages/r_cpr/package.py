# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpr(RPackage):
	"""Control Polygon Reduction

	Implementation of the Control Polygon Reduction and Control Net
    Reduction methods for finding parsimonious B-spline regression models.
	"""
	
	homepage = "https://github.com/dewittpe/cpr/"
	cran = "cpr" 

	version("0.4.0", md5="6d33f1a4d136a66fae82303671924174")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-lme4@1.1.35.1:", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
