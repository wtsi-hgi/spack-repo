# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvconverter(RPackage):
	"""Apply Transformations to Data

	Provides a set of functions for data transformations.
    Transformations are performed on character and numeric data. As the scope of the package is
    within Student Analytics, there are functions focused around the academic year.
	"""
	
	cran = "vvconverter" 

	version("0.5.9", md5="46918b93a7ccbe88479591b78212a662")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-polyglotr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
