# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnpivotr(RPackage):
	"""Unpivot Complex and Irregular Data Layouts

	Tools for converting data from complex or irregular layouts to a
    columnar structure.  For example, tables with multilevel column or row
    headers, or spreadsheets.  Header and data cells are selected by their
    contents and position, as well as formatting and comments where available,
    and are associated with one other by their proximity in given directions.
    Functions for data frames and HTML tables are provided.
	"""
	
	homepage = "https://github.com/nacnudus/unpivotr"
	cran = "unpivotr" 

	version("0.6.3", md5="559235090be6b13bfda54fd311b71b73")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-cellranger", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
