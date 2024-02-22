# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreedimensiontest(RPackage):
	"""Trajectory Presence and Heterogeneity in Multivariate Data

	Testing for trajectory presence and heterogeneity on
 multivariate data. Two statistical methods (Tenha & Song 2022) 
 <doi:10.1371/journal.pcbi.1009829> are implemented. The tree dimension
 test quantifies the statistical evidence for trajectory presence. The
 subset specificity measure summarizes pattern heterogeneity using the
 minimum subtree cover. There is no user tunable parameters for either
 method. Examples are included to illustrate how to use the methods on 
 single-cell data for studying gene and pathway expression dynamics and
 pathway expression specificity.
	"""
	
	cran = "TreeDimensionTest" 

	version("0.0.2", md5="5bc3e2ff978429c4c865f39d8f35c8ce")

	depends_on("r-mlpack", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nfactors", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
