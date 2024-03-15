# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDce(RPackage):
	"""Pathway Enrichment Based on Differential Causal Effects

	Compute differential causal effects (dce) on (biological) networks. Given observational samples from a control experiment and non-control (e.g., cancer) for two genes A and B, we can compute differential causal effects with a (generalized) linear regression. If the causal effect of gene A on gene B in the control samples is different from the causal effect in the non-control samples the dce will differ from zero. We regularize the dce computation by the inclusion of prior network information from pathway databases such as KEGG.
	"""
	
	homepage = "https://github.com/cbg-ethz/dce"
	bioc = "dce" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/dce_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/dce/dce_1.10.0.tar.gz"]

	version("1.10.0", md5="dbebdd246ea193f92c1a466a84617876")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-epinem", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-mnem", type=("build", "run"))
	depends_on("r-naturalsort", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-harmonicmeanp", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-shadowtext", type=("build", "run"))
