# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGibasa(RPackage):
	"""An Alternative 'Rcpp' Wrapper of 'MeCab'

	A plain 'Rcpp' wrapper of 'MeCab' that can segment Chinese,
    Japanese, and Korean text into tokens. The main goal of this package
    is to provide an alternative to 'tidytext' using morphological
    analysis.
	"""
	
	homepage = "https://paithiov909.github.io/gibasa/"
	cran = "gibasa" 

	version("1.1.0", md5="c85cd9227fd091d362824a876875d176")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
