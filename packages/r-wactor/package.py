# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWactor(RPackage):
	"""Word Factor Vectors

	A user-friendly factor-like interface for converting strings of
    text into numeric vectors and rectangular data structures.
	"""
	
	homepage = "https://github.com/mkearney/wactor"
	cran = "wactor" 

	version("0.0.1", md5="cfc03ff7db14ae752998a7759a6e772e")

	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-text2vec", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
