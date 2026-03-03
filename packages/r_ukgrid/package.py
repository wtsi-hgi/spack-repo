# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkgrid(RPackage):
	"""The UK National Electricity Transmission System Dataset

	A time series of the national grid demand (high-voltage electric power transmission network) in the UK since 2011.
	"""
	
	homepage = "https://github.com/RamiKrispin/UKgrid"
	cran = "UKgrid" 

	version("0.1.3", md5="2c668c1c89e75253f1cc35964032a7af")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-data-table@1.11.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tsibble@0.9:", type=("build", "run"))
	depends_on("r-xts@0.12:", type=("build", "run"))
	depends_on("r-zoo@1.8.0:", type=("build", "run"))
