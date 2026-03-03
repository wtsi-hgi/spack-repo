# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJustifyalpha(RPackage):
	"""Justifying Alpha Levels for Hypothesis Tests

	Functions to justify alpha levels for statistical hypothesis tests by avoiding Lindley's paradox, or by minimizing or balancing error rates. For more information about the package please read the following: Maier & Lakens (2021) <doi:10.31234/osf.io/ts4r6>).
	"""
	
	cran = "JustifyAlpha" 

	version("0.1.1", md5="f233555f1c5ec48e7b7e79ff66392d63")

	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-superpower", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
