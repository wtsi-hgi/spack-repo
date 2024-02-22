# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataloader(RPackage):
	"""Import Multiple File Types

	Functions to import multiple files of multiple data file types ('.xlsx', '.xls', '.csv', '.txt')
             from a given directory into R data frames.
	"""
	
	cran = "DataLoader" 

	version("1.3", md5="d19a6bfb24d98ec8f4a05b550ab569a5")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-rchoicedialogs", type=("build", "run"))
