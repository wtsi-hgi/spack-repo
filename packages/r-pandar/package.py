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

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="dce63a6685d1ae7eeb25fb612ba5f0980814324be72072910d066688d26ec294")

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
