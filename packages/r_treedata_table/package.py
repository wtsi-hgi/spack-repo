# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreedataTable(RPackage):
	"""Manipulation of Matched Phylogenies and Data using 'data.table'

	An implementation that combines trait data and a phylogenetic tree (or trees) into a 
    single object of class treedata.table. The resulting object can be easily 
    manipulated to simultaneously change the trait- and tree-level sampling.
    Currently implemented functions allow users to use a 'data.table' syntax when
    performing operations on the trait dataset within the treedata.table object.
	"""
	
	homepage = "https://docs.ropensci.org/treedata.table/"
	cran = "treedata.table" 

	version("0.1.0", md5="88e62c05100a0019db4766ded8be7f37")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
