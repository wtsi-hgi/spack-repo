# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedcapdm(RPackage):
	"""'REDCap' Data Management

	REDCap Data Management - REDCapDM is a comprehensive package that enables users to seamlessly handle data exported directly from REDCap or through API connections. This tool facilitates various functions, including data preprocessing, report generation for queries such as outliers or missing values, and tracking of identified queries. 'REDCap' (Research Electronic Data CAPture; <https://projectredcap.org>) is a web application developed at Vanderbilt University, designed for creating and managing online surveys and databases. The API connection provides users with the capability to programmatically access both data and project metadata, including the data dictionary, from the web.
	"""
	
	homepage = "https://bruigtp.github.io/REDCapDM/"
	cran = "REDCapDM" 

	version("0.9.8", md5="d271886e0376c033b9fbc06497ed5118")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-redcapr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
