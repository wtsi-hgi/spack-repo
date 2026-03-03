# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmlconvert(RPackage):
	"""Comfortably Converting XML Documents to Dataframes and Vice
Versa

	Converts XML documents to R dataframes and dataframes to XML documents.
  A wide variety of options allows for different XML formats and flexible control
  of the conversion process. Results can be exported to CSV and Excel, if desired. 
  Also converts XML data to R lists.
	"""
	
	homepage = "https://github.com/jsugarelli/xmlconvert/"
	cran = "xmlconvert" 

	version("0.1.2", md5="7820a1d89026599c386ab48c2727e427")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
