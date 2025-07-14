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

	version("1.22.0", commit="80cb3ecd90785661f44a23246a8544628318a6dd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
