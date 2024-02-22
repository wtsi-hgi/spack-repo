# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeslicer(RPackage):
	"""To Slice Phylogenetic Trees and Infer Evolutionary Patterns Over
Time

	Provide a range of functions with multiple criteria for cutting phylogenetic trees at any evolutionary depth. It enables users to cut trees in any orientation, such as rootwardly (from root to tips) and tipwardly (from tips to its root), or allows users to define a specific time interval of interest. It can also be used to create multiple tree pieces of equal temporal width. Moreover, it allows the assessment of novel temporal rates for various phylogenetic indexes, which can be quickly displayed graphically.
	"""
	
	homepage = "https://github.com/AraujoMat/treesliceR"
	cran = "treesliceR" 

	version("1.0.1", md5="3c9445192bbed394f0cead66d1fb5388")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape@5.7.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-sf@1.0.9:", type=("build", "run"))
