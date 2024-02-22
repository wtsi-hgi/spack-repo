# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReliabilitydiag(RPackage):
	"""Reliability Diagrams Using Isotonic Regression

	Checking the reliability of predictions via the CORP approach,
    which generates provably statistically 'C'onsistent, 'O'ptimally binned, and
    'R'eproducible reliability diagrams using the 'P'ool-adjacent-violators
    algorithm. See Dimitriadis, Gneiting, Jordan (2021) <doi:10.1073/pnas.2016191118>.
	"""
	
	homepage = "https://github.com/aijordan/reliabilitydiag/"
	cran = "reliabilitydiag" 

	version("0.2.1", md5="7b6b6d6023febd34276215a1b5ba9fe0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-bde", type=("build", "run"))
