# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidysmd(RPackage):
	"""Tidy Standardized Mean Differences

	Tidy standardized mean differences ('SMDs'). 'tidysmd' uses
    the 'smd' package to calculate standardized mean differences for
    variables in a data frame, returning the results in a tidy format.
	"""
	
	homepage = "https://github.com/r-causal/tidysmd"
	cran = "tidysmd" 

	version("0.2.0", md5="ccfaa4f2a47c773abdccfc35932a7acb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-smd", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
