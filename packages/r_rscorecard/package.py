# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRscorecard(RPackage):
	"""A Method to Download Department of Education College Scorecard
Data

	A method to download Department of Education College
     Scorecard data using the public API
     <https://collegescorecard.ed.gov/data/documentation/>. It is based on
     the 'dplyr' model of piped commands to select and filter data in a
     single chained function call.  An API key from the U.S. Department of
     Education is required.
	"""
	
	homepage = "https://github.com/btskinner/rscorecard"
	cran = "rscorecard" 

	version("0.26.0", md5="5b39cf74bf12824554eaeb0e65d7542c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
