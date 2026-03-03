# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatahari(RPackage):
	"""Spy on Your R Session

	Conveniently log everything you type into the R console. Logs are
    are stored as tidy data frames which can then be analyzed using 'tidyverse'
    style tools.
	"""
	
	homepage = "https://github.com/jhudsl/matahari"
	cran = "matahari" 

	version("0.1.3", md5="9b41614a9866327b0cd95d11bd74a9ce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
