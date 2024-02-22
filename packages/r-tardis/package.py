# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTardis(RPackage):
	"""Text Analysis with Rules and Dictionaries for Inferring
Sentiment

	Measure text's sentiment with dictionaries and simple rules covering
    negations and modifiers. User-supplied dictionaries are supported, including
    Unicode emojis and multi-word tokens, so this package can also be used to
    study constructs beyond sentiment.
	"""
	
	homepage = "https://github.com/chris31415926535/tardis"
	cran = "tardis" 

	version("0.1.4", md5="d6ff2a21581064656394fe585b3b7a64")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
