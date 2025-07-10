# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomwalkrestartmh(RPackage):
	"""Random walk with restart on multiplex and heterogeneous Networks

	This package performs Random Walk with Restart on multiplex and heterogeneous networks. It is described in the following article: "Random Walk With Restart On Multiplex And Heterogeneous Biological Networks" <https://academic.oup.com/bioinformatics/article/35/3/497/5055408>.
	"""
	
	homepage = "https://github.com/alberto-valdeolivas/RandomWalkRestartMH"
	bioc = "RandomWalkRestartMH" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RandomWalkRestartMH_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RandomWalkRestartMH/RandomWalkRestartMH_1.22.0.tar.gz"]

	version("1.22.0", sha256="ccb300c5b0cd8af6921f2f96ddbaddd63579db48b9d0f5da553cd206ae107057")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
