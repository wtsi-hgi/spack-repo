# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactoclass(RPackage):
	"""Combination of Factorial Methods and Cluster Analysis

	Some functions of 'ade4' and 'stats' are combined in order to obtain 
             a partition of the rows of a data table, with columns representing 
             variables of scales: quantitative, qualitative or frequency. 
             First, a principal axes method is performed and then, a combination 
             of Ward agglomerative hierarchical classification and K-means is 
             performed, using some of the first coordinates obtained from the 
             previous principal axes method. 
             In order to permit different weights of the elements to be clustered, 
             the function 'kmeansW', programmed in C++, is included. 
             It is a modification of 'kmeans'. Some graphical functions include 
             the option: 'gg=FALSE'.  When 'gg=TRUE', they  use the 'ggplot2' 
             and 'ggrepel' packages to avoid  the super-position of the labels.   
	"""
	
	cran = "FactoClass" 

	version("1.2.9", md5="8a7ecf5480035f1bc99271f48aec0c99")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
