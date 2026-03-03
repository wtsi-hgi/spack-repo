# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpi(RPackage):
	"""Access the U.S. National Provider Identifier Registry API

	Access the United States National Provider Identifier
    Registry API <https://npiregistry.cms.hhs.gov/api/>. Obtain and transform
    administrative data linked to a specific individual or organizational
    healthcare provider, or perform advanced searches based on provider name,
    location, type of service, credentials, and other attributes exposed by
    the API.
	"""
	
	homepage = "https://github.com/ropensci/npi/"
	cran = "npi" 

	version("0.2.0", md5="7b6e93ab63fffa0a4d22e3811d8cfdc9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkluhn", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
