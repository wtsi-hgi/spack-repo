# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXina(RPackage):
	"""Multiplexes Isobaric Mass Tagged-based Kinetics Data for Network Analysis

	The aim of XINA is to determine which proteins exhibit similar patterns within and across experimental conditions, since proteins with co-abundance patterns may have common molecular functions. XINA imports multiple datasets, tags dataset in silico, and combines the data for subsequent subgrouping into multiple clusters. The result is a single output depicting the variation across all conditions. XINA, not only extracts coabundance profiles within and across experiments, but also incorporates protein-protein interaction databases and integrative resources such as KEGG to infer interactors and molecular functions, respectively, and produces intuitive graphical outputs.
	"""
	
	bioc = "XINA"

	version("1.26.0", commit="6ab511ac6b017b94020fa2f25af0a33e6c7142de")
	version("1.20.0", commit="8ca83bc0400740d17790388b7da88f576fcbb7d0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-alluvial", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
