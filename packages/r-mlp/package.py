# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlp(RPackage):
	"""Mean Log P Analysis

	Pathway analysis based on p-values associated to genes from a genes expression analysis of interest. Utility functions enable to extract pathways from the Gene Ontology Biological Process (GOBP), Molecular Function (GOMF) and Cellular Component (GOCC), Kyoto Encyclopedia of Genes of Genomes (KEGG) and Reactome databases. Methodology, and helper functions to display the results as a table, barplot of pathway significance, Gene Ontology graph and pathway significance are available.
	"""
	
	bioc = "MLP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MLP_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MLP/MLP_1.50.0.tar.gz"]

    version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="9093f4a28a2c7d8dc13000dadf362d0207cb9127cf09175e6cb00582bac00642")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
