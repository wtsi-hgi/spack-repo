# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavaanShiny(RPackage):
	"""Latent Variable Analysis with Shiny

	Interactive shiny application for working with different kinds of
    latent variable analysis, with the 'lavaan' package. Graphical output for models
    are provided and different estimators are supported.
	"""
	
	homepage = "https://github.com/kylehamilton/lavaan.shiny"
	cran = "lavaan.shiny" 

	version("1.2", md5="2b866c2dbb21827233523f0dfc922966")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
