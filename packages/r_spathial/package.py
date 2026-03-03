# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpathial(RPackage):
	"""Evolutionary Analysis

	A generic tool for manifold analysis. It allows to infer a relevant transition or evolutionary path which can highlights the features involved in a specific process. 'spathial' can be useful in all the scenarios where the temporal (or pseudo-temporal) evolution is the main problem (e.g. tumor progression). The algorithm for finding the principal path is described in: Ferrarotti et al., (2019) <doi:10.1109/TNNLS.2018.2884792>."
	"""
	
	cran = "spathial" 

	version("0.1.2", md5="aefd4bfac6c778d1dbd4a4a959f79903")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
