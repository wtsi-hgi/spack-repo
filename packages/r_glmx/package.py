# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmx(RPackage):
	"""Generalized Linear Models Extended

	Extended techniques for generalized linear models (GLMs), especially for binary responses,
             including parametric links and heteroscedastic latent variables.
	"""
	
	cran = "glmx" 

	version("0.2-0", md5="809eac8845e282100ce327852a725682")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
