# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWidyr(RPackage):
	"""Widen, Process, then Re-Tidy Data

	Encapsulates the pattern of untidying data into a wide
    matrix, performing some processing, then turning it back into a tidy
    form. This is useful for several operations such as co-occurrence
    counts, correlations, or clustering that are mathematically convenient
    on wide matrices.
	"""
	
	homepage = "https://github.com/juliasilge/widyr"
	cran = "widyr" 

	version("0.1.5", md5="d641268fe803fd707ed10deca13a474d")

	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
