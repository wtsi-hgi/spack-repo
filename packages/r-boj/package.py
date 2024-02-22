# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoj(RPackage):
	"""Interface to Bank of Japan Statistics

	Provides an interface to Bank of Japan <https://www.boj.or.jp>
  statistics.
	"""
	
	cran = "BOJ" 

	version("0.3", md5="d406fc43ad17243e5f7ddee8c699c357")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
