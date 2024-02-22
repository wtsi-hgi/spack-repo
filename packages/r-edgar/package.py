# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdgar(RPackage):
	"""Tool for the U.S. SEC EDGAR Retrieval and Parsing of Corporate
Filings

	In the USA, companies file different forms with the U.S. 
    Securities and Exchange Commission (SEC) through EDGAR (Electronic 
    Data Gathering, Analysis, and Retrieval system). The EDGAR 
    database automated system collects all the different necessary 
    filings and makes it publicly available. This package facilitates
    retrieving, storing, searching, and parsing of all the available 
    filings on the EDGAR server. It downloads filings from SEC 
    server in bulk with a single query. Additionally, it provides 
    various useful functions: extracts 8-K triggering events, extract
    "Business (Item 1)" and "Management's Discussion and Analysis(Item 7)"
    sections of annual statements, searches filings for desired 
    keywords, provides sentiment measures, parses filing header 
    information, and provides HTML view of SEC filings.  
	"""
	
	cran = "edgar" 

	version("2.0.7", md5="c569512025f02c3192aaf62fe9673317")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
