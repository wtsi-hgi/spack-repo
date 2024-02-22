# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVersus(RPackage):
	"""Compare Data Frames

	A toolset for interactively exploring the differences between two data frames.
	"""
	
	homepage = "https://eutwt.github.io/versus/"
	cran = "versus" 

	version("0.3.0", md5="17ef3b56bcacac253d61e8dd8623723e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-collapse@2.0.9:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
