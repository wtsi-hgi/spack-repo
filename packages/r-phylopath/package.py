# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylopath(RPackage):
	"""Perform Phylogenetic Path Analysis

	A comprehensive and easy to use R implementation of confirmatory
    phylogenetic path analysis as described by Von Hardenberg and Gonzalez-Voyer
    (2012) <doi:10.1111/j.1558-5646.2012.01790.x>.
	"""
	
	homepage = "https://Ax3man.github.io/phylopath/"
	cran = "phylopath" 

	version("1.2.1", md5="7003e8d8299619a11eb7fd131f72396f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape@4.1:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggm@2.3:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggraph@1:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-mumin@1.15.6:", type=("build", "run"))
	depends_on("r-phylolm@2.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
