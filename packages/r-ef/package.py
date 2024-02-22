# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REf(RPackage):
	"""Modelling Framework for the Estimation of Salmonid Abundance

	A set of functions to estimate capture probabilities and
  densities from multipass pass removal data.
	"""
	
	cran = "ef" 

	version("1.2.0", md5="3503270d920b066a21ffe53cfafabf97")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
