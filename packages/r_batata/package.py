# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatata(RPackage):
	"""Managing Packages Removal and Installation

	
    Allows the user to manage easily R packages removal and installation. It offers many functions to display installed packages according to
    specific dates and removes them if needed. The user is always prompted when running the removal functions in order to confirm
    the required action. It also provides functions that will install 'Github' starred R packages whether available on 'CRAN' or not. 
	"""
	
	homepage = "https://github.com/feddelegrand7/batata"
	cran = "batata" 

	version("0.2.1", md5="f299617cbc922452534139ad6cc40de4")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
