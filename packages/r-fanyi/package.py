# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFanyi(RPackage):
	"""Translate Words or Sentences via Online Translators

	Useful functions to translate text for multiple languages using online translators. 
    For example, by translating error messages and descriptive analysis results into a language familiar
    to the user, it enables a better understanding of the information, thereby reducing the barriers caused by language.
    It offers several helper functions to query gene information to help interpretation of interested genes (e.g., marker genes, differential expression genes),
    and provides utilities to translate 'ggplot' graphics.
	"""
	
	homepage = "https://github.com/YuLab-SMU/fanyi"
	cran = "fanyi" 

	version("0.0.6", md5="f6ce3e845ebe31b1f266d1dc1606aaf8")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ggfun", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sseparser", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-yulab-utils@0.1.3:", type=("build", "run"))
