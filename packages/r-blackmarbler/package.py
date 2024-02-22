# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlackmarbler(RPackage):
	"""Black Marble Data and Statistics

	Geographically referenced data and statistics of nighttime lights from NASA Black Marble <https://blackmarble.gsfc.nasa.gov/>.
	"""
	
	homepage = "https://worldbank.github.io/blackmarbler/"
	cran = "blackmarbler" 

	version("0.1.2", md5="f078003810900b6ec2f05778479f692a")

	depends_on("r-readr", type=("build", "run"))
	depends_on("r-hdf5r", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-exactextractr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
