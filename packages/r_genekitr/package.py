# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenekitr(RPackage):
	"""Gene Analysis Toolkit

	An analysis toolkit focused on genes. It mainly includes five
    features (search, convert, analysis, plot, and export).
    The user just needs to input feature id ('entrez', 'symbol', 'ensembl' or
    'uniprot') to retrieve feature information and 'PubMed'<https://pubmed.ncbi.nlm.nih.gov/> records, 
    to convert id types, to easily handle gene enrichment analysis and publication-level figures, 
    to plot group interaction and export results as sheets in one 'excel'
    file to easily share and communicate with others.
	"""
	
	homepage = "https://www.genekitr.fun/"
	cran = "genekitr" 

	version("1.2.5", md5="8963315be41ac977657fa8c3e0866025")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-europepmc", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-geneset", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggvenn", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
