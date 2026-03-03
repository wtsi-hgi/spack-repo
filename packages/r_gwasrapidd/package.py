# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasrapidd(RPackage):
	"""'REST' 'API' Client for the 'NHGRI'-'EBI' 'GWAS' Catalog

	'GWAS' R 'API' Data Download.
    This package provides easy access to the 'NHGRI'-'EBI' 'GWAS' Catalog data by
    accessing the 'REST' 'API' <https://www.ebi.ac.uk/gwas/rest/docs/api/>.
	"""
	
	homepage = "https://github.com/ramiromagno/gwasrapidd"
	cran = "gwasrapidd" 

	version("0.99.17", md5="68f6ad6ece261d48c63a456ee335c4ec")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-concatenate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidyr@0.8.99:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
