# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivepathways(RPackage):
	"""Integrative Pathway Enrichment Analysis of Multivariate Omics
Data

	Framework for analysing multiple omics datasets in the context of molecular pathways, biological processes and other types of gene sets. The package uses p-value merging to combine gene- or protein-level signals, followed by ranked hypergeometric tests to determine enriched pathways and processes. This approach allows researchers to interpret a series of omics datasets in the context of known biology and gene function, and discover associations that are only apparent when several datasets are combined. The first version of the package is part of the following publication: Integrative Pathway Enrichment Analysis of Multivariate Omics Data. Paczkowska M^, Barenboim J^, Sintupisut N, Fox NS, Zhu H, Abd-Rabbo D, Mee MW, Boutros PC, PCAWG Drivers and Functional Interpretation Working Group; Reimand J, PCAWG Consortium. Nature Communications (2020) <doi:10.1038/s41467-019-13983-9>.
	"""
	
	cran = "ActivePathways" 

	version("2.0.3", md5="e05703006dfee7236296e6a77f049237")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
