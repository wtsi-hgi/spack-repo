# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplinetree(RPackage):
	"""Longitudinal Regression Trees and Forests

	Builds regression trees and random forests for longitudinal or functional data using a spline projection method. Implements and extends the work of Yu and Lambert (1999) <doi:10.1080/10618600.1999.10474847>. This method allows trees and forests to be built while considering either level and shape or only shape of response trajectories. 
	"""
	
	homepage = "https://github.com/anna-neufeld/splinetree"
	cran = "splinetree" 

	version("0.2.0", md5="b3d95a262bc6d4f982f2b8497f84c428")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mosaic", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-treeclust", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
