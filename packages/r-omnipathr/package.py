# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmnipathr(RPackage):
	"""OmniPath web service client and more

	A client for the OmniPath web service (https://www.omnipathdb.org) and many other resources. It also includes functions to transform and pretty print some of the downloaded data, functions to access a number of other resources such as BioPlex, ConsensusPathDB, EVEX, Gene Ontology, Guide to Pharmacology (IUPHAR/BPS), Harmonizome, HTRIdb, Human Phenotype Ontology, InWeb InBioMap, KEGG Pathway, Pathway Commons, Ramilowski et al. 2015, RegNetwork, ReMap, TF census, TRRUST and Vinayagam et al. 2011. Furthermore, OmnipathR features a close integration with the NicheNet method for ligand activity prediction from transcriptomics data, and its R implementation `nichenetr` (available only on github).
	"""
	
	homepage = "https://r.omnipathdb.org/"
	bioc = "OmnipathR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OmnipathR_3.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OmnipathR/OmnipathR_3.10.1.tar.gz"]

	version("3.10.1", md5="c51296b40e8d580f14dc3ff6839495f6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
