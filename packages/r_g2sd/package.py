# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RG2sd(RPackage):
	"""Grain-Size Statistics and Description of Sediment

	Full descriptive statistics, physical description of sediment,
            metric or phi sieves.
	"""
	
	homepage = "https://cran.r-project.org/package=G2Sd"
	cran = "G2Sd" 

	version("2.1.5", md5="15832f717e4644dc6b261b31e41782ea")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-xlsxjars", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
