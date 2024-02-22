# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnheadr(RPackage):
	"""Handle Data with Messy Header Rows and Broken Values

	Verb-like functions to work with messy data, often derived from 
             spreadsheets or parsed PDF tables. Includes functions for unwrapping 
             values broken up across rows, relocating embedded grouping values, 
             and to annotate meaningful formatting in spreadsheet files.
	"""
	
	homepage = "https://github.com/luisDVA/unheadr"
	cran = "unheadr" 

	version("0.3.3", md5="e3f0c286ef03051e5443a3716dce8450")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-rlang@0.2.1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyxl", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
