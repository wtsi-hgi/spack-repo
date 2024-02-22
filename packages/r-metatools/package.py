# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetatools(RPackage):
	"""Enable the Use of 'metacore' to Help Create and Check Dataset

	Uses the metadata information stored in 'metacore' objects to check and build metadata associated columns.
	"""
	
	homepage = "https://pharmaverse.github.io/metatools/"
	cran = "metatools" 

	version("0.1.5", md5="cf6725f85baa1cbcc2d5c7c3b51a4a7d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-metacore@0.0.4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
