# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStorywranglr(RPackage):
	"""Explore Twitter Trends with the 'Storywrangler' API

	An interface to explore trends in Twitter data using the 
    'Storywrangler' Application Programming Interface (API), which can be found
    here: <https://github.com/janeadams/storywrangler>.
	"""
	
	homepage = "https://github.com/chris31415926535/storywranglr"
	cran = "storywranglr" 

	version("0.2.0", md5="7a3afe2ab48a47696c7f6015e004622c")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
