# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollateral(RPackage):
	"""Quickly Evaluate Captured Side Effects

	Map functions while capturing results, errors, warnings, messages and other output tidily, then filter and summarise data frames or lists on the basis of those side effects.
	"""
	
	homepage = "https://collateral.jamesgoldie.dev"
	cran = "collateral" 

	version("0.5.2", md5="62cde42da33a31e7a1fa619bcd9b0839")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
