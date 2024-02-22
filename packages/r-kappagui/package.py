# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKappagui(RPackage):
	"""An R-Shiny Application for Calculating Cohen's and Fleiss' Kappa

	Offers a graphical user interface for the evaluation of inter-rater agreement with Cohen's and Fleiss' Kappa. The calculation of kappa statistics is done using the R package 'irr', so that 'KappaGUI' is essentially a Shiny front-end for 'irr'.
	"""
	
	cran = "KappaGUI" 

	version("2.0.2", md5="39ab574bf1c3e642d7c696dc278031e5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
