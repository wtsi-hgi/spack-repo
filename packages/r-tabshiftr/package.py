# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabshiftr(RPackage):
	"""Reshape Disorganised Messy Data

	Helps the user to build and register schema descriptions of 
    disorganised (messy) tables. Disorganised tables are tables that are 
    not in a topologically coherent form, where packages such as 'tidyr' could 
    be used for reshaping. The schema description documents the arrangement of 
    input tables and is used to reshape them into a standardised (tidy) output 
    format.
	"""
	
	homepage = "https://github.com/luckinet/tabshiftr"
	cran = "tabshiftr" 

	version("0.4.1", md5="e05d0aebf2e6edabf12e740cec895c00")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
