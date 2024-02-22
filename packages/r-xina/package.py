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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/XINA_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/XINA/XINA_1.20.0.tar.gz"]

	version("1.20.0", md5="f6a090d9e94032485c8c42a6c985b223")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-alluvial", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
