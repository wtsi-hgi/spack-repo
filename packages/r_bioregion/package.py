# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioregion(RPackage):
	"""Comparison of Bioregionalisation Methods

	The main purpose of this package is to propose a transparent methodological framework to compare bioregionalisation methods based on hierarchical and non-hierarchical clustering algorithms (Kreft & Jetz (2010) <doi:10.1111/j.1365-2699.2010.02375.x>) and network algorithms (Lenormand et al. (2019) <doi:10.1002/ece3.4718> and Leroy et al. (2019) <doi:10.1111/jbi.13674>).
	"""
	
	homepage = "https://github.com/bioRgeo/bioregion"
	cran = "bioregion" 

	version("1.1.0", md5="d248e1254d9ec4df4ac0f32e00afb8cf")
	version("1.0.0", md5="7401daff7bd87109da191f2d1f80b418")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-fastkmedoids", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
