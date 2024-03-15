# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReformulas(RPackage):
	"""Machinery for Processing Random Effect Formulas

	Takes formulas including random-effects components (formatted as in 'lme4', 'glmmTMB', etc.) and processes them. Includes various helper functions.
	"""
	
	homepage = "https://github.com/bbolker/reformulas"
	cran = "reformulas" 

	version("0.2.0", md5="1ed50cd59333fa72aff4bff2bb40804b")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
