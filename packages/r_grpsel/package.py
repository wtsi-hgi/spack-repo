# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpsel(RPackage):
	"""Group Subset Selection

	Provides tools for sparse regression modelling with grouped predictors using the group 
    subset selection penalty. Uses coordinate descent and local search algorithms to rapidly deliver 
    near optimal estimates. The group subset penalty can be combined with a group lasso or ridge 
    penalty for added shrinkage. Linear and logistic regression are supported, as are overlapping 
    groups.
	"""
	
	homepage = "https://github.com/ryan-thompson/grpsel"
	cran = "grpsel" 

	version("1.3.1", md5="7845431365d42b46d1849ae3b423e1dd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
