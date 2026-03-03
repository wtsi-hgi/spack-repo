# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRJive(RPackage):
	"""Perform JIVE Decomposition for Multi-Source Data

	Performs the Joint and Individual Variation Explained (JIVE) decomposition on a list of data sets when the data share a dimension, returning low-rank matrices that capture the joint and individual structure of the data [O'Connell, MJ and Lock, EF (2016) <doi:10.1093/bioinformatics/btw324>]. It provides two methods of rank selection when the rank is unknown, a permutation test and a Bayesian Information Criterion (BIC) selection algorithm. Also included in the package are three plotting functions for visualizing the variance attributed to each data source: a bar plot that shows the percentages of the variability attributable to joint and individual structure, a heatmap that shows the structure of the variability, and principal component plots. 
	"""
	
	cran = "r.jive" 

	version("2.4", md5="2eec4b28cf04c4c8109b9cc66845dd9a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
