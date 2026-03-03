# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemnetcleaner(RPackage):
	"""An Automated Cleaning Tool for Semantic and Linguistic Data

	Implements several functions that automates the cleaning and spell-checking of text data. Also converges, finalizes, removes plurals and continuous strings, and puts text data in binary format for semantic network analysis. Uses the 'SemNetDictionaries' package to make the cleaning process more accurate, efficient, and reproducible.
	"""
	
	homepage = "https://github.com/AlexChristensen/SemNetCleaner"
	cran = "SemNetCleaner" 

	version("1.3.4", md5="ef956ada15563d5bda37f2eedeaf3eeb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-semnetdictionaries@0.1.8:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-searcher", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-easycsv", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-editdata", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
