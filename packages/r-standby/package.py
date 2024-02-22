# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStandby(RPackage):
	"""Alerts, Notifications and Loading Screen in 'Shiny'

	Easily create alerts, notifications, modals, info tips and loading 
    screens in 'Shiny'. Includes several options to customize alerts and 
    notifications by including text, icons, images and buttons. When wrapped 
    around a 'Shiny' output, loading screen is automatically displayed while 
    the output is being recalculated.
	"""
	
	homepage = "https://standby.rsquaredacademy.com/"
	cran = "standby" 

	version("0.1.0", md5="fd650e6c9507921d6440f3eea195a9d5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
