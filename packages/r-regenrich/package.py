# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegenrich(RPackage):
	"""Gene regulator enrichment analysis

	This package is a pipeline to identify the key gene regulators in a biological process, for example in cell differentiation and in cell development after stimulation. There are four major steps in this pipeline: (1) differential expression analysis; (2) regulator-target network inference; (3) enrichment analysis; and (4) regulators scoring and ranking.
	"""
	
	bioc = "RegEnrich" 

    version("1.18.1", tag="RELEASE_3_21")
	version("1.12.0", commit="0524ae661d5e148d84abf9ab6c3052ff97defbf0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-biocset", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
