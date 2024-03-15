# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROne4all(RPackage):
	"""Validate, Share, and Download Data

	Designed to enhance data validation and management processes by employing a set of functions that read a set of rules from a 'CSV' or 'Excel' file and apply them to a dataset. Funded by the National Renewable Energy Laboratory and Possibility Lab, maintained by the Moore Institute for Plastic Pollution Research.
	"""
	
	homepage = "https://github.com/Moore-Institute-4-Plastic-Pollution-Res/One4All"
	cran = "One4All" 

	version("0.4", md5="bff4f9b4662858708867b45cd7962027")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-validate", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ckanr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-lexicon", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mongolite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
