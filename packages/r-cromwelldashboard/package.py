# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCromwelldashboard(RPackage):
	"""A Dashboard to Visualize Scientific Workflows in 'Cromwell'

	A dashboard supports the usage of 'cromwell'. 
 'Cromwell' is a scientific workflow engine for command line users.
 This package utilizes 'cromwell' REST APIs and provides these convenient 
 functions: timing diagrams for running workflows, 'cromwell' engine status, 
 a tabular workflow list. For more information about 'cromwell', 
 visit <http://cromwell.readthedocs.io>.
	"""
	
	cran = "cromwellDashboard" 

	version("0.5.1", md5="7c932f8690aec97ce8e8a7258d68074d")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
