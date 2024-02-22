# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlashier(RPackage):
	"""Empirical Bayes Matrix Factorization

	Methods for matrix factorization based on Wang and Stephens (2021) 
    <https://jmlr.org/papers/v22/20-589.html>.
	"""
	
	homepage = "https://github.com/willwerscheid/flashier"
	cran = "flashier" 

	version("1.0.7", md5="9ba2fd76c6cceae00405714349462aa0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ebnm@0.1.21:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
