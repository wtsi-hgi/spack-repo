# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychreport(RPackage):
	"""Reproducible Reports in Psychology

	Helper functions for producing reports in Psychology (Reproducible Research). Provides required formatted strings (APA style) for use in 'Knitr'/'Latex' integration within *.Rnw files.
	"""
	
	cran = "psychReport" 

	version("3.0.2", md5="09e1bc0b7ab4f03afcb06cf90f79b174")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ez", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
