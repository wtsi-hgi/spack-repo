# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdam(RPackage):
	"""ADAM: Activity and Diversity Analysis Module

	ADAM is a GSEA R package created to group a set of genes from comparative samples (control versus experiment) belonging to different species according to their respective functions (Gene Ontology and KEGG pathways as default) and show their significance by calculating p-values referring togene diversity and activity. Each group of genes is called GFAG (Group of Functionally Associated Genes).
	"""
	
	bioc = "ADAM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ADAM_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ADAM/ADAM_1.18.0.tar.gz"]

	version("1.18.0", md5="7f051085afca603520dbb5cb010e58fe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-go-db@3.6:", type=("build", "run"))
	depends_on("r-keggrest@1.20.2:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pbapply@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-dt@0.4:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.10.1:", type=("build", "run"))
