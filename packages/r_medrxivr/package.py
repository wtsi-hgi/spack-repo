# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedrxivr(RPackage):
	"""Access and Search MedRxiv and BioRxiv Preprint Data

	An increasingly important source of health-related bibliographic 
    content are preprints - preliminary versions of research articles that have
    yet to undergo peer review. The two preprint repositories most relevant to 
    health-related sciences are medRxiv <https://www.medrxiv.org/> and
    bioRxiv <https://www.biorxiv.org/>, both of which are operated by the Cold 
    Spring Harbor Laboratory. 'medrxivr' provides programmatic access to the 
    'Cold Spring Harbour Laboratory (CSHL)' API <https://api.biorxiv.org/>,
    allowing users to easily download medRxiv and bioRxiv preprint metadata
    (e.g. title, abstract, publication date, author list, etc) into R. 
    'medrxivr' also provides functions to search the downloaded preprint records 
    using regular expressions and Boolean logic, as well as helper functions 
    that allow users to export their search results to a .BIB file for easy 
    import to a reference manager and to download the full-text PDFs of 
    preprints matching their search criteria.
	"""
	
	homepage = "https://github.com/ropensci/medrxivr"
	cran = "medrxivr" 

	version("0.0.5", md5="a572143633b82745fd1016833c4c4427")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-bib2df", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
