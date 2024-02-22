# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMclm(RPackage):
	"""Mastering Corpus Linguistics Methods

	Read, inspect and process corpus files for quantitative corpus linguistics.
  Obtain concordances via regular expressions, tokenize texts,
  and compute frequencies and association measures. Useful for collocation analysis,
  keywords analysis and variationist studies (comparison of linguistic variants
  and of linguistic varieties).
	"""
	
	homepage = "https://github.com/masterclm/mclm"
	cran = "mclm" 

	version("0.2.7", md5="334a7ab5508b954a5ce6056c2193ea1a")

	depends_on("r-ca", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
