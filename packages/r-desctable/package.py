# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesctable(RPackage):
	"""Produce Descriptive and Comparative Tables Easily

	Easily create descriptive and comparative tables.
    It makes use and integrates directly with the tidyverse family of packages, and pipes.
    Tables are produced as (nested) dataframes for easy manipulation.
	"""
	
	homepage = "https://desctable.github.io"
	cran = "desctable" 

	version("0.3.0", md5="90f858888ef4b6d4a95b9cb07a89f23e")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
