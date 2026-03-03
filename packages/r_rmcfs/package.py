# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmcfs(RPackage):
	"""The MCFS-ID Algorithm for Feature Selection and Interdependency
Discovery

	MCFS-ID (Monte Carlo Feature Selection and Interdependency Discovery) is a Monte Carlo method-based tool for feature selection. It also allows for the discovery of interdependencies between the relevant features. MCFS-ID is particularly suitable for the analysis of high-dimensional, 'small n large p' transactional and biological data. M. Draminski, J. Koronacki (2018) <doi:10.18637/jss.v085.i12>.
	"""
	
	homepage = "https://home.ipipan.waw.pl/m.draminski/mcfs.html"
	cran = "rmcfs" 

	version("1.3.5", md5="81fea135a57c8b6138ce2a739789c05d")

	depends_on("r-rjava@0.5.0:", type=("build", "run"))
	depends_on("r@2.70:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-data-table@1.0.1:", type=("build", "run"))
	depends_on("java@1.7:", type=("build", "link", "run"))
