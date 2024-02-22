# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetcoin(RPackage):
	"""Interactive Analytic Networks

	Create interactive analytic networks. It joins the data analysis power of R to obtain coincidences, co-occurrences and correlations, and the visualization libraries of 'JavaScript' in one package.
	"""
	
	homepage = "https://modesto-escobar.github.io/netCoin-2.x/"
	cran = "netCoin" 

	version("2.0.48", md5="9350aae1b9f8142cbd8911a2370b2e8a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rd3plot@1.0.68:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.4:", type=("build", "run"))
	depends_on("r-haven@1.1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-gparotation@2022.4:", type=("build", "run"))
