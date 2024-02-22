# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemnet(RPackage):
	"""Methods and Measures for Semantic Network Analysis

	Implements several functions for the analysis of semantic networks including different network estimation algorithms, partial node bootstrapping (Kenett, Anaki, & Faust, 2014 <doi:10.3389/fnhum.2014.00407>), random walk simulation (Kenett & Austerweil, 2016 <http://alab.psych.wisc.edu/papers/files/Kenett16CreativityRW.pdf>), and a function to compute global network measures. Significance tests and plotting features are also implemented. 
	"""
	
	homepage = "https://github.com/AlexChristensen/SemNeT"
	cran = "SemNeT" 

	version("1.4.4", md5="85230eb35a782a6c9034a79fda49f6c5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-effects", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
