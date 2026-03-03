# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoveffectsplot(RPackage):
	"""Produce Forest Plots to Visualize Covariate Effects

	Produce forest plots to visualize covariate effects using either
    the command line or an interactive 'Shiny' application.
	"""
	
	homepage = "https://smouksassi.github.io/coveffectsplot/"
	cran = "coveffectsplot" 

	version("1.0.5", md5="e12282547ac170c70cc6ce6060b739e9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
