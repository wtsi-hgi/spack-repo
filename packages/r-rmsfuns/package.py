# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmsfuns(RPackage):
	"""Quickly View Data Frames in 'Excel', Build Folder Paths and
Create Date Vectors

	Contains several useful navigation helper functions, including easily building
    folder paths, quick viewing dataframes in 'Excel', creating date vectors and changing the
    console prompt to reflect time.
	"""
	
	homepage = "https://rmsfuns.nfkatzke.com"
	cran = "rmsfuns" 

	version("1.0.0.1", md5="f56c3067e6ccd754fd0994acc1fc8130")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tbl2xts", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
