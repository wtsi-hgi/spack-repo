# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParsel(RPackage):
	"""Parallel Dynamic Web-Scraping Using 'RSelenium'

	A system to increase the efficiency of dynamic web-scraping with 'RSelenium'
    by leveraging parallel processing. You provide a function wrapper for your 'RSelenium' 
    scraping routine with a set of inputs, and 'parsel' runs it in several browser instances. 
    Chunked input processing as well as error catching and logging ensures seamless 
    execution and minimal data loss, even when unforeseen 'RSelenium' errors occur. You can additionally 
    build safe scraping functions with minimal coding by utilizing constructor functions that act as wrappers 
    around 'RSelenium' methods. 
	"""
	
	homepage = "https://github.com/till-tietz/parsel"
	cran = "parsel" 

	version("0.3.0", md5="68561e332b5e4f9738f0a7067612e657")

	depends_on("r-rselenium", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
