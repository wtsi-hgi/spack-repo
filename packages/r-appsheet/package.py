# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppsheet(RPackage):
	"""An Interface to the 'AppSheet' API

	Functionality to add, delete, read and update table
    records from your 'AppSheet' apps, using the official API <https://api.appsheet.com/>.
	"""
	
	homepage = "https://github.com/calderonsamuel/appsheet"
	cran = "appsheet" 

	version("0.1.0", md5="970b91f15faf5c80a8183ffbba33d984")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
