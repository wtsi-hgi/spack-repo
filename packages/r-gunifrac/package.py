# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGunifrac(RPackage):
	"""Generalized UniFrac Distances, Distance-Based Multivariate
Methods and Feature-Based Univariate Methods for Microbiome
Data Analysis

	A suite of methods for powerful and robust microbiome data analysis including data normalization, data simulation, community-level association testing and differential abundance analysis. It implements generalized UniFrac distances,  Geometric Mean of Pairwise Ratios (GMPR) normalization, semiparametric data simulator, distance-based statistical methods, and feature-based statistical methods. The distance-based statistical methods include three extensions of PERMANOVA: (1) PERMANOVA using the Freedman-Lane permutation scheme, (2) PERMANOVA omnibus test using multiple matrices, and  (3) analytical approach to approximating PERMANOVA p-value. Feature-based statistical methods include linear model-based methods for differential abundance analysis of zero-inflated high-dimensional compositional data. 
	"""
	
	cran = "GUniFrac" 

	version("1.8", md5="5117c6e23fa9da45978808b23144bba3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
