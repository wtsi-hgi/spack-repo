# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPollen(RPackage):
	"""Analysis of Aerobiological Data

	Supports analysis of aerobiological data. 
    Available features include determination of pollen season limits, 
    replacement of outliers (Kasprzyk and Walanus (2014) <doi:10.1007/s10453-014-9332-8>),
    calculation of growing degree days (Baskerville and Emin (1969) <doi:10.2307/1933912>), 
    and determination of the base temperature for growing degree days
    (Yang et al. (1995) <doi:10.1016/0168-1923(94)02185-M).
	"""
	
	homepage = "https://nowosad.github.io/pollen/"
	cran = "pollen" 

	version("0.82.0", md5="b633c53b07ffd477e89b42a2b697217d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
