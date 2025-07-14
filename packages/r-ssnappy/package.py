# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsnappy(RPackage):
	"""Single Sample directioNAl Pathway Perturbation analYsis

	A single sample pathway perturbation testing method for RNA-seq data. The method propagates changes in gene expression down gene-set topologies to compute single-sample directional pathway perturbation scores that reflect potential direction of change. Perturbation scores can be used to test significance of pathway perturbation at both individual-sample and treatment levels.
	"""
	
	homepage = "https://wenjun-liu.github.io/sSNAPPY/"
	bioc = "sSNAPPY"

	version("1.12.0", commit="8905dd77f53dc0be46a7569052e84777dc742d90")
	version("1.6.1", md5="15f7a550e110c069710c3f6572a06e83")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
