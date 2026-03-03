# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetlattes(RPackage):
	"""Import and Process Data from the 'Lattes' Curriculum Platform

	Tool for import and process data from 'Lattes' curriculum platform (<http://lattes.cnpq.br/>). The Brazilian government keeps an extensive base of curricula for academics from all over the country, with over 5 million registrations. The academic life of the Brazilian researcher, or related to Brazilian universities, is documented in 'Lattes'. Some information that can be obtained: professional formation, research area, publications, academics advisories, projects, etc. 'getLattes' package allows work with 'Lattes' data exported to XML format.
	"""
	
	homepage = "https://github.com/roneyfraga/getLattes"
	cran = "getLattes" 

	version("0.2.0", md5="ee5a4dfe18eedd73c9e01aed2605a768")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-piper", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
