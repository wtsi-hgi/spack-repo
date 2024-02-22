# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppeears(RPackage):
	"""Interface to 'AppEEARS' NASA Web Services

	Programmatic interface to the NASA Application for Extracting and Exploring Analysis Ready Samples services (AppEEARS; <https://appeears.earthdatacloud.nasa.gov/>).
 The package provides easy access to analysis ready earth observation data in R.
	"""
	
	homepage = "https://github.com/bluegreen-labs/appeears"
	cran = "appeears" 

	version("1.1", md5="8a5f4510f7397bf0233b3ae23b00e14c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-geojsonio", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
