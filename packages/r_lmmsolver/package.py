# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmmsolver(RPackage):
	"""Linear Mixed Model Solver

	An efficient and flexible system to solve sparse mixed model
    equations. Important applications are the use of splines to model spatial or temporal
    trends as described in Boer (2023). (<doi:10.1177/1471082X231178591>).
	"""
	
	homepage = "https://biometris.github.io/LMMsolver/index.html"
	cran = "LMMsolver" 

	version("1.0.6", md5="e57814b3105bc595d935ef2fac6ba366")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-agridat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
