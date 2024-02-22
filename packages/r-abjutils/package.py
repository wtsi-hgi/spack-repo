# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbjutils(RPackage):
	"""Useful Tools for Jurimetrical Analysis Used by the Brazilian
Jurimetrics Association

	The Brazilian Jurimetrics Association (ABJ in Portuguese, see
    <https://abj.org.br/> for more information) is a non-profit
    organization which aims to investigate and promote the use of
    statistics and probability in the study of Law and its institutions.
    This package implements general purpose tools used by ABJ, such as
    functions for sampling and basic manipulation of Brazilian lawsuits
    identification number. It also implements functions for text cleaning,
    such as accentuation removal.
	"""
	
	homepage = "https://github.com/abjur/abjutils"
	cran = "abjutils" 

	version("0.3.2", md5="3b2f11ee82ac1ef0bf38de4207213273")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
