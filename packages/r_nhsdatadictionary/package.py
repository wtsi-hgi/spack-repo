# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhsdatadictionary(RPackage):
	"""NHS Data Dictionary Toolset for NHS Lookups

	Providing a common set of simplified web scraping tools for working with the NHS Data Dictionary <https://datadictionary.nhs.uk/data_elements_overview.html>.
    The intended usage is to access the data elements section of the NHS Data Dictionary to access key lookups.
    The benefits of having it in this package are that the lookups are the live lookups on the website and will not need to be maintained.
    This package was commissioned by the NHS-R community <https://nhsrcommunity.com/> to provide this consistency of lookups.
    The OpenSafely lookups have now been added <https://www.opencodelists.org/docs/>.
	"""
	
	cran = "NHSDataDictionaRy" 

	version("1.2.5", md5="a7808b6a824e432cdb19b1ae6a62360c")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
