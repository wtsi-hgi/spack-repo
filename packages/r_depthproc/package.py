# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepthproc(RPackage):
	"""Statistical Depth Functions for Multivariate Analysis

	Data depth concept offers a variety of powerful and user friendly
    tools for robust exploration and inference for multivariate data. The offered
    techniques may be successfully used in cases of lack of our knowledge on
    parametric models generating data due to their nature. The
    package consist of among others implementations of several data depth techniques
    involving multivariate quantile-quantile plots, multivariate scatter estimators,
    multivariate Wilcoxon tests and robust regressions.
	"""
	
	homepage = "https://www.depthproc.zstat.pl/"
	cran = "DepthProc" 

	version("2.1.5", md5="f6d169ed8279d1380a3999cf91db0f92")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
