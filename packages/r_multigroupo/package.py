# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultigroupo(RPackage):
	"""MultiGroup Method and Simulation Data Analysis

	Two method new of multigroup and simulation of data.
  The first technique called multigroup PCA (mgPCA) this multivariate exploration approach
  that has the idea of considering the structure of groups and / or different types
  of variables. On the other hand, the second multivariate technique called Multigroup Dimensionality
  Reduction (MDR) it is another multivariate exploration method that is based on
  projections. In addition, a method called Single Dimension Exploration (SDE) was
  incorporated for to analyze the exploration of the data. It could help us in a better
  way to observe the behavior of the multigroup data with certain variables of interest.
	"""
	
	cran = "MultiGroupO" 

	version("0.1.0", md5="a6d4e99e332ff55282fb9835c63033c3")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-plsgenomics", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-mgm", type=("build", "run"))
