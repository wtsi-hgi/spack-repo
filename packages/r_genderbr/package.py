# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenderbr(RPackage):
	"""Predict Gender from Brazilian First Names

	A method to predict and report gender from Brazilian first names
    using the Brazilian Institute of Geography and Statistics' Census data (<https://censo2010.ibge.gov.br/nomes/>).
	"""
	
	homepage = "https://github.com/meirelesff/genderBR"
	cran = "genderBR" 

	version("1.1.2", md5="e490060ae685f9fa5b951ac696080468")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
