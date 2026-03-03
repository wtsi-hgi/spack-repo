# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatsearchanalyticsr(RPackage):
	"""An Interface for the 'STAT Search Analytics' 'API'

	Pull data from the 'STAT Search Analytics' API <https://help.getstat.com/knowledgebase/api-services/>. It was developed by the Search Discovery team to help analyze keyword ranking data.
	"""
	
	homepage = "https://searchdiscovery.github.io/statsearchanalyticsr/"
	cran = "statsearchanalyticsr" 

	version("0.1.4", md5="998df9d833eb8570d4288fd64b090be2")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
