# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMycran(RPackage):
	"""Graph of Daily and Cumulative Downloads of your Packages

	Plot the daily and cumulative number of downloads of your packages.
    It is designed to be slightly more convenient than the several similar programs. If you want to run this each morning,
    you do not need to keep typing in the names of your packages. Also, this combines the daily and cumulative counts in one
    run, you do not need to run separate programs to get both types of information.
	"""
	
	cran = "myCRAN" 

	version("1.1", md5="d328d6132eb9010c46e8d87186341a14")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cranlogs", type=("build", "run"))
	depends_on("r-pkgsearch", type=("build", "run"))
