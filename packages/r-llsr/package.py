# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLlsr(RPackage):
	"""Data Analysis of Liquid-Liquid Systems using R

	Originally design to characterise Aqueous Two Phase Systems, LLSR provide a simple way to analyse experimental data and obtain phase diagram parameters, among other properties, systematically. The package will include (every other update) new functions in order to comprise useful tools in liquid-liquid extraction research.
	"""
	
	homepage = "https://CRAN.R-project.org/package=LLSR"
	cran = "LLSR" 

	version("0.0.3.1", md5="4a64adecc7100e4e9f4392c927232bc6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-svdialogs", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
