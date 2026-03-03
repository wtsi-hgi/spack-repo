# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytometree(RPackage):
	"""Automated Cytometry Gating and Annotation

	Given the hypothesis of a bi-modal distribution of cells for
    each marker, the algorithm constructs a binary tree, the nodes of which are
    subpopulations of cells. At each node, observed cells and markers are modeled
    by both a family of normal distributions and a family of bi-modal normal mixture
    distributions. Splitting is done according to a normalized difference of AIC
    between the two families. Method is detailed in: Commenges, Alkhassim, Gottardo, 
    Hejblum & Thiebaut (2018) <doi: 10.1002/cyto.a.23601>. 
	"""
	
	cran = "cytometree" 

	version("2.0.2", md5="c2db466ee7825ed47ab03496ec4db086")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-gofkernel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
