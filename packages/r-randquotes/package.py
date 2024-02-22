# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandquotes(RPackage):
	"""Get Random Quotes from Quotes on Design API

	Connects to the site <http://quotesondesign.com/> 
            that uses the 'WordPress' built-in REST API 
            to provide a way for you to grab quotes.
	"""
	
	homepage = "https://github.com/amrrs/randquotes"
	cran = "randquotes" 

	version("0.1.1", md5="ea5cda8d3be6daf7ec98b34fd8c7fac4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
