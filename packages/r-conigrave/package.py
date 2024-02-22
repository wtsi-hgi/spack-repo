# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConigrave(RPackage):
	"""Flexible Tools for Multiple Imputation

	Provides a set of tools that can be used across 'data.frame' and
    'imputationList' objects.
	"""
	
	cran = "Conigrave" 

	version("0.4.4", md5="321d1c85f66c83b854ee911ed44620fa")

	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-stringdist@0.9.5.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-ppcor@1.1:", type=("build", "run"))
	depends_on("r-mitools@2.4:", type=("build", "run"))
	depends_on("r-miceadds@3.2.48:", type=("build", "run"))
