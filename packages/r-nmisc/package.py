# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmisc(RPackage):
	"""Miscellaneous Functions Used at 'Numeract LLC'

	Contains functions useful for debugging, set operations on vectors,
    and 'UTC' date and time functionality. It adds a few vector manipulation 
    verbs to 'purrr' and 'dplyr' packages. It can also generate an R file to 
    install and update packages to simplify deployment into production. The 
    functions were developed at the data science firm 'Numeract LLC' and are 
    used in several packages and projects.
	"""
	
	homepage = "https://github.com/numeract/Nmisc"
	cran = "Nmisc" 

	version("0.3.7", md5="1417dd5ad18882abee8b473333ca440c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
