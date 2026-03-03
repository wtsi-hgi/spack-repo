# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocxtools(RPackage):
	"""Tools for R Markdown to Docx Documents

	A set of helper functions for using R Markdown to create documents
    in docx format, especially documents for use in a classroom or workshop
    setting.
	"""
	
	homepage = "https://github.com/graphdr/docxtools"
	cran = "docxtools" 

	version("0.3.0", md5="7e0b879d06dc6c0d165e81b87f2afa4c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
