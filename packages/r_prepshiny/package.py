# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrepshiny(RPackage):
	"""Interactive Document for Preprocessing the Dataset

	An interactive document for preprocessing the dataset using  'rmarkdown' and 'shiny' packages. Runtime examples are provided in the package function as well as at  <https://analyticmodels.shinyapps.io/PREPShiny/>.
	"""
	
	cran = "PREPShiny" 

	version("0.1.0", md5="a06adacf13e0f5be25a825d78e3aaf55")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-psycho", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
