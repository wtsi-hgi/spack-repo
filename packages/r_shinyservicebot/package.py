# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyservicebot(RPackage):
	"""Servicebot 'Shiny' Integration

	Create in-app purchasing and subscriptions through 'Servicebot' payment using the 'Stripe' framework.
	"""
	
	homepage = "https://github.com/capiaas/shinyservicebot"
	cran = "shinyservicebot" 

	version("0.1.0", md5="08d0818fc49f3b8823b0d25354606df6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-htmltools@0.2.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.6:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
