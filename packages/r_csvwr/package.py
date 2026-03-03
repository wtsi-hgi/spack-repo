# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsvwr(RPackage):
	"""Read and Write CSV on the Web (CSVW) Tables and Metadata

	Provide functions for reading and writing CSVW - i.e. CSV tables and JSON metadata.
    The metadata helps interpret CSV by setting the types and variable names.
	"""
	
	homepage = "https://robsteranium.github.io/csvwr/"
	cran = "csvwr" 

	version("0.1.7", md5="e2355fc6f5b92125ccae54c861254803")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
