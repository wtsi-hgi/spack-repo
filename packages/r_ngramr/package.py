# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgramr(RPackage):
	"""Retrieve and Plot Google n-Gram Data

	Retrieve and plot word frequencies through time from the "Google
    Ngram Viewer" <https://books.google.com/ngrams>.
	"""
	
	homepage = "https://github.com/seancarmody/ngramr"
	cran = "ngramr" 

	version("1.9.3", md5="2e2ce2c7b48a027f61ddb9bc64a6079c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr@1.0.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
