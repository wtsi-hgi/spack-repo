# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSalesforcer(RPackage):
	"""An Implementation of 'Salesforce' APIs Using Tidy Principles

	Functions connecting to the 'Salesforce' Platform APIs (REST, SOAP, 
    Bulk 1.0, Bulk 2.0, Metadata, Reports and Dashboards) 
    <https://trailhead.salesforce.com/en/content/learn/modules/api_basics/api_basics_overview>. 
    "API" is an acronym for "application programming interface". Most all calls 
    from these APIs are supported as they use CSV, XML or JSON data that can be 
    parsed into R data structures. For more details please see the 'Salesforce' 
    API documentation and this package's website 
    <https://stevenmmortimer.github.io/salesforcer/> for more information, 
    documentation, and examples.
	"""
	
	homepage = "https://github.com/StevenMMortimer/salesforcer"
	cran = "salesforcer" 

	version("1.0.1", md5="6277744e8efb3dc51191203f15c28785")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-vctrs@0.3.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.8:", type=("build", "run"))
	depends_on("r-anytime@0.3.9:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-xml@3.99.0.3:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-rlist@0.4.6.1:", type=("build", "run"))
	depends_on("r-zip@2.0.4:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-mime@0.9:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
