# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REganet(RPackage):
	"""Exploratory Graph Analysis – a Framework for Estimating the
Number of Dimensions in Multivariate Data using Network
Psychometrics

	Implements the Exploratory Graph Analysis (EGA) framework for dimensionality
             and psychometric assessment. EGA estimates the number of dimensions in
	     psychological data using network estimation methods and community detection
             algorithms. A bootstrap method is provided to assess the stability of dimensions
	     and items. Fit is evaluated using the Entropy Fit family of indices. Unique 
             Variable Analysis evaluates the extent to which items are locally dependent (or
             redundant). Network loadings provide similar information to factor loadings and
	     can be used to compute network scores. A bootstrap and permutation approach are
             available to assess configural and metric invariance. Hierarchical structures
             can be detected using Hierarchical EGA. Time series and intensive longitudinal 
	     data can be analyzed using Dynamic EGA, supporting individual, group, and 
             population level assessments.
	"""
	
	homepage = "https://r-ega.net"
	cran = "EGAnet" 

	version("2.0.5", md5="82a86eca7bdeb596efe1add7a4694307")
	version("2.0.4", md5="183213a6e614bd0a8e6a63acccbb71c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-fungible", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-igraph@1.3:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
