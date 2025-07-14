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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GNET2_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GNET2/GNET2_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="36873c17e13e0fc19e2ba28699981969ea32344f8ca6a10dde314de4b857659c", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GNET2_1.18.0.tar.gz")

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
