# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnet2(RPackage):
	"""Constructing gene regulatory networks from expression data through functional module inference

	Cluster genes to functional groups with E-M process. Iteratively perform TF assigning and Gene assigning, until the assignment of genes did not change, or max number of iterations is reached.
	"""
	
	homepage = "https://github.com/chrischen1/GNET2"
	bioc = "GNET2"

	version("1.24.0", commit="9743478572fb195a041921609b29ce9e6f56c6e2")
	version("1.18.0", commit="49bc07bf09f1eaa6f0de2574a99e2a0f31ba1f2a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
