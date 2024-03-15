# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCadra(RPackage):
	"""Candidate Driver Analysis

	Performs both stepwise and backward heuristic search for candidate (epi)genetic drivers based on a binary multi-omics dataset. CaDrA's main objective is to identify features which, together, are significantly skewed or enriched pertaining to a given vector of continuous scores (e.g. sample-specific scores representing a phenotypic readout of interest, such as protein expression, pathway activity, etc.), based on the union occurence (i.e. logical OR) of the events.
	"""
	
	homepage = "https://github.com/montilab/CaDrA/"
	bioc = "CaDrA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CaDrA_1.0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CaDrA/CaDrA_1.0.1.tar.gz"]

	version("1.0.1", md5="9ac2bc6afe6632e5fbd00c687ca19bba")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
