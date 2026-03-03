# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstoolbox(RPackage):
	"""Remote Sensing Data Analysis

	Toolbox for remote sensing image processing and analysis such as
    calculating spectral indexes, principal component transformation, unsupervised
    and supervised classification or fractional cover analyses.
	"""
	
	homepage = "https://bleutner.github.io/RStoolbox/"
	cran = "RStoolbox" 

	version("0.4.0", md5="4992cb43fac954ce6cb8825d5eb808aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret@6.0.79:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-exactextractr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
