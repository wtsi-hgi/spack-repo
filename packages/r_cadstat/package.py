# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCadstat(RPackage):
	"""Provides a GUI to Several Statistical Methods

	Using Java GUI for R (JGR), CADStat provides a user
    interface for several statistical methods -
    scatterplot, boxplot, linear regression, generalized linear
    regression, quantile regression, conditional probability
    calculations, and regression trees.
	"""
	
	homepage = "http://www.rforge.net/CADStat/"
	cran = "CADStat" 

	version("3.0.8", md5="e81ca5d3bb1bde12a86060a8e2e8c439")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-jgr@1.7.10:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-bio-infer", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-javagd", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
