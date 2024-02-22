# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcml(RPackage):
	"""Consensus Clustering for Different Sample Coverage Data

	Consensus clustering, also called meta-clustering or cluster ensembles, has been increasingly 
    used in clinical data. Current consensus clustering methods tend to ensemble a number of different 
    clusters from mathematical replicates with similar sample coverage. As the fact of common variety
    of sample coverage in the real-world data, a new consensus clustering strategy dealing with
    such biological replicates is required. This is a two-step consensus clustering package, which
    is used to input multiple predictive labels with different sample coverage (missing labels). 
	"""
	
	cran = "ccml" 

	version("1.4.0", md5="c05b5c45f42d3eade3ff6aa85b9de478")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dicer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-snftool", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-consensusclusterplus@1.56:", type=("build", "run"))
