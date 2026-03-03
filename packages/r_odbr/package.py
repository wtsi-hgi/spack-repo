# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdbr(RPackage):
	"""Download Data from Brazil's Origin Destination Surveys

	Download data from Brazil's Origin Destination Surveys. The package covers both data from household travel surveys, dictionaries of variables, and the spatial geometries of surveys conducted in different years and across various urban areas in Brazil. For some cities, the package will include enhanced versions of the data sets with variables "harmonized" across different years.
	"""
	
	cran = "odbr" 

	version("0.1.0", md5="2eaa2232019bdc6bdbb5f7a21d0557ed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-piggyback", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
