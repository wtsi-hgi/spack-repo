# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobaltrends(RPackage):
	"""Download and Measure Global Trends Through Google Search Volumes

	Google offers public access to global search volumes from its
    search engine through the Google Trends portal. The package downloads
    these search volumes provided by Google Trends and uses them to
    measure and analyze the distribution of search scores across countries
    or within countries. The package allows researchers and analysts to
    use these search scores to investigate global trends based on patterns
    within these scores. This offers insights such as degree of
    internationalization of firms and organizations or dissemination of
    political, social, or technological trends across the globe or within
    single countries.  An outline of the package's methodological
    foundations and potential applications is available as a working
    paper: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3969013>.
	"""
	
	homepage = "https://github.com/ha-pu/globaltrends/"
	cran = "globaltrends" 

	version("0.0.14", md5="6b5b500fbc3bab029e6c56a1fb004247")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-dbplyr@1.4.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-forecast@8.12:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-gtrendsr@1.5.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-rsqlite@2.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-zoo@1.8.8:", type=("build", "run"))
