# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REyelinker(RPackage):
	"""Import ASC Files from EyeLink Eye Trackers

	Imports plain-text ASC data files from EyeLink eye trackers 
    into (relatively) tidy data frames for analysis and visualization.
	"""
	
	homepage = "https://github.com/a-hurst/eyelinker"
	cran = "eyelinker" 

	version("0.2.1", md5="e7d53ca393cc67ecc9b187ceb797f90f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-intervals", type=("build", "run"))
