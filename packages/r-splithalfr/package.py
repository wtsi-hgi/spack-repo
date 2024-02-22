# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplithalfr(RPackage):
	"""Estimate Split-Half Reliabilities

	Estimates split-half reliabilities for scoring algorithms of cognitive tasks and questionnaires. The 'splithalfr' supports researcher-provided scoring algorithms, with six vignettes illustrating how on included datasets. The package provides four splitting methods (first-second, odd-even, permutated, Monte Carlo), the option to stratify splits by task design, a number of reliability coefficients, and the option to sub-sample data.
	"""
	
	homepage = "https://github.com/tpronk/splithalfr"
	cran = "splithalfr" 

	version("2.2.2", md5="61fd52a0b80c4b64af6cccfeb50ec69d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-psych@1.8.12:", type=("build", "run"))
	depends_on("r-bcaboot@0.2.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
