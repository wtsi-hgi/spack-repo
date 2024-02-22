# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBibliometrix(RPackage):
	"""Comprehensive Science Mapping Analysis

	Tool for quantitative research in scientometrics and bibliometrics.
    It provides various routines for importing bibliographic data from 'SCOPUS',
    'Clarivate Analytics Web of Science' (<https://www.webofknowledge.com/>), 'Digital Science Dimensions' 
	(<https://www.dimensions.ai/>), 'Cochrane Library' (<https://www.cochranelibrary.com/>),  'Lens' (<https://lens.org>), 
	and 'PubMed' (<https://pubmed.ncbi.nlm.nih.gov/>) databases, performing bibliometric analysis 
    and building networks for co-citation, coupling, scientific collaboration and co-word analysis.
	"""
	
	homepage = "https://www.bibliometrix.org"
	cran = "bibliometrix" 

	version("4.1.4", md5="672ecab3491295552fc9e190c3cc4892")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bibliometrixdata", type=("build", "run"))
	depends_on("r-dimensionsr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-openalexr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pubmedr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rscopus", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
