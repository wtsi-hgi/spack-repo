# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsbclust(RPackage):
	"""Least-Squares Bilinear Clustering for Three-Way Data

	Functions for performing least-squares bilinear clustering of
    three-way data. The method uses the bilinear decomposition (or bi-additive
    model) to model two-way matrix slices while clustering over the third way.
    Up to four different types of clusters are included, one for each term of the
    bilinear decomposition. In this way, matrices are clustered simultaneously on
    (a subset of) their overall means, row margins, column margins and row-column
    interactions. The orthogonality of the bilinear model results in separability of
    the joint clustering problem into four separate ones. Three of these sub-problems
    are specific k-means problems, while a special algorithm is implemented for the
    interactions. Plotting methods are provided, including biplots for the low-rank
    approximations of the interactions.
	"""
	
	cran = "lsbclust" 

	version("1.1", md5="bbea60978a4bd16809d7043623d47367")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
