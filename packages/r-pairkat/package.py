# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairkat(RPackage):
	"""PaIRKAT

	PaIRKAT is model framework for assessing statistical relationships between networks of metabolites (pathways) and an outcome of interest (phenotype). PaIRKAT queries the KEGG database to determine interactions between metabolites from which network connectivity is constructed. This model framework improves testing power on high dimensional data by including graph topography in the kernel machine regression setting. Studies on high dimensional data can struggle to include the complex relationships between variables. The semi-parametric kernel machine regression model is a powerful tool for capturing these types of relationships. They provide a framework for testing for relationships between outcomes of interest and high dimensional data such as metabolomic, genomic, or proteomic pathways. PaIRKAT uses known biological connections between high dimensional variables by representing them as edges of ‘graphs’ or ‘networks.’ It is common for nodes (e.g. metabolites) to be disconnected from all others within the graph, which leads to meaningful decreases in testing power whether or not the graph information is included. We include a graph regularization or ‘smoothing’ approach for managing this issue.
	"""
	
	bioc = "pairkat" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/pairkat_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/pairkat/pairkat_1.8.0.tar.gz"]

	version("1.8.0", md5="030b0f4ea6e9f71adf6769ca9b16cae0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
