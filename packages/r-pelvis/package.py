# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPelvis(RPackage):
	"""Probabilistic Sex Estimate using Logistic Regression, Based on
VISual Traits of the Human Os Coxae

	An R-Shiny application implementing a method of sexing the human os coxae based on logistic regressions and Bruzek's nonmetric traits <doi:10.1002/ajpa.23855>.
	"""
	
	homepage = "https://gitlab.com/f-santos/pelvis/"
	cran = "PELVIS" 

	version("2.0.4", md5="7d92847d6b0513ca723f3d4b222778bc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
