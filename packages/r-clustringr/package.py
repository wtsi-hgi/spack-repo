# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustringr(RPackage):
	"""Cluster Strings by Edit-Distance

	Returns an edit-distance based clusterization of an input vector of strings.
    Each cluster will contain a set of strings w/ small mutual edit-distance
    (e.g., Levenshtein, optimum-sequence-alignment, Damerau-Levenshtein), as computed by
    stringdist::stringdist(). The set of all mutual edit-distances is then used by
    graph algorithms (from package 'igraph') to single out subsets of high connectivity.
	"""
	
	cran = "clustringr" 

	version("1.0", md5="798919425d43bcf5d0443d96f6ac7ffc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
