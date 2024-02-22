# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelenv(RPackage):
	"""Provide Tools to Register Models for Use in 'tidymodels'

	An developer focused, low dependency package in 'tidymodels' that
    provides functions to register how models are to be used. Functions to
    register models are complimented with accessor functions to retrieve
    registered model information to aid in model fitting and error handling.
	"""
	
	homepage = "https://github.com/tidymodels/modelenv"
	cran = "modelenv" 

	version("0.1.1", md5="3ea3e9365c8c36752036b20aec780a6f")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
