# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuler(RPackage):
	"""Tidy Data Validation Reports

	Tools for creating data validation pipelines and
    tidy reports. This package offers a framework for exploring and
    validating data frame like objects using 'dplyr' grammar of data
    manipulation.
	"""
	
	homepage = "https://echasnovski.github.io/ruler/"
	cran = "ruler" 

	version("0.3.0", md5="eeb4a73625da43f9a523f13156823acc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-keyholder", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@0.7:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
