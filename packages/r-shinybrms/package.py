# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinybrms(RPackage):
	"""Graphical User Interface ('shiny' App) for 'brms'

	A graphical user interface (GUI) for fitting Bayesian regression
    models using the package 'brms' which in turn relies on 'Stan'
    (<https://mc-stan.org/>). The 'shinybrms' GUI is a 'shiny' app.
	"""
	
	homepage = "https://fweber144.github.io/shinybrms/"
	cran = "shinybrms" 

	version("1.8.0", md5="139dba47d28870c68e6b3b44bdedb315")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-brms@2.16:", type=("build", "run"))
	depends_on("r-rstan@2.19.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
