# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFedregs(RPackage):
	"""Text Analysis of the US Code of Federal Regulations

	The Code of Federal Regulations (CFR) annual edition is the codification 
    of the general and permanent rules published in the Federal Register by the departments
    and agencies of the Federal Government of the United States of America. Simply, the 
    'fedregs' package facilitates word processing and sentiment analysis of the CFR using tidy 
    principles. Note: According to the Code of Federal Regulations XML Rendition User Guide Document: 
    "In general, there are no restrictions on re-use of information in Code of Federal Regulations
    material because U.S. Government works are not subject to copyright. OFR and GPO do not
    restrict downstream uses of Code of Federal Regulations data, except that independent providers
    should be aware that only the OFR and GPO are entitled to represent that they are the providers
    of the official versions of the Code of Federal Regulations and related Federal Register
    publications."
	"""
	
	cran = "fedregs" 

	version("1.0.0", md5="2c3fe7db4666dcba6dd16b541332e3d3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-stringi@1.1.7:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidytext@0.1.9:", type=("build", "run"))
