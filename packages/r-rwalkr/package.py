# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwalkr(RPackage):
	"""API to Melbourne Pedestrian Data

	Provides API to Melbourne pedestrian and weather data
    <https://data.melbourne.vic.gov.au> in tidy data form.
	"""
	
	homepage = "https://pkg.earo.me/rwalkr/"
	cran = "rwalkr" 

	version("0.5.7", md5="04edcb0063ae30319710d1080dc78913")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
