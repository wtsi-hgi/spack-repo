# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmopgenerics(RPackage):
	"""Methods and Classes for the OMOP Common Data Model

	Provides definitions of core classes and methods used by analytic 
    pipelines that query the OMOP (Observational Medical Outcomes Partnership) 
    common data model.
	"""
	
	homepage = "https://darwin-eu-dev.github.io/omopgenerics/"
	cran = "omopgenerics" 

	version("0.0.2", md5="366af0ff6c2b6280f2ed878ed9e58d0d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
