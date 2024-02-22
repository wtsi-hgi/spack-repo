# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpidata(RPackage):
	"""Tools to Retrieve Economic Policy Institute Data Library
Extracts

	The Economic Policy Institute (<https://www.epi.org/>) provides
    researchers, media, and the public with easily accessible, up-to-date, and
    comprehensive historical data on the American labor force. It is compiled
    from Economic Policy Institute analysis of government data sources. Use
    it to research wages, inequality, and other economic indicators over time
    and among demographic groups. Data is usually updated monthly.
	"""
	
	homepage = "https://gitlab.com/hrbrmstr/epidata"
	cran = "epidata" 

	version("0.4.0", md5="28d7cea393d766cad0c0ada142275f92")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tinytest", type=("build", "run"))
