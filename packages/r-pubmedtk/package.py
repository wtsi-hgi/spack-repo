# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubmedtk(RPackage):
	"""'Pubmed' Toolkit

	Provides various functions for retrieving and
    interpreting information from 'Pubmed' via the API,
    <https://www.ncbi.nlm.nih.gov/home/develop/api/>.
	"""
	
	homepage = "https://github.com/bgcarlisle/pubmedtk"
	cran = "pubmedtk" 

	version("1.0.2", md5="1d961635b08a9b871577821931ff844c")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
