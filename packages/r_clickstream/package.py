# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClickstream(RPackage):
	"""Analyzes Clickstreams Based on Markov Chains

	A set of tools to read, analyze and write lists of click sequences
    on websites (i.e., clickstream). A click can be represented by a number,
    character or string. Clickstreams can be modeled as zero- (only computes
    occurrence probabilities), first- or higher-order Markov chains.
	"""
	
	cran = "clickstream" 

	version("1.3.3", md5="31a4fb7649d0a6df0dcba40e983ed990")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-linprog", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-clickclust", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
