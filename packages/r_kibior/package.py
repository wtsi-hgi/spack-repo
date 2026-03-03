# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKibior(RPackage):
	"""A Simple Data Management and Sharing Tool

	An interface to store, retrieve, search, join and share datasets, based on Elasticsearch (ES) API. As a decentralized, FAIR and collaborative search engine and database effort, it proposes a simple push/pull/search mechanism only based on ES, a tool which can be deployed on nearly any hardware. It is a high-level R-ES binding to ease data usage using 'elastic' package (S. Chamberlain (2020)) <https://docs.ropensci.org/elastic/>, extends joins from 'dplyr' package (H. Wickham et al. (2020)) <https://dplyr.tidyverse.org/> and integrates specific biological format importation with Bioconductor packages such as 'rtracklayer' (M. Lawrence and al. (2009) <doi:10.1093/bioinformatics/btp328>) <http://bioconductor.org/packages/rtracklayer>, 'Biostrings' (H. Pagès and al. (2020) <doi:10.18129/B9.bioc.Biostrings>) <http://bioconductor.org/packages/Biostrings>, and 'Rsamtools' (M. Morgan and al. (2020) <doi:10.18129/B9.bioc.Rsamtools>) <http://bioconductor.org/packages/Rsamtools>, but also a long list of more common ones with 'rio' (C-h. Chan and al. (2018)) <https://cran.r-project.org/package=rio>.
	"""
	
	homepage = "https://github.com/regisoc/kibior"
	cran = "kibior" 

	version("0.1.1", md5="84e9fcf33f13e7a1bfdf73cb447050b7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r6@2.5:", type=("build", "run"))
	depends_on("r-data-table@1.13.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.1:", type=("build", "run"))
	depends_on("r-rio@0.5.16:", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-elastic@1.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
