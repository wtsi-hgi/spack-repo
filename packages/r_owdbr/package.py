# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROwdbr(RPackage):
	"""Open Welfare Data Brazil

	Tools for collecting municipal-level data <http://www.transparencia.gov.br/swagger-ui.html> from several Brazilian governmental social programs.
	"""
	
	homepage = "https://github.com/kimjoaoun/owdbr"
	cran = "owdbr" 

	version("1.0.1.1", md5="3d75afd4ce59f0394e6e2153763f2a31")

	depends_on("r@3.4.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
