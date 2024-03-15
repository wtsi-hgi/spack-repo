# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPandar(RPackage):
	"""PANDA Algorithm

	Runs PANDA, an algorithm for discovering novel network structure by combining information from multiple complementary data sources.
	"""
	
	bioc = "pandaR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pandaR_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pandaR/pandaR_1.34.0.tar.gz"]

	version("1.34.0", md5="203422d8a9df096677530f57bffe9e9c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
