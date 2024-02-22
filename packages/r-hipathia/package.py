# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHipathia(RPackage):
	"""HiPathia: High-throughput Pathway Analysis

	Hipathia is a method for the computation of signal transduction along signaling pathways from transcriptomic data. The method is based on an iterative algorithm which is able to compute the signal intensity passing through the nodes of a network by taking into account the level of expression of each gene and the intensity of the signal arriving to it. It also provides a new approach to functional analysis allowing to compute the signal arriving to the functions annotated to each pathway.
	"""
	
	bioc = "hipathia" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/hipathia_3.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/hipathia/hipathia_3.2.0.tar.gz"]

	version("3.2.0", md5="819d2eecca55d3d4708934bbe69e82a7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-annotationhub@2.6.5:", type=("build", "run"))
	depends_on("r-multiassayexperiment@1.4.9:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.8.1:", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-metbrewer", type=("build", "run"))
