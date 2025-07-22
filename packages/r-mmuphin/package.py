# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmuphin(RPackage):
	"""Meta-analysis Methods with Uniform Pipeline for Heterogeneity in Microbiome Studies

	MMUPHin is an R package for meta-analysis tasks of microbiome cohorts. It has function interfaces for: a) covariate-controlled batch- and cohort effect adjustment, b) meta-analysis differential abundance testing, c) meta-analysis unsupervised discrete structure (clustering) discovery, and d) meta-analysis unsupervised continuous structure discovery.
	"""
	
	bioc = "MMUPHin"

	version("1.22.0", commit="6dd5463d5a65305034da9d3d4d3b3bdd5ad2ebb8")
	version("1.16.0", commit="61bc5dc476d68ccea15e666b3756e87c6ee6d27b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-maaslin2", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("glpk@4.57:", type=("build", "link", "run"))
