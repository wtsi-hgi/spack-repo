# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaryn(RPackage):
	"""Native Access Medical Record Retriever for High Yield Analytics

	A toolkit for medical records data analysis. The 'naryn'
    package implements an efficient data structure for storing medical
    records, and provides a set of functions for data extraction,
    manipulation and analysis.
	"""
	
	homepage = "https://tanaylab.github.io/naryn/"
	cran = "naryn" 

	version("2.6.26", md5="c67472ddaab1db5337de40bfc0f36602")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
