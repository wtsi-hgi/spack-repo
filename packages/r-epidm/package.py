# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpidm(RPackage):
	"""UK Epidemiological Data Management

	Contains utilities and functions for the cleaning, processing and
    management of patient level public health data for surveillance
    and analysis held by the UK Health Security Agency, UKHSA.
	"""
	
	homepage = "https://github.com/alexbhatt/epidm"
	cran = "epidm" 

	version("1.0.4", md5="0bca4941f1cf26069ea734b5bd645c38")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-phonics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
