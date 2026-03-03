# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierarchicalsets(RPackage):
	"""Set Data Visualization Using Hierarchies

	Pure set data visualization approaches are often limited in
    scalability due to the combinatorial explosion of distinct set families as
    the number of sets under investigation increases. hierarchicalSets applies
    a set centric hierarchical clustering of the sets under investigation and
    uses this hierarchy as a basis for a range of scalable visual
    representations. hierarchicalSets is especially well suited for collections
    of sets that describe comparable comparable entities as it relies on the
    sets to have a meaningful relational structure.
	"""
	
	cran = "hierarchicalSets" 

	version("1.0.4", md5="38ed91e5d1781180eaff79b485a9c341")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
