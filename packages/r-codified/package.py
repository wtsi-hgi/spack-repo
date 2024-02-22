# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodified(RPackage):
	"""Produce Standard/Formalized Demographics Tables

	Augment clinical data with metadata to create
    output used in conventional publications and reports.
	"""
	
	homepage = "https://ouhscbbmc.github.io/codified/"
	cran = "codified" 

	version("0.3.0", md5="f1330d53934b78f1c478b1a5edc0213b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate@1.8.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr@1.18:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
