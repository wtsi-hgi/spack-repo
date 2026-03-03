# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkr(RPackage):
	"""Network Analysis and Visualization

	Collection of functions for fast manipulation, handling, and analysis of large-scale
    networks based on family and social data. Functions are utility functions used to manipulate data
    in three "formats": sparse adjacency matrices, pedigree trio family data, and pedigree family data.
    When possible, the functions should be able to handle millions of data points quickly for use in combination
    with data from large public national registers and databases.
    Kenneth Lange (2003, ISBN:978-8181281135).
	"""
	
	cran = "networkR" 

	version("0.1.2", md5="af1a8a95c2d0fd8f01b7c0030a2d7447")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
